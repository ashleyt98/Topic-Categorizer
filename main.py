import sys
from monkeylearn import MonkeyLearn
from collections import Counter
from itertools import chain

ans = input("Would you like to use:\n\t1.) Synopsis Classifier\n\t2.) Social Media Classifier\n")
#This allows you to choose which classifier you want to use

if ans == "1":
    print("Not implemented yet.")
elif ans == "2":
    option = input("Would you like to use:\n\t1.) Write your own tweet\n\t2.) Select a random tweet\n")
    
    if option == "1": 
        tweet = input(" Please write your tweet and when you're done press <Enter>.\n")
        
        ml = MonkeyLearn('dd20ef03405ebdd8301a985f30db2b2e0b570d92') #This allows you to use Monkey Learn
        data = [tweet] #This reads in the data that you want the classifier to look at
        model_id = 'cl_4keevyV9' #This allows you to specify what classifier you want to use
        result = ml.classifiers.classify(model_id, data) #This will put all the information in results
        
        counts = Counter(chain.from_iterable(i.keys() for i in result.body[0]['classifications'])) #This will count how many tags there are
        for key, value in counts.items():
            tag_name = value #This will assign the amount of tags used for the tweet to tag_name
            break
        
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Tweet:", result.body[0]['text']) #This will print the tweet
        
        for i in range(value): #This will print the tag associated with the tweet and how confident the classifier is that it's correct
            print("Tag:", result.body[0]['classifications'][i]['tag_name'], "\tConfidence:", result.body[0]['classifications'][i]['confidence'])        

    if option == "2":
        print("Not implemnted yet.")
else:
    print("The option you chose is not valid.")
