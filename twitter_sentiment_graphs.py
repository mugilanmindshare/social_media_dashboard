import pandas as pd
import psycopg2
import sqlalchemy
from sqlalchemy import create_engine
from connection import *
from sentiment import *
import plotly.express as px



def year_wise_sentiment_plot(data):
    fig = px.line(data, x = "year", y = ['Positive','Negative','Neutral'],color = 'username',title = 'Year Wise Sentiment',markers = True, color_discrete_map={ "Positive": "Green", "Negative": "Red","Neutral":"Blue"}) 
    st.plotly_chart(fig,use_container_width = True)




def month_wise_sentiment_plot(data):
    fig = px.line(data, x = "month_year", y = ['Positive','Negative','Neutral'],color='username',title = 'Month Wise Sentiment',markers = True, color_discrete_map = { "Positive": "Green", "Negative": "Red","Neutral":"Blue"}) 
    st.plotly_chart(fig,use_container_width = True)




def day_wise_sentiment_plot(data):
    fig = px.line(data, x = "date", y = ['Positive','Negative','Neutral'],color = 'username',title = 'Day Wise Sentiment', color_discrete_map={ "Positive": "Green", "Negative": "Red","Neutral":"Blue"}) 
    st.plotly_chart(fig,use_container_width = True)        


def hour_wise_sentiment_plot(data):
    fig = px.line(data, x = "datehour", y = ['Positive','Negative','Neutral'],color='username',title = 'Hour Wise Sentiment', color_discrete_map={ "Positive": "Green", "Negative": "Red","Neutral":"Blue"}) 
    st.plotly_chart(fig,use_container_width = True)    