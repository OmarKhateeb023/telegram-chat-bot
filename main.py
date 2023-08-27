import datetime
import logging
from datetime import datetime
from enum import Enum

import os
from typing import List
from bs4 import BeautifulSoup

import requests
import openai
import urllib


from telegram import ForceReply, Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters, JobQueue


from api_tokens import TELEGRAM_BOT_TOKEN , OPENAI_API_KEY
from article_extractor import summarise_link,get_latest_news, ExtractedArticle
from exceptions import InvalidArticleLink
from dotenv import load_dotenv

load_dotenv()

subscribed_users = dict()

openai.api_key = OPENAI_API_KEY


class UserCommand(Enum):
    start = 'start'
    summarise = 'summarise'
    subscribe = 'subscribe'


users_last_command = dict()

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.ERROR
)

# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.INFO)
logger = logging.getLogger(__name__)


def add_last_command(chat_id, last_action: UserCommand):
    users_last_command[chat_id] = last_action

async def send_command_list(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[KeyboardButton(text='/subscribe'),
                 KeyboardButton(text='/summarise')]]
    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=True,
                                       resize_keyboard=True)
    await update.message.reply_markdown("Please choose your command", reply_markup=reply_markup)


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    add_last_command(update.message.chat_id, UserCommand.start)
    await update.message.reply_html(
        rf"Hi {user.mention_html()}! "
        rf"Welcome to our news summary bot!",
        reply_markup=ForceReply(selective=True),
    )
    await send_command_list(update, context)

async def do_subscribe(update: Update, context: ContextTypes.DEFAULT_TYPE):
    #   parse time from text then replace desired time
    try:
        desired_time = datetime.strptime(update.message.text, "%H:%M")
        print(desired_time.time())
        subscribed_users[update.message.chat_id] = desired_time
        await update.message.reply_text("You've successfully subscribed to our daily summarized news!")
    except Exception:
        await update.message.reply_text("Please enter a valid time [HH:MM]")

async def subscribe_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    add_last_command(update.message.chat_id, UserCommand.subscribe)
    keyboard = [[KeyboardButton(text='8:00'),
                 KeyboardButton(text='10:00'),
                 KeyboardButton(text='12:00'),
                 KeyboardButton(text='14:00'),
                 KeyboardButton(text='16:00')]]
    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=True,
                                       resize_keyboard=True)
    await update.message.reply_markdown_v2("Please choose the hour to receive the daily summary [HH:MM]",
                                           reply_markup=reply_markup)

async def do_summarise(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_text = update.message.text
    try:
        article = await summarise_link(message_text)
        await update.message.reply_text(article.article_summary)
    except InvalidArticleLink as e:
        await update.message.reply_text("Invalid article url!")

async def summarise_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    add_last_command(update.message.chat_id, UserCommand.summarise)
    await update.message.reply_text("Please enter the article link you would like to summarise")


async def do_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    last_command = users_last_command.get(chat_id, None)

    if last_command == UserCommand.summarise:
        await do_summarise(update, context)
    elif last_command == UserCommand.subscribe:
        await do_subscribe(update, context)
    else:
        pass

    users_last_command.pop(chat_id, None)
    await send_command_list(update, context)

async def send_summary_to_subs(context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send the subscription summary to all users"""
    for chat_id, desired_time in subscribed_users.items():
        current_time = datetime.now().time()
        if ((current_time.hour == desired_time.hour
                and current_time.minute == desired_time.minute)
                and current_time.second == desired_time.second):
            articles = await get_latest_news()
            for article in articles:
                await context.bot.send_message(chat_id=chat_id, text=article.article_summary)


def start_app() -> None:
    # Create the Application
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start_command))

    application.add_handler(CommandHandler("subscribe", subscribe_command))

    application.add_handler(CommandHandler("summarise", summarise_command))

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, do_command))

    '''
    application.job_queue.run_daily(callback=sub_summary_task,
                                    time=datetime.time(hour=11, minute=23, second=00))
    '''

    application.job_queue.run_repeating(callback=send_summary_to_subs, interval=1)

    # Run the bot until program exit
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    start_app()
