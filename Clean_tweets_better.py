import numpy as np
import sys
import nltk
import re
import csv
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pandas as pd

data = pd.read_csv('Raw_Data/output_got.txt', encoding='utf8',
                   sep=';', lineterminator='\n', keep_default_na=False)  # , lineterminator='\n', low_memory=False, quoting=csv.QUOTE_NONE , usecols = [5,9], names=list['text','id'], dtype=str)

data["id"] = data["id"].astype(str)
data["text"] = data["text"].astype(str)


# Preprocessing
def remove_string_special_characters(s):
    stripped = str(s)
    # removes special characters with ' '
    stripped = re.sub('[^a-zA-z\s]', '', str(s))
    stripped = re.sub('_', '', stripped)

    # Change any white space to one space
    stripped = re.sub('\s+', ' ', stripped)

    # Remove urls
    stripped = re.sub(r"http\S+", '', stripped)

    # Remove start and end white spaces
    stripped = stripped.strip()
    if stripped != '':
        return stripped.lower()


data["text"] = data["text"].apply(remove_string_special_characters)
data['text'].dropna(inplace=True)

# Stopword removal
stop_words = set(stopwords.words('english'))
spanishSW = set(stopwords.words('spanish'))
stop_words.update(spanishSW)

#outputs csv file of ngrams called your original file name + -ngrams.csv
data.to_csv(r'C:\Users\sullkath\OneDrive\D2V Fellowship\COVID-19\COVID19docs_Project_Twitter\covid19docs\Raw_Data\output_got-cleaned.csv', encoding='utf-8-sig', index=False, header=True)