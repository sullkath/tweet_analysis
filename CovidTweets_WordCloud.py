# load libraries necessary to run wordcloud
# https://www.datacamp.com/community/tutorials/wordcloud-python
import matplotlib
import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import matplotlib.pyplot as plt
import seaborn as sns
import itertools
import collections


import re
import networkx


# #load in dataframe using pandas
# #the "data/" tells it to go to the current working directory to find the csv file, in this case,
# # C:\Users\sullkath\OneDrive\D2V Fellowship\COVID-19\COVID19docs_Project_Twitter\covid19docs
# #df stands for dataframe, which the pandas program will use to put the csv into a dataframe
# df = pd.read_csv("C:/Users/sullkath/OneDrive/D2V Fellowship/COVID-19/COVID19docs_Project_Twitter/covid19docs/output_got_TweetsJune2_sublime.csv", sep = ';')
# print(df.head(5))
# print(df[['text']])
#
# #start with one tweet; note, in df.text, 'text' refers to the variable name in the dataframe, but in 'text =', text
# #is the variable name. These would be different if the variable were called anything else, like 'tweet' or 'description'
# #as noted in the referenced tutorial website
#
# ##text = df.text[0]
#
# #create and generate a word cloud image
# ##wordcloud = WordCloud().generate(text)
#
# # lower max_font_size, change the maximum number of word and lighten the background:
# #wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(text)
# #plt.figure()
# #plt.imshow(wordcloud, interpolation="bilinear")
# #plt.axis("off")
# #plt.show()
#
# #display generated image
# ##plt.imshow(wordcloud, interpolation='bilinear')
# ##plt.axis("off")
# ##plt.show()
#
# # Save the image in the img folder:
# ##wordcloud.to_file("first_tweet.png")
#
# #look at all unique tweets and put them together in one word cloud
# all_tweets = "".join(str(tweet) for tweet in df.text)
# print ("There are {} words in the combination of all tweets.".format(len(all_tweets)))
#
# #create stopwords; aka words you don't want included, like 'the'
# stopwords = set(STOPWORDS) #can make this a function
# #To add stop words to this list:
# stopwords.update({"twin", "TWIN", "Twin", "and", "AND", "are", "ARE", "Are", "to", "uche", "oni", "https", "html", "com", "org",
#      "or", "wa", "twitter", "the", "is", "pic", "statu", "fbclid", "don", "news", "com/news/"})
#
# #generate a word cloud image with all of the combined tweets
# wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(all_tweets)
#
# #display generated image:
# #the matplotlib way:
# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis("off")
# plt.show()
#
# #save the image to file
# wordcloud.to_file("all_tweets1.png") #can be variable as output path in the overall function
# filepath, output_file, and stopwords are variables

# function
def WordCloudsTweets(filepath, stopwords, output_path):
    df = pd.read_csv(filepath, encoding='utf8', sep=',') #reads csv file given by the filename you give it using pandas, and gives this dataframe the name df
    #print(df.head(5))
    #print(df[['text']])

    tweets = df.Tweet_lemmatized.apply(str)
    #tweets = df.text.apply(str) #in dataframe, df, make values in the "text" variable strings
    tweets = [tweets.replace("'", '') for tweets in tweets] #gets rid of quotes around each word
    print(tweets[:5])

    all_tweets = "".join(str(tweet) for tweet in tweets)  #joins all of the tweets together into on long string; in 'df.text' text is the variable name
    #str(tweet) for tweet in
    ##print("There are {} words in the combination of all tweets.".format(len(all_tweets)))
    #all_tweets.split()
    print(all_tweets[:5])

    #replaces all urls in all_tweets with nothing
    #all_tweets_no_urls = "".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", all_tweets))
    #print(all_tweets_no_urls[:5])

    #make all words in first tweet lowercase
    ##all_tweets_no_urls[0].lower().split()

    #make all words in all tweets lowercase
    #creates a list of lists containing lowercase words for each tweet

    #words_in_tweets = [tweet.lower().split() for tweet in all_tweets_no_urls]
    #print(words_in_tweets[:1000])

    # generate a word cloud image with all of the combined tweets
    wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(all_tweets) #all_tweets_no_urls

    # display generated image:
    # the matplotlib way:
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()
    # save the image to file
    wordcloud.to_file(output_path)  # can be variable as output path in the overall function
    # filepath, output_file, and stopwords are variables


# this is where you're scripting
# this is telling python to actually do the following stuff
# makes more generalizable
if __name__ == '__main__':  # below are all the 'ingredients' you need; aka all of your variables.
    filepath = "C:/Users/sullkath/OneDrive/D2V Fellowship/COVID-19/COVID19docs_Project_Twitter/covid19docs/Lemmatized_only.csv"
    stopwords = set(STOPWORDS)  # can make this a function
    # To add stop words to this list:
    stopwords.update({"twin", "uche", "oni", "https", "html", "com", "org", "or", "wa", "twitter", "pic", "statu", "fbclid", "don", "com/news/",
         "the hospital", "theyre", "im"})
    output_path = "all_tweets1.png"
    WordCloudsTweets(filepath, stopwords, output_path)  # calls the function from above




# string.lower or string.upper will make everything lowercase; you can normalize each word to be the same word
# make everything more uniform
# look at All_Tweets
