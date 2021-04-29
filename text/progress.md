# 27.04.2021

Hi, today I decided start project dedicated person feature extraction based on social group in which person belongs.

During the work on the project I want to achieve the following goals:

1. Check out available solutions.
2. Develop a method for extracting information from a social network.
3. Develop data processing method.
4. Create user-friendly frontend interface. 
5. Put everything in docker so it's easy to deploy

Also I want examine new interesting libraries and approaches for graph analysis, processing and visualization. 

# 28.04.2021

So, today second day of my work on this project. I should have read more articles, but I just read some from top of google result. But since I need do some tasks today, I start do 2nd part of plan.

And I find some asynchronous library called **aiovk** - I think it can be better solution because it still some update and do all non-linear. 

# 29.04.2021

We got an idea to do all the API communication on the frontend side. 
We understand at least one limitation:
1. we cannot use our own tokens (e.g. to make many concurrent requests with different token)
So, possiblity of pure frontend-based implementation depends on the future alogirthm.


Features:
- Analyze friends info
- Analyze person contact info
- Analyze person subsriptions
- Looking for cached versions of pages



Ideas regarding architecture:
1. Business logic is on frontend. Not scalable: e.g. not possible to create another front-end like telegram bot
2. Business logic is on backend. Cache parsing service, vk API services are devided. 

We gonna select features:
- e.g. age, city, school which can be detected very precisely
- Clusterization based on mutual friends

Result:

1. Predict unfilled fields, detect false/incorrect information in fields.
2. Graph based data visualisation


We will start with:
 - City
 - Age
 - Gender
 - Work, University, School
 - Real profile?
 
 
 // todo
 
 Real profile identification.
 Criteria of a fake profile (friends count? pictures? wall posts?).
 analyze gifts.
 find mutual likes to detect real friends.
 How we can analyze data in functional way (F#?)
