from imaplib import _Authenticator
import matplotlib.pyplot as plt
import ast
from matplotlib.pyplot import title
import streamlit as st
from streamlit_option_menu import option_menu
import wordcloud
import pandas as pd
import psycopg2
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import sqlalchemy
import sys
from sqlalchemy import create_engine
from connection import *
from twitter_metrics import *
from twitter_metrics_graphs import *
import plotly.express as px
from streamlit_card import card
from sentiment import *
from twitter_sentiment_graphs import *
from hashtag_data import *
from wordcloud import WordCloud
from wordcloud_data_graph import *
from datetime import date
from plotly import graph_objs as go
from datetime import datetime
from hashtag_mentions_plots import *
from leader_performance_plots import *
import datetime
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode
import streamlit_card
from streamlit_card import card
import streamlit_authenticator as stauth
from twitter_mentions_data import *
from twitter_mentions_plots import *
from mentions_sentiment import *
from age_followers_tweet_cat import *
import hydralit_components as hc


connection = conn()

data = pd.read_sql_table('social_media_dashboard_login_authentication', connection)

username = data['username'].tolist()
password = data['password'].tolist()
name=[1,2]

authenticator = stauth.Authenticate(name,username,password,'sm_authenticator', 'abcdef', cookie_expiry_days = 30)

name,authentication_status,username = authenticator.login('Login','sidebar')


if authentication_status == 'False':
    st.error('Username/password is incorrect')
if authentication_status == None:
    st.warning('Please enter your username and password')
if authentication_status == True:
    authenticator.logout('Logout','sidebar')
    st.write('chsghjhjhshsejhdchjv')        