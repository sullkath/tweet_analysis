# Python3 code to find frequency of each word
# function for calculating the frequency
#https://www.geeksforgeeks.org/find-frequency-of-each-word-in-a-string-in-python/
import pandas as pd
import re

def Ngrams_freq(filepath):
    df = pd.read_csv(filepath, encoding='utf8', sep=';')
    #print(df.head(5))
    #print(df[['text']])
    tweets = df.text.apply(str)
    tweets = [tweets.lower() for tweets in tweets]
    #tweets = ''.join(tweets).lower()
    #tweets = tweets.split()
    tweets = pd.Series(tweets)
    #tweets = [tweets.replace("'", '') for tweets in tweets]
    #print(tweets[:25])

    #tweets.to_csv(r'C:\Users\sullkath\OneDrive\D2V Fellowship\COVID-19\COVID19docs_Project_Twitter\covid19docs\tweetsJuly23.csv')

    #drops null value columns to avoid errors
    #tell it what to search for
    #create and pass to new column, -1 means not in string
    #tweets_ppe = tweets.str.find(substring)

    #to search for a phrase, change word in quotes after pat = "word/phrase"
    tweets_ppe = tweets.str.contains(pat = "racial inequality").sum()
    print(tweets_ppe)

    #if using below to output the csv, remove ".sum()" from above "tweets_ppe =" line
    #tweets_ppe.to_csv(r'C:\Users\sullkath\OneDrive\D2V Fellowship\COVID-19\COVID19docs_Project_Twitter\covid19docs\SpecificPhraseCounts\pers_prot_equip_count.csv')

# driver code
if __name__ == "__main__":
    filepath = "C:/Users/sullkath/OneDrive/D2V Fellowship/COVID-19/COVID19docs_Project_Twitter/covid19docs/output_got.txt"
    #str = 'PPE' #personal protective equipment”, “N95”, “face shield”, “telemedicine”, “telehealth”, “furlough”, “unemployed”, “pay cut”, “racial injustice”, “racial discrimination”, “racism”, “racial inequality”'
    Ngrams_freq(filepath)

