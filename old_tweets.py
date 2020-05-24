
import pandas as pd
import numpy as np 
import seaborn as sns 

import GetOldTweets3 as got
def get_tweets(username,  max_tweets): 
    # specifying tweet search criteria 
    tweetCriteria = got.manager.TweetCriteria().setUsername(username).setMaxTweets(max_tweets)
    # scraping tweets based on criteria
    tweet = got.manager.TweetManager.getTweets(tweetCriteria)
    # creating list of tweets with the tweet attributes 
    # specified in the list comprehension
    text_tweets = [[tw.id,tw.username,
                tw.text,
                tw.date,
                tw.retweets,
                tw.favorites,
                tw.mentions,
                tw.hashtags,tw.geo] for tw in tweet]
    # creating dataframe, assigning column names to list of
    # tweets corresponding to tweet attributes
    user_tweets = pd.DataFrame(text_tweets, 
                            columns = ['id','user', 'text','date','favorites', 'retweets', 'mentions', 'hashTags','geo'])
    
    return user_tweets
#Username of the user and max_tweets<1 so that all possible tweets are retrieved
df=get_tweets("@elonmusk", 0) 

print(df.head())
print(len(df))
df.to_csv("/home/apurva/Documents/code/reddit/elon.csv", encoding = "utf-8",index = False)

def get_search(query,max_tweets,since):
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch(query).setSince(since).setMaxTweets(max_tweets)
#"2015-05-30"
    tweet = got.manager.TweetManager.getTweets(tweetCriteria)
#max_tweets<1, all possible tweets will be generated
    text_tweets = [[tw.id,tw.username,
                tw.text,
                tw.date,
                tw.retweets,
                tw.favorites,
                tw.mentions,
                tw.hashtags,tw.geo] for tw in tweet]   
    #print(text_tweets) 
    query_tweets = pd.DataFrame(text_tweets, 
                            columns = ["id",'user', 'text','date', 'favorites', 'retweets', 'mentions', 'hashTags','geo'])
    
    return query_tweets



'''
dates_list=[ "2019/12/01", "2020/01/01", "2020/02/01", "2020/03/01", "2020/04/01", "2020/05/01"]
counter=0
for dat in dates_list:
    if(counter>0):
        df_old=df.copy()
        df=get_search("covid-19", 0, dat)
        print("df_old",len(df_old))
        print("df",len(df))
        df = df_old.merge(df, on=list(df_old), how='outer')
        df.drop_duplicates(subset=['id'], inplace=True, keep='last')
        print("joined",len(df))
    else:
        df=get_search("covid-19", 0, dat)
    counter+=1

print(df.head())
print(len(df))
df.to_csv("/home/apurva/Documents/code/reddit/covid_dec.csv", encoding = "utf-8",index = False)
'''


