import pandas as pd
import psycopg2
import sqlalchemy
from sqlalchemy import create_engine
from connection import conn
import streamlit as st

def mentions_over_all_sentiment(data):
    over_all_sentiment_data = data.groupby(['mentioned_user','vader_sentiment']).agg({'id':'count'})
    over_all_sentiment_data=over_all_sentiment_data.reset_index()
    return over_all_sentiment_data


def mentions_year_wise_sentiment(data):
    year_wise_sentiment_data = data.groupby(['year','mentioned_user','vader_sentiment']).agg({'id','count'})
    year_wise_sentiment_data=year_wise_sentiment_data.reset_index()
    return year_wise_sentiment_data


def mentions_month_year_wise_sentiment(data):
    month_year_wise_sentiment_data = data.groupby(['month_year','mentioned_user','vader_sentiment']).agg({'id','count'})
    month_year_wise_sentiment_data=month_year_wise_sentiment_data.reset_index()
    return month_year_wise_sentiment_data



def mentions_day_wise_sentiment(data):
    day_wise_sentiment_data = data.groupby(['date','mentioned_user','vader_sentiment']).agg({'id','count'})
    day_wise_sentiment_data = day_wise_sentiment_data.reset_index()
    return day_wise_sentiment_data



def mentions_hour_wise_sentiment(data):
    hour_wise_sentiment_data = data.groupby(['hour','mentioned_user','vader_sentiment']).agg({'id','count'})
    hour_wise_sentiment_data = hour_wise_sentiment_data.reset_index()
    return hour_wise_sentiment_data



