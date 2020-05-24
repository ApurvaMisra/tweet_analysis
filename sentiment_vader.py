import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
from nltk.tokenize.casual import casual_tokenize

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

df=pd.read_csv("elon.csv")
#drop any of the rows which had no text
df.dropna(subset=["text"],axis=0,inplace=True)
#create a new column for inserting the sentiment score
df["vader_score"]=""
analyzer=SentimentIntensityAnalyzer()
#Going over each sentence and finding the respective compound sentiment score 
for idx, sen in df['text'].iteritems():
    score=analyzer.polarity_scores(text=sen)
    df.loc[idx,"vader_score"]=score["compound"]

print(df.head())
df.to_csv("/home/apurva/Documents/code/reddit/elon_sentiment.csv", encoding = "utf-8",index = False)