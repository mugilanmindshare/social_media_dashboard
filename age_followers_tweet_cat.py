import pandas as pd
import psycopg2
import sqlalchemy
from sqlalchemy import create_engine
from connection import conn
import streamlit as st
from sqlalchemy import text
from matplotlib.axis import XAxis
from matplotlib.pyplot import title
import pandas as pd
import psycopg2
from pyparsing import White
import sqlalchemy
from sqlalchemy import create_engine
from connection import *
from twitter_metrics import *
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.io as pio
pio.templates 

def follower_age_category(data):
    import datetime as dt
    data["max_rank"] = data.groupby("username")["computed_date"].rank("dense",ascending=False)
    d_df=data[data['max_rank']==1.0]
    d_df = d_df.drop_duplicates(subset=['username'])

    d_df['created']=pd.to_datetime(d_df['created'])


    d_df['created_date'] = d_df['created'].dt.date

    d_df['diff_days'] = (d_df['computed_date'] - d_df['created_date']).dt.days


    d_df['age_category']='category'
    for i in range(len(d_df)):
        if d_df['diff_days'].iloc[i] > 1460:
            d_df['age_category'].iloc[i] = '>4 years'
        elif d_df['diff_days'].iloc[i] >= 1096 and d_df['diff_days'].iloc[i] <= 1460:
            d_df['age_category'].iloc[i] = '3 - 4 years'
        elif d_df['diff_days'].iloc[i] >= 731 and d_df['diff_days'].iloc[i] <= 1095:
            d_df['age_category'].iloc[i] = '2 - 3 years'
        elif d_df['diff_days'].iloc[i] >= 366 and d_df['diff_days'].iloc[i] <= 730:
            d_df['age_category'].iloc[i] = '1 - 2 years'
        elif d_df['diff_days'].iloc[i] >= 182 and d_df['diff_days'].iloc[i] <= 365:
            d_df['age_category'].iloc[i] = '6 - 12 months'
        elif d_df['diff_days'].iloc[i] >= 32 and d_df['diff_days'].iloc[i] <= 61:
            d_df['age_category'].iloc[i] = '1 - 6 months'
        elif d_df['diff_days'].iloc[i] >= 11 and d_df['diff_days'].iloc[i] <= 31:
            d_df['age_category'].iloc[i] = '11 - 30 days'        
        else:
            d_df['age_category'].iloc[i] = '<10 days'





    d_df['followers_category']='category'
    for i in range(len(d_df)):
        if d_df['followerscount'].iloc[i] > 10000:
            d_df['followers_category'].iloc[i] = '> 10000'
        elif d_df['followerscount'].iloc[i] >= 5001 and d_df['followerscount'].iloc[i] <= 10000:
            d_df['followers_category'].iloc[i] = '5001-10000'
        elif d_df['followerscount'].iloc[i] >= 1001 and d_df['followerscount'].iloc[i] <= 5000:
            d_df['followers_category'].iloc[i] = '1001-5000'
        elif d_df['followerscount'].iloc[i] >= 501 and d_df['followerscount'].iloc[i] <= 1000:
            d_df['followers_category'].iloc[i] = '501-1000'
        elif d_df['followerscount'].iloc[i] >= 101 and d_df['followerscount'].iloc[i] <= 500:
            d_df['followers_category'].iloc[i] = '101-500'    
        elif d_df['followerscount'].iloc[i] >= 51 and d_df['followerscount'].iloc[i] <= 100:
            d_df['followers_category'].iloc[i] = '51-100' 
        elif d_df['followerscount'].iloc[i] >= 41 and d_df['followerscount'].iloc[i] <= 50:
            d_df['followers_category'].iloc[i] = '41-50'                         
        elif d_df['followerscount'].iloc[i] >= 31 and d_df['followerscount'].iloc[i] <= 40:
            d_df['followers_category'].iloc[i] = '31-40'    
        elif d_df['followerscount'].iloc[i] >= 21 and d_df['followerscount'].iloc[i] <= 30:
            d_df['followers_category'].iloc[i] = '21-30'    
        elif d_df['followerscount'].iloc[i] >= 10 and d_df['followerscount'].iloc[i] <= 20:
            d_df['followers_category'].iloc[i] = '10-20'                                           

        else:
            d_df['followers_category'].iloc[i] = '<10'            

    age_category_data = d_df.groupby('age_category').agg({'id':'count'})
    age_category_data = age_category_data.reset_index()
    age_category_data = age_category_data.rename(columns={'id':'Number of Users'})
    age_category_data = age_category_data.sort_values(by=['age_category'])
    


    follower_category_data = d_df.groupby('followers_category').agg({'id':'count'})
    follower_category_data = follower_category_data.reset_index()
    follower_category_data = follower_category_data.rename(columns={'id':'Number of Users'})
    followers_category_data = follower_category_data.sort_values(by=['followers_category'])
    return age_category_data, follower_category_data       








def tweet_category(data):
    tweet_cat = data.groupby('username').agg({'id':'count'})
    tweet_cat = tweet_cat.reset_index()

    tweet_cat['tweet_category']='category'
    for i in range(len(tweet_cat)):
        if tweet_cat['id'].iloc[i] > 10:
            tweet_cat['tweet_category'].iloc[i] = '>10 Tweets'
        elif tweet_cat['id'].iloc[i] > 5 and tweet_cat['id'].iloc[i] <= 10:
            tweet_cat['tweet_category'].iloc[i] = '6-10 Tweets'
        elif tweet_cat['id'].iloc[i] >= 3 and tweet_cat['id'].iloc[i] <= 5:
            tweet_cat['tweet_category'].iloc[i] = '3-5 Tweets'
        elif tweet_cat['id'].iloc[i] == 2:
            tweet_cat['tweet_category'].iloc[i] = '2 Tweets'
        else:
            tweet_cat['tweet_category'].iloc[i] = '1 Tweet'
    tweet_category = tweet_cat.groupby('tweet_category').agg({'id':'count'})
    tweet_category = tweet_category.reset_index()

    tweet_category = tweet_category.rename(columns={'id':'Number of Users'})
    tweet_category = tweet_category.sort_values(by=['tweet_category'])
    return tweet_category   



def age_category_plot(data):
        fig = px.bar(data, x = data['age_category'], y = data['Number of Users'], text_auto='.2s',title='Age category Frequency')
        fig.update_layout(xaxis={'categoryorder':'array', 'categoryarray':['<10 days','11 - 30 days','1 - 6 months','6 - 12 months','1 - 2 years','2 - 3 years','3 - 4 years','>4 years']})
        st.plotly_chart(fig,use_container_width = True)    



def followers_category_plot(data):
        fig = px.bar(data, x = data['followers_category'], y = data['Number of Users'], text_auto='.2s',title='Users by Followers range')
        fig.update_layout(xaxis={'categoryorder':'array', 'categoryarray':['<10','10-20','21-30','31-40','41-50','51-100','101-500','501-1000','1001-5000','5001-10000','> 10000']})
        st.plotly_chart(fig,use_container_width = True)           

def tweet_category_plot(data):
        fig = px.bar(data, x = data['tweet_category'], y = data['Number of Users'], text_auto='.2s',title='Tweets Frequency')
        st.plotly_chart(fig,use_container_width = True)         