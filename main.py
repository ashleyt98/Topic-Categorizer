from monkeylearn import MonkeyLearn
from collections import Counter
from itertools import chain
from random import randrange
import sys
import tweepy

consumer_key = "xSA6hRSv03jI0AegAB0210s2u"
consumer_secret = "59n2PG84kEedk8WBJ1s5OleTiRHWeG6V6VUw973Al47X0BEuFQ"
access_key = "3224628037-HO7a4r1CDsBlR1SJt3I5JpV1ysm2tXfq0CmQMMn"
access_secret = "6jnq4sye3lS03MYsNgSeillQ6KYXMNWnFlI6PjzJh5J6e"

def get_tweets(username): #This will extract the tweets
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)    
    auth.set_access_token(access_key, access_secret) 
    
    api = tweepy.API(auth) 
    number_of_tweets = 1
    
    tweets = api.user_timeline(screen_name=username) 
    
    temp = []
    
    tweets_for_csv = [tweet.text for tweet in tweets]
    for j in tweets_for_csv: 
        temp.append(j)
        
    amt = len(temp) #This will get the total number of tweets retrieved
    rand_num = randrange(amt - 1) #This will randomly select a tweet from the list
    post = temp[rand_num]
    
    ml = MonkeyLearn('dd20ef03405ebdd8301a985f30db2b2e0b570d92')
    data = [post]
    model_id = 'cl_4keevyV9'
    result = ml.classifiers.classify(model_id, data)
    
    counts = Counter(chain.from_iterable(i.keys() for i in result.body[0]['classifications']))
        
    if len(result.body[0]['classifications']) == 0: #If the tweet doesn't belong in any categories the system will exit
        print(post)
        sys.exit("The tweet did not match any exisiting topics")
    
    for key, value in counts.items():
        tag_name = value
        break
    
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Tweet:", result.body[0]['text'])
    for i in range(value):
        print("Tag:", result.body[0]['classifications'][i]['tag_name'], "\tConfidence:", result.body[0]['classifications'][i]['confidence'])
    
    
ans = input("Would you like to use:\n\t1.) Synopsis Classifier\n\t2.) Social Media Classifier\n")

if ans == "1":
    print("Hasn't been implemented.")
    
elif ans == "2":
    option = input("Would you like to use:\n\t1.) Write your own tweet\n\t2.) Select a random tweet\n")
    
    if option == "1":
        tweet = input(" Please write your tweet and when you're done press <Enter>.\n")
        ml = MonkeyLearn('dd20ef03405ebdd8301a985f30db2b2e0b570d92')
        data = [tweet]
        model_id = 'cl_4keevyV9'
        result = ml.classifiers.classify(model_id, data)
        
        counts = Counter(chain.from_iterable(i.keys() for i in result.body[0]['classifications']))
        
        if len(result.body[0]['classifications']) == 0: #If the tweet doesn't belong in any categories the system will exit
            sys.exit("The tweet did not match any exisiting topics")
        
        for key, value in counts.items():
            tag_name = value
            break
        
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Tweet:", result.body[0]['text'])
        for i in range(value):
            print("Tag:", result.body[0]['classifications'][i]['tag_name'], "\tConfidence:", result.body[0]['classifications'][i]['confidence'])        

    if option == "2":
        get_tweets("@nowthisnews") #This will get the most recent tweets from "NowThisNews" timeline
else:
    print("The option you chose is not valid.")
