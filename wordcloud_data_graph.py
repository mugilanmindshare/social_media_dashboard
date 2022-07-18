import wordcloud_data_graph
from wordcloud import WordCloud
import pandas as pd
import psycopg2
import sqlalchemy
from sqlalchemy import create_engine
from connection import conn
import streamlit as st
from connection import *
from sentiment import *
import plotly.express as px
import matplotlib.pyplot as plt


@st.cache(allow_output_mutation=True)
def wordcloud_data():
    con=conn()
    wordcloud_data_df = pd.read_sql_table('wordcloud_data', con)
    return wordcloud_data_df


def overall_wordcloud(data):
    Words = ' '.join([text for text in data])
    wordcloud = WordCloud(width=800, height=500, random_state=21, max_font_size=110).generate(Words)
    plt.figure(figsize=(10, 10)) 
    plt.imshow(wordcloud, interpolation="bilinear") 
    plt.axis('off')
    plt.title('Wordcloud for Overall Tweets')
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()  

def positive_wordcloud(data):
    Words = ' '.join([text for text in data])
    wordcloud = WordCloud(width=800, height=500, random_state=21, max_font_size=110).generate(Words)
    plt.figure(figsize=(10, 10)) 
    plt.imshow(wordcloud, interpolation="bilinear") 
    plt.axis('off')
    plt.title('Wordcloud for positive Tweets')
    st.pyplot()  

def negative_wordcloud(data):
    Words = ' '.join([text for text in data])
    wordcloud = WordCloud(width=800, height=500, random_state=21, max_font_size=110).generate(Words)
    plt.figure(figsize=(10, 10)) 
    plt.imshow(wordcloud, interpolation="bilinear") 
    plt.axis('off')
    plt.title('Wordcloud for negative Tweets')
    st.pyplot()  


def neutral_wordcloud(data):
    Words = ' '.join([text for text in data])
    wordcloud = WordCloud(width=800, height=500, random_state=21, max_font_size=110).generate(Words)
    plt.figure(figsize=(10, 10)) 
    plt.imshow(wordcloud, interpolation="bilinear") 
    plt.axis('off')
    plt.title('Wordcloud for neutral Tweets')
    st.pyplot()              