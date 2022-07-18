import pandas as pd
import psycopg2
import sqlalchemy
from sqlalchemy import create_engine
from connection import conn
import streamlit as st

@st.cache(allow_output_mutation=True)
def over_all_sentiment(data):
    over_all_sentiment_data = data.groupby(['username','vader_sentiment']).agg({'id':'count'})
    over_all_sentiment_data=over_all_sentiment_data.reset_index()
    return over_all_sentiment_data


@st.cache(allow_output_mutation=True)
def year_wise_sentiment(data):
    year_wise_sentiment_data = data.groupby(['year','username','vader_sentiment']).agg({'id','count'})
    year_wise_sentiment_data=year_wise_sentiment_data.reset_index()
    return year_wise_sentiment_data


@st.cache(allow_output_mutation=True)
def month_year_wise_sentiment(data):
    month_year_wise_sentiment_data = data.groupby(['month_year','username','vader_sentiment']).agg({'id','count'})
    month_year_wise_sentiment_data=month_year_wise_sentiment_data.reset_index()
    return month_year_wise_sentiment_data



@st.cache(allow_output_mutation=True)
def day_wise_sentiment(data):
    day_wise_sentiment_data = data.groupby(['date','username','vader_sentiment']).agg({'id','count'})
    day_wise_sentiment_data=day_wise_sentiment_data.reset_index()
    return day_wise_sentiment_data



@st.cache(allow_output_mutation=True)
def hour_wise_sentiment(data):
    hour_wise_sentiment_data = data.groupby(['hour','username','vader_sentiment']).agg({'id','count'})
    hour_wise_sentiment_data=hour_wise_sentiment_data.reset_index()
    return hour_wise_sentiment_data



