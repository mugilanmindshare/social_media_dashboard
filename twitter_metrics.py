import pandas as pd
import psycopg2
import sqlalchemy
from sqlalchemy import create_engine
from connection import conn
import streamlit as st
from sqlalchemy import text


@st.cache(allow_output_mutation=True)
def over_all_twitter_metrics():
    con=conn()
    mapping_query = "SELECT 'url','content','replycount','retweetCount','likecount','quotecount','username','year','month','hour','month_year','hashtag','mentions','tweets_no_stopwords','vader_sentiment','computed_date','computed_time' FROM twitter_leaders_user_level_finall_table"
    t = text(mapping_query)
    data = pd.read_sql_query(t, con)    
    return data




def year_wise_twitter_metrics(data):
    year_data=data.groupby(['year', 'username']).agg({'id':'count','likecount':'sum','replycount':'sum','retweetCount':'sum','quotecount':'sum'})
    year_data=year_data.reset_index()
    year_data=year_data.rename(columns={'id':'total_tweets','likecount':'total_likes','replycount':'total_replies','retweetCount':'total_retweets','quotecount':'total_quotes'})
    year_data=year_data.sort_values(by=['year'])
    return year_data
    


def month_year_wise_twitter_metrics(data):
    month_data=data.groupby(['month_year', 'username']).agg({'id':'count','likecount':'sum','replycount':'sum','retweetCount':'sum','quotecount':'sum'})
    month_data=month_data.reset_index()
    month_data=month_data.rename(columns={'id':'total_tweets','likecount':'total_likes','replycount':'total_replies','retweetCount':'total_retweets','quotecount':'total_quotes'})
    month_data=month_data.sort_values(by=['month_year'])
    return month_data

def week_wise_twitter_metrics(data):
    week_data=data.groupby(['week', 'username']).agg({'id':'count','likecount':'sum','replycount':'sum','retweetCount':'sum','quotecount':'sum'})
    week_data=week_data.reset_index()
    week_data=week_data.rename(columns={'id':'total_tweets','likecount':'total_likes','replycount':'total_replies','retweetCount':'total_retweets','quotecount':'total_quotes'})
    week_data=week_data.sort_values(by=['week'])
    return week_data




def day_wise_twitter_metrics(data):
    day_data=data.groupby(['computed_date', 'username']).agg({'id':'count','likecount':'sum','replycount':'sum','retweetCount':'sum','quotecount':'sum'})
    day_data=day_data.reset_index()
    day_data=day_data.rename(columns={'id':'total_tweets','likecount':'total_likes','replycount':'total_replies','retweetCount':'total_retweets','quotecount':'total_quotes'})
    day_data=day_data.sort_values(by=['computed_date'])
    return day_data
    

def hour_wise_twitter_metrics(data):
    hour_data=data.groupby(['hour', 'username']).agg({'id':'count','likecount':'sum','replycount':'sum','retweetCount':'sum','quotecount':'sum'})
    hour_data=hour_data.reset_index()
    hour_data=hour_data.rename(columns={'id':'total_tweets','likecount':'total_likes','replycount':'total_replies','retweetCount':'total_retweets','quotecount':'total_quotes'})
    hour_data=hour_data.sort_values(by=['hour'])
    return hour_data
    


