import pandas as pd
import psycopg2
import sqlalchemy
from sqlalchemy import create_engine
from connection import conn
import streamlit as st
from sqlalchemy import text





@st.cache(allow_output_mutation=True)
def get_username_for_search():
    con=conn()
    mapping_query = "SELECT distinct mentioned_user FROM twitter_leaders_mentions_view"
    t = text(mapping_query)
    data = pd.read_sql_query(t, con)
    data_list = data['mentioned_user'].tolist()
    return data_list



@st.cache(allow_output_mutation=True)
def over_all_twitter_mentions_data(username,fromm, to):
    data=pd.DataFrame(columns=['id', 'replycount', 'retweetcount', 'likecount','quotecount', 'lang', 'place', 'username','verified', 'created', 'followerscount','location', 'date','time', 'year', 'month', 'hour', 'month_year','hashtag', 'mentions', 'tweets_no_stopwords','textblob_sentiment','vader_sentiment', 'mentioned_user', 'computed_datetime','computed_date', 'computed_time'])
    table_list={'ncbn':'leaders_mention1','naralokesh':'leaders_mention2','ysjagan':'leaders_mention3','PawanKalyan':'leaders_mention4','TelanganaCMO':'leaders_mention5','KTRTRS':'leaders_mention6','bandisanjay_bjp':'leaders_mention7','TigerRajaSingh':'leaders_mention8','imAkbarOwaisi':'leaders_mention9','asadowaisi':'leaders_mention10','revanth_anumula':'leaders_mention11','Arvindharmapuri':'leaders_mention12','BSBommai':'leaders_mention13','BSYBJP':'leaders_mention14','siddaramaiah':'leaders_mention15','DKShivakumar':'leaders_mention16','hd_kumaraswamy':'leaders_mention17','H_D_Devegowda':'leaders_mention18','narendramodi':'leaders_mention19','rahulgandhi':'leaders_mention20','ArvindKejriwal':'leaders_mention21','MamataOfficial':'leaders_mention22','PawarSpeaks':'leaders_mention23','ComradeDRaja':'leaders_mention24','SitaramYechury':'leaders_mention25','Mayawati':'leaders_mention26','yadavtejashwi':'leaders_mention27','SangmaConrad':'leaders_mention28','priyankagandhi':'leaders_mention29','ShashiTharoor':'leaders_mention30','AmitShah':'leaders_mention31','msisodia':'leaders_mention32','myogiadityanath':'leaders_mention33'}
    for i in username:
        con=conn()
        user=table_list[i]
        selected_users_query = '''select id, replycount, retweetcount, likecount,quotecount, lang, place, username,verified, created, followerscount,location, date,time, year, month, hour, month_year,hashtag, mentions, tweets_no_stopwords,textblob_sentiment,vader_sentiment, mentioned_user, computed_datetime,computed_date, computed_time from '''+user+''' where computed_date >= :fromm and computed_date <= :to'''
        params = {'fromm': fromm, 'to':to }
        t = text(selected_users_query)
        selected_users_info = pd.read_sql(t, con, params=params)
        data=data.append(selected_users_info)
    return data





def year_wise_twitter_mention_metrics(data):
    year_data=data.groupby(['year', 'mentioned_user']).agg({'id':'count','likecount':'sum','replycount':'sum','retweetcount':'sum','quotecount':'sum'})
    year_data=year_data.reset_index()
    year_data=year_data.rename(columns={'id':'total_tweets','likecount':'total_likes','replycount':'total_replies','retweetcount':'total_retweets','quotecount':'total_quotes'})
    year_data=year_data.sort_values(by=['year'])
    return year_data
    


def month_year_wise_twitter_mention_metrics(data):
    month_data=data.groupby(['month_year', 'mentioned_user']).agg({'id':'count','likecount':'sum','replycount':'sum','retweetcount':'sum','quotecount':'sum'})
    month_data=month_data.reset_index()
    month_data=month_data.rename(columns={'id':'total_tweets','likecount':'total_likes','replycount':'total_replies','retweetcount':'total_retweets','quotecount':'total_quotes'})
    month_data=month_data.sort_values(by=['month_year'])
    return month_data

def week_wise_twitter_mention_metrics(data):
    week_data=data.groupby(['week', 'mentioned_user']).agg({'id':'count','likecount':'sum','replycount':'sum','retweetcount':'sum','quotecount':'sum'})
    week_data=week_data.reset_index()
    week_data=week_data.rename(columns={'id':'total_tweets','likecount':'total_likes','replycount':'total_replies','retweetcount':'total_retweets','quotecount':'total_quotes'})
    week_data=week_data.sort_values(by=['week'])
    return week_data




def day_wise_twitter_mention_metrics(data):
    day_data=data.groupby(['computed_date', 'mentioned_user']).agg({'id':'count','likecount':'sum','replycount':'sum','retweetcount':'sum','quotecount':'sum'})
    day_data=day_data.reset_index()
    day_data=day_data.rename(columns={'id':'total_tweets','likecount':'total_likes','replycount':'total_replies','retweetcount':'total_retweets','quotecount':'total_quotes'})
    day_data=day_data.sort_values(by=['computed_date'])
    return day_data
    

def hour_wise_twitter_mention_metrics(data):
    hour_data=data.groupby(['hour', 'mentioned_user']).agg({'id':'count','likecount':'sum','replycount':'sum','retweetcount':'sum','quotecount':'sum'})
    hour_data=hour_data.reset_index()
    hour_data=hour_data.rename(columns={'id':'total_tweets','likecount':'total_likes','replycount':'total_replies','retweetcount':'total_retweets','quotecount':'total_quotes'})
    hour_data=hour_data.sort_values(by=['hour'])
    return hour_data
    











def year_wise_twitter_mention_mentions(data):
    year_data=data.groupby(['year', 'mentioned_user']).agg({'id':'count','likecount':'sum','replycount':'sum','retweetcount':'sum','quotecount':'sum'})
    year_data=year_data.reset_index()
    year_data=year_data.rename(columns={'id':'total_tweets','likecount':'total_likes','replycount':'total_replies','retweetcount':'total_retweets','quotecount':'total_quotes'})
    year_data=year_data.sort_values(by=['year'])
    return year_data
    


def month_year_wise_twitter_mention_mentions(data):
    month_data=data.groupby(['month_year', 'mentioned_user']).agg({'id':'count','likecount':'sum','replycount':'sum','retweetcount':'sum','quotecount':'sum'})
    month_data=month_data.reset_index()
    month_data=month_data.rename(columns={'id':'total_tweets','likecount':'total_likes','replycount':'total_replies','retweetcount':'total_retweets','quotecount':'total_quotes'})
    month_data=month_data.sort_values(by=['month_year'])
    return month_data

def week_wise_twitter_mention_mentions(data):
    week_data=data.groupby(['week', 'mentioned_user']).agg({'id':'count','likecount':'sum','replycount':'sum','retweetcount':'sum','quotecount':'sum'})
    week_data=week_data.reset_index()
    week_data=week_data.rename(columns={'id':'total_tweets','likecount':'total_likes','replycount':'total_replies','retweetcount':'total_retweets','quotecount':'total_quotes'})
    week_data=week_data.sort_values(by=['week'])
    return week_data




def day_wise_twitter_mention_mentions(data):
    day_data=data.groupby(['date', 'mentioned_user']).agg({'id':'count','likecount':'sum','replycount':'sum','retweetcount':'sum','quotecount':'sum'})
    day_data=day_data.reset_index()
    day_data=day_data.rename(columns={'id':'total_tweets','likecount':'total_likes','replycount':'total_replies','retweetcount':'total_retweets','quotecount':'total_quotes'})
    day_data=day_data.sort_values(by=['date'])
    return day_data
    

def hour_wise_twitter_mention_mentions(data):
    hour_data=data.groupby(['hour', 'mentioned_user']).agg({'id':'count','likecount':'sum','replycount':'sum','retweetcount':'sum','quotecount':'sum'})
    hour_data=hour_data.reset_index()
    hour_data=hour_data.rename(columns={'id':'total_tweets','likecount':'total_likes','replycount':'total_replies','retweetcount':'total_retweets','quotecount':'total_quotes'})
    hour_data=hour_data.sort_values(by=['hour'])
    return hour_data
    



