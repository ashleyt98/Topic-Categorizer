from monkeylearn import MonkeyLearn
from collections import Counter
from itertools import chain
from random import randrange
import sys
import tweepy

"""
References:
MonkeyLearn API for classifiers: https://monkeylearn.com/api/v3/#classifier-api
Extracting tweets from twitter: https://www.geeksforgeeks.org/extraction-of-tweets-using-tweepy/
"""

consumer_key = "xSA6hRSv03jI0AegAB0210s2u"
consumer_secret = "59n2PG84kEedk8WBJ1s5OleTiRHWeG6V6VUw973Al47X0BEuFQ"
access_key = "3224628037-HO7a4r1CDsBlR1SJt3I5JpV1ysm2tXfq0CmQMMn"
access_secret = "6jnq4sye3lS03MYsNgSeillQ6KYXMNWnFlI6PjzJh5J6e"

def get_tweets(username): #This will extract the tweets
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)  #This gets me the authorization from twitter developer page  
    auth.set_access_token(access_key, access_secret) 
    
    api = tweepy.API(auth) #This calls on the Twitter API
    number_of_tweets = 1
    
    tweets = api.user_timeline(screen_name=username) 
    
    temp = []
    
    tweets_for_csv = [tweet.text for tweet in tweets] #This section gets about 20 of the most recent posts from the specified account
    for j in tweets_for_csv: 
        temp.append(j)
        
    amt = len(temp) #This will get the total number of tweets retrieved
    rand_num = randrange(amt - 1) #This will randomly select a tweet from the list
    post = temp[rand_num]
    
    ml = MonkeyLearn('dd20ef03405ebdd8301a985f30db2b2e0b570d92')
    data = [post]
    model_id = 'cl_4keevyV9'
    result = ml.classifiers.classify(model_id, data)
    
    counts = Counter(chain.from_iterable(i.keys() for i in result.body[0]['classifications'])) #This counts how many topics the tweet fits in
        
    if len(result.body[0]['classifications']) == 0: #If the tweet doesn't belong in any categories the system will exit
        print(post)
        sys.exit("The tweet did not match any exisiting topics")
    
    for key, value in counts.items():
        tag_name = value
        break
    
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Tweet:", result.body[0]['text'])
    for i in range(value): #This prints the tweet classification and its confidence score
        print("Tag:", result.body[0]['classifications'][i]['tag_name'], "\tConfidence:", result.body[0]['classifications'][i]['confidence'])
    
    
ans = input("Would you like to use:\n\t1.) Synopsis Classifier\n\t2.) Social Media Classifier\n")

if ans == "1":
    print("Hasn't been implemented.")
    """
    movie = input("Type in a movie title or synopsis and press <Enter> when done\n")
    ml = MonkeyLearn('79a6b0d3ca225f4372bb7456b033ab3c807b2587')
    data = [movie]
    model_id = 'cl_tvhZLUjZ'
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
    """
elif ans == "2":
    option = input("Would you like to use:\n\t1.) Write your own post\n\t2.) Select a random tweet\n")
    
    if option == "1":
        tweet = input(" Please write your post and when you're done press <Enter>.\n")
        
        ml = MonkeyLearn('dd20ef03405ebdd8301a985f30db2b2e0b570d92') #This calls on the MonkeyLearn Topic Classifier tool 
        data = [tweet] #This will send the post written by the user to be analyzed
        model_id = 'cl_4keevyV9' #This will call on the classifier that I created for this portion
        result = ml.classifiers.classify(model_id, data) #This will give the results back
        
        #This will count the number of classifications that the post has so that they can all be printed
        counts = Counter(chain.from_iterable(i.keys() for i in result.body[0]['classifications']))
        
        if len(result.body[0]['classifications']) == 0: #If the tweet doesn't belong in any categories the system will exit
            sys.exit("The tweet did not match any exisiting topics")
        
        for key, value in counts.items():
            tag_name = value
            break
        
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Post:", result.body[0]['text']) #Prints out the user's post
        for i in range(value): #This will show what topics the post has been classified as and how confident the machine learning is about them
            print("Tag:", result.body[0]['classifications'][i]['tag_name'], "\tConfidence:", result.body[0]['classifications'][i]['confidence'])        

    if option == "2":
        get_tweets("@nowthisnews") #This will get the most recent tweets from "NowThisNews" timeline
else:
    print("The option you chose is not valid.")
