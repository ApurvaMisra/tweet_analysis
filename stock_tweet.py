import numpy as np 
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt
stocks=pd.read_csv("tesla_price.csv")
tweets=pd.read_csv("elon_sentiment.csv")
#Converting the respective columns to fdatetime datatype
stocks.date=pd.to_datetime(stocks.date)
tweets.date=pd.to_datetime(tweets.date)
#Grouping tweets by day
agg_df = tweets.groupby([tweets['date'].dt.date]).mean()
agg_df = agg_df.reset_index()
agg_df.set_index("date",inplace=True)
agg_df.index=pd.to_datetime(agg_df.index)
#Joining the two database based on the intersection between the datasets
df=stocks.join(agg_df,on="date",how='inner')
#Taking the difference between stock price from today with the previous day
df["diff"]=df.close.diff()
#The first row does no have a previous row to take difference with hence Nan and dropped 
df=df.iloc[1:]
#Scaling the difference
df['diff_norm']=df["diff"]/df["diff"].max()
#Choosing datapoints corresponding to only negative sentiments
neg_df=df[df.vader_score<0]
#Correlation coefficient
print(neg_df["diff_norm"].corr(neg_df['vader_score']))
df["close_norm"]=(df.close-df.close.min())/df.close.max()
print(df.head())
'''
ax=sns.lineplot(x="date",y="vader_score",data=df)
ax=sns.lineplot(x="date",y="close_norm",data=df)
plt.xticks(rotation=45)
plt.savefig("stockvssentiment.png")
plt.show()
'''


ax=sns.lineplot(x="date",y="vader_score",data=df)
ax=sns.lineplot(x="date",y="diff_norm",data=df)
plt.xticks(rotation=45)
plt.savefig("stockdropvssentiment.png")
plt.show()

print(df["diff_norm"].corr(df['vader_score_diff']))

neg_df=df[df.diff_norm<0]
print(neg_df["diff_norm"].corr(neg_dfdf['vader_score']))
ax1=sns.lineplot(x="date",y="vader_score",data=neg_df)
ax1=sns.lineplot(x="date",y="diff_norm",data=neg_df)
plt.xticks(rotation=45)
plt.savefig("negative_stockdropvssentiment.png")
plt.show()


#calculating pearson correlation for small windows
window_size=4
rolling_r = df['diff_norm'].rolling(window=window_size, center=True).corr(df['vader_score'])
ax=sns.lineplot(x=np.arange(len(rolling_r)),y=rolling_r)
plt.savefig("correlation.png")
plt.show()


