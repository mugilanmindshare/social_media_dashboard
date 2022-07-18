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
from wordcloud import WordCloud
from wordcloud_data_graph import *
from datetime import date
from plotly import graph_objs as go
from datetime import datetime





def find_hashtag_fre(data):   
    hashtag_fre_data = pd.DataFrame(columns=['hashtag','count','username'])
    username_list = data['username'].unique().tolist()
    for i in username_list:
        data1 = data[data['username'] == i]
        hashtag_list=[]
        for j in data1['hashtag']:
            if j != '{}':
                hashtag_list.append(j)
        set_string_list=[]
        for k in hashtag_list:
            set_str= k.replace("{", "")
            set_str=set_str.replace("}","")
            set_string_list.append(set_str)        
        unique_numbers = set(set_string_list)
        unique_list=list(unique_numbers)    
        hashtag_count=[]
        for l in unique_list:
            counts=set_string_list.count(l)
            hashtag_count.append([l,counts])
        hashtag_data=pd.DataFrame(hashtag_count,columns=['hashtag','count'])
        hashtag_data['username'] = i
        hashtag_fre_data = hashtag_fre_data.append(hashtag_data)
    return hashtag_fre_data

def hastags_category_fun(data):
    hashtags_list=[]
    for i in range(len(data['hashtag'])):
        if data['hashtag'].iloc[i].count(',') > 2:
            hashtags_list.append('Multi Variate')
        elif data['hashtag'].iloc[i].count(',') == 2:
            hashtags_list.append('Tri Variate') 
        elif data['hashtag'].iloc[i].count(',') == 1: 
            hashtags_list.append('Bi Variate')
        elif data['hashtag'].iloc[i].count(',') == 0: 
            hashtags_list.append('Uni Variate')
        else:
            a=0    
    data['hashtag_category'] = hashtags_list
    return data       






def find_mentions_fre(data):  
    mentions_fre_data = pd.DataFrame(columns=['mentions','count','username'])
    username_list = data['username'].unique().tolist()
    for i in username_list:
        data1 = data[data['username'] == i]    
        mentions_list=[]
        for j in data1['mentions']:
            if j != '{}':
                mentions_list.append(j)
        set_string_list=[]
        for k in mentions_list:
            set_str= k.replace("{", "")
            set_str=set_str.replace("}","")
            set_string_list.append(set_str)        
        unique_numbers = set(set_string_list)
        unique_list=list(unique_numbers)    
        mentions_count=[]
        for l in unique_list:
            counts=set_string_list.count(l)
            mentions_count.append([l,counts])
        mentions_data=pd.DataFrame(mentions_count,columns=['mentions','count'])
        mentions_data['username']=i
        mentions_fre_data = mentions_fre_data.append(mentions_data)
    return mentions_fre_data


def mentions_category_fun(data):
    mentions_list=[]
    for i in range(len(data['mentions'])):
        if data['mentions'].iloc[i].count(',') > 2:
            mentions_list.append('Multi Variate')
        elif data['mentions'].iloc[i].count(',') == 2:
            mentions_list.append('Tri Variate') 
        elif data['mentions'].iloc[i].count(',') == 1: 
            mentions_list.append('Bi Variate')
        elif data['mentions'].iloc[i].count(',') == 0: 
            mentions_list.append('Uni Variate')
        else:
            a=0    
    data['mentions_category'] = mentions_list
    return data  












def m_find_hashtag_fre(data):   
    hashtag_fre_data = pd.DataFrame(columns=['hashtag','count','mentioned_user'])
    username_list = data['mentioned_user'].unique().tolist()
    for i in username_list:
        data1 = data[data['mentioned_user'] == i]
        hashtag_list=[]
        for j in data1['hashtag']:
            if j != '[]':
                hashtag_list.append(j)
        set_string_list=[]
        for k in hashtag_list:
            set_str= k.replace("[", "")
            set_str=set_str.replace("]","")
            set_string_list.append(set_str)        
        unique_numbers = set(set_string_list)
        unique_list=list(unique_numbers)    
        hashtag_count=[]
        for l in unique_list:
            counts=set_string_list.count(l)
            hashtag_count.append([l,counts])
        hashtag_data=pd.DataFrame(hashtag_count,columns=['hashtag','count'])
        hashtag_data['mentioned_user'] = i
        hashtag_fre_data = hashtag_fre_data.append(hashtag_data)
    return hashtag_fre_data

def m_hastags_category_fun(data):
    hashtags_list=[]
    for i in range(len(data['hashtag'])):
        if data['hashtag'].iloc[i].count(',') > 2:
            hashtags_list.append('Multi Variate')
        elif data['hashtag'].iloc[i].count(',') == 2:
            hashtags_list.append('Tri Variate') 
        elif data['hashtag'].iloc[i].count(',') == 1: 
            hashtags_list.append('Bi Variate')
        elif data['hashtag'].iloc[i].count(',') == 0: 
            hashtags_list.append('Uni Variate')
        else:
            a=0    
    data['hashtag_category'] = hashtags_list
    return data       


def m_find_mentions_fre(data):  
    mentions_fre_data = pd.DataFrame(columns=['mentions','count','mentioned_user'])
    username_list = data['mentioned_user'].unique().tolist()
    for i in username_list:
        data1 = data[data['mentioned_user'] == i]    
        mentions_list=[]
        for j in data1['mentions']:
            if j != '[]':
                mentions_list.append(j)
        set_string_list=[]
        for k in mentions_list:
            set_str= k.replace("[", "")
            set_str=set_str.replace("]","")
            set_string_list.append(set_str)        
        unique_numbers = set(set_string_list)
        unique_list=list(unique_numbers)    
        mentions_count=[]
        for l in unique_list:
            counts=set_string_list.count(l)
            mentions_count.append([l,counts])
        mentions_data=pd.DataFrame(mentions_count,columns=['mentions','count'])
        mentions_data['mentioned_user']=i
        mentions_fre_data = mentions_fre_data.append(mentions_data)
    return mentions_fre_data


def m_mentions_category_fun(data):
    mentions_list=[]
    for i in range(len(data['mentions'])):
        if data['mentions'].iloc[i].count(',') > 2:
            mentions_list.append('Multi Variate')
        elif data['mentions'].iloc[i].count(',') == 2:
            mentions_list.append('Tri Variate') 
        elif data['mentions'].iloc[i].count(',') == 1: 
            mentions_list.append('Bi Variate')
        elif data['mentions'].iloc[i].count(',') == 0: 
            mentions_list.append('Uni Variate')
        else:
            a=0    
    data['mentions_category'] = mentions_list
    return data     