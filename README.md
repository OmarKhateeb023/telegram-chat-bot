![image](https://github.com/OmarKhateeb023/telegram-chat-bot/assets/142600750/455ba144-1389-4764-9a2e-fd15a781c8ab)# My Project
## weekly report

## until 4/3 
These two weeks were research focused. Seeing how generative AI is becoming a hot subject in the market I want to try doing something simillair to this area.
I tried to mainly focus on the area of text summariztion.


I started my journey by learning about the dominant solutions on the market today. Given that Python was leading the way with innovative libraries, I saw an opportunity to learn Python in the process. 

During this exploration, I came across the "transformers" library by Hugging Face—an entity specializing in natural language processing (NLP) research and applications. This library provides user-friendly interfaces and pre-trained models tailored for a broad spectrum of NLP tasks.

The functionalities included in the library's offerings were Language Translation, Text Generation, Summarization, Analysis, and many more. I focused on the aspect of text summarization. 
As I explored the library's capitalites, I discovered two different approaches for text summarization:

1) Extractive Summarization: This approach involves selecting the most important sentences or phrases from the original text and presenting them in a condensed form. ( mostly implemented by testrank and tensorflow)
2) Abstractive Summarization: This approach involves generating new sentences that capture the most important information from the original text.

I started a small Python project to evaluate the library's potential. I started by summarizing online news articles and short texts, and I found that the two methods produced different results.
Interestingly, the Abstractive method stood out because it produced content with a structure that was noticeably more natural and readable by humans.

I had doubts about how sufficient the results were despite how impressive they were. It is obvious that looking into alternative strategies is essential.

**Total Time** ~20 hours


## 1/4 
I started my joureny again searching for a better solution for my text summriztion challange. While searching online, I came across a repository that specialized in summarizing news articles (https://github.com/SKRohit/Generating_Text_Summary_With_GPT2) and it looked very promising.

I cloned the repository locally and began exploring its contents. It was difficult to navigate and study the code, so I began learning a little bit about the key terms I found on the documentation in an effort to grasp the big picture.  
After trying to learn about NLP for a while and reading about various topics like Sequence-to-Sequence and other things. I eventually made the decision to test the algorithm.

I started receiving some error messages because the instructions for running the code were not very clear. I begin modifying the code in an attempt to make it function.
The code in the repository should be working without any changes, so after spending countless hours debugging, I made the decision to stop and reconsider the changes I had made.  
Since it seemed related, I made the decision to put more effort into understanding how Python's environment functions and versioning works.

**Total Time** ~12 hours ( soon to realise they led no where :) )

## 8/4
Last week I decided that I need to better understand the python language.  I began reading blogs online and enrolling in courses on websites like YouTube.
After spending hours learning, I was able to explain the logic behind the broken code. I learned that Python is not backward compatible, nor are its libraries.

I re-cloned the repositoray again in an effort to make it work this time. Created a python virtual enviorment as suggested by the language best practies. I started by downloading the correct version of the modules on the requirment files, only to find the most of them were depericated.
after the huge effort of finding the missing moudles online I had no luck :( 

I decided to keep searching for other solutions.

**Total Time** ~16 hours

## 25/4
In the previous week, I made the decision to continue my search for alternative text summarization solutions. However, upon reevaluating the progress I had made, I opted to stick with the available solutions, despite acknowledging their shortcomings.  
while examining my project, I came to the conclusion that, even after it was finished, interacting with it was still difficult; the idea of having to run a Python script to produce a summary discouraged user interaction.
I relized that it needs to be integrated with other easy to interact with social media platforms.

I began exploring my options,  with a particular focus on WhatsApp and Telegram. Following online research, Telegram emerged as the more viable choice.  
The implementation process appeared smoother and more straightforward compared to WhatsApp, which not only required a business account but also cost money.

**Total Time** ~10 hours

## 3/6 
I got started by creating a fresh Python project and getting ready to code. I read the docuemtnion on the telegram-bot and watched some tutorials online.
Again I am stuck with two options, the library does offer two ways to communicate with my program. so I either:

1) webhool: requests are made by a server; automatically triggered when an event occurs.
2) polling: requests are made by a client; set up to run at fixed intervals and runs whether there is a new event or not

Eventhough the webhook is better here I choose to go with the polling mechanism since it is easier to implement and sufficient enough for my project.  
After some time of writing code I hear the sound of a notifcation back on my phone! The bot said it first words replying "hi" back to me.

Interstingly, I heard it about python but got to witnes it this time, the code is very short but its filled with a lot of concepts and does a lot!  
I finished my work for this week with a plan in my mind to further improve the bot next week to reply back with the summary of the text I send him.

**Total Time** ~30 hours

## 15/6
Last week I had a plan of further improving the bot this week by making it reply with a meaningful summary of the message it receive. But upon re-thinking the strategy during the week I came up with an idea the makes the proeject more interesting.  
I decided that instead of receiving a free text and summrizing it back (which can be done online with quick google search), the bot could become a news summarizer, by reciving a link to a news article it could fetch it content and send the news back summrized to the user.

I began exploring what different news compaines had to offer. Logically I started with the big ones, as I have a better chance of finding something helpful.  
I came accross the NY times API, I started reading their documentation to find a few intersting API's that offered their articles with different search quries like timestamps, tags (sport,finance..) and other cool stuff.

Jumping back to code I created an account for NY times and recieved a authentication token to interact with the API, then I started implementing the additional feature of fetching the article only to sadly realize the API's only includes the metadata of the articles and not the content itself.  
Meaning that I could only get the article title,tags,time, author and other metadata but would not get the news itself.

Searching again on there website I found an email for their API customer support. I tried to take a shot by contacting them explaining my project and asking for access to a few articles content.


**Total Time** ~16 hours


## 24/6
Last week I sent an email to NY times requesting access to their articles, after a few messages back and forth during the week my request was declined and I had to find other way to fetch the data.
I realized that compaines does offer such and API for free so I started searching online till I stumbled upon a thread explaining a way to fetch a data from and html website using the simple way of taking the text between the '/p' Paragraph element.

The approach was not perfect but I thought it was good enough for my project so I jumped to the code to implement it. It was easy to do it in python and did not take a lot of time.
While testing it I realized that it didn't work for all websites for example it didn't work NY times. After some investigation I understood that it is related to blocking the ad-blocker on the website so they block fetching the HTML page.
 
I can see some progress now, the bot now returns the actual news articles of the link it receive.

Next step would be to summrize this content.


**Total Time** ~8 hours

## 2/7
There was an amazing news this week, OpenAI is offering a new API to interact with it's model. It was exactly what my project was missing, a good text summarization algorithm.  

Once again I am reading the doecmention online, this time OpenAI documentation for the GPT 3.5 summrization model, It seemed easy to implement and since it is so popular I even found the implemention online and needed just to modify it a little bit.  
Then I had to create an account with a free trial to recieve a token so I can trigger their API.

Great! I once again see a huge progress, now my bot receives a link to a news article and replies back with it summary


**Total Time** ~12 hours
## 15/7

This week I am thinking of addiontal feature that I want to invest on. I came thought of two that would improve the user experience:
1) Upong searching online for an API to fetch the news articles, I came across an interesting API offering of MediaStack that allows querying different news compaines with a rich query parameters set like:
  A) popularity: returns the URL of the most populart news.
  B) Tags: returns news with the specificed tags on the request. tags could be the category I specify like: music, sport, finance...
2) Since I need my program to run all the time for the bot to work, running the program on the cloud seems like a big improvment.

To further advance the first idea into a useful feature I decided to allow subscribing to my bot, meaning that users now can subscribe for news summary in a ceratin time of the day they pick.
I jumped to implemention of the new feature, since I am now familair with creating API calls in python from my previous work with the NY times. I was able to smoothly Implement the new feature.

The MediaStack API does still offer more stuff that I can use to further improve my bot. for example I could use the tags search to let the user which category to subsribe to.

**Total Time** ~16 hours
## 18/8

This Week I wil be focusing in deploying my code to the could. I start by reading about differnt cloud offerings, soon to relize that all the offerings were good enough for my needs.  

I needed to create a VM and then deploy and run my code in, which is a basic service that all clould services offered. I decided to go with Azure since we get a free studen credit.

After reading online and watching some tutorials I was able to create the VM resource and connect to it using the SSH protocol. Now all I had to do is deploy my code and set up the environment for my program to work.
I succeded in doing that and finally my bot can run all the time.


**Total Time** ~16 hours

