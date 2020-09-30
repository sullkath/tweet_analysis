from collections import OrderedDict, defaultdict, Counter
import pandas as pd
import csv
from nltk.tokenize import TweetTokenizer
from sklearn.feature_extraction.text import CountVectorizer
#runs NRC sentiment analysis
#https://github.com/pmbaumgartner/text-feat-lib/blob/master/notebooks/NRC%20Emotion%20Lexicon%20Features.ipynb
df = pd.read_csv('Raw_Data/lemmatized_only1.csv', sep=',', encoding='utf8')
print(df.head(10))

tweets = df.Tweet_lemmatized.apply(str)
tweets = [tweets.replace("'", '') for tweets in tweets] #gets rid of quotes around each word
print(tweets[:5])

#tweets = "".join(str(tweet) for tweet in tweets)

wordList = defaultdict(list)
emotionList = defaultdict(list)
with open(r'NRC-Sentiment-Emotion-Lexicons/NRC-Emotion-Lexicon-v0.92/NRC-Emotion-Lexicon-Wordlevel-v0.92.txt') as f:
    reader = csv.reader(f, delimiter='\t')
    headerRows = [i for i in range(0, 46)]
    for row in headerRows:
        next(reader)
    for word, emotion, present in reader:
        if int(present) == 1:
            #print(word)
            wordList[word].append(emotion)
            emotionList[emotion].append(word)

tt = TweetTokenizer()

def generate_emotion_count(string, tokenizer):
    emoCount = Counter()
    for token in tt.tokenize(string):
        token = token.lower()
        emoCount += Counter(wordList[token])
    return emoCount

emotionCounts = [generate_emotion_count(tweet, tt) for tweet in tweets]

emotion_df = pd.DataFrame(emotionCounts)
emotion_df = emotion_df.fillna(0)

emotion_df.to_csv(r'C:\Users\sullkath\OneDrive\D2V Fellowship\COVID-19\COVID19docs_Project_Twitter\covid19docs\NRC_emotion_Analysis1.csv', index=False)

print(emotion_df.head(15))



