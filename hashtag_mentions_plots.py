from matplotlib.axis import XAxis
from matplotlib.pyplot import autoscale, title
import pandas as pd
import psycopg2
import sqlalchemy
from sqlalchemy import create_engine
from connection import *
from twitter_metrics import *
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from hashtag_data import *






def overall_hashtag_plot(data):
    hashtag_category_data = data.sort_values('count')
    fig = px.bar(hashtag_category_data, y='hashtag', x='count',color='username', orientation='h',title='Overall Hashtags Frequency')
    fig.update_layout(yaxis = dict(tickfont = dict(size=8)))
    st.plotly_chart(fig,use_container_width = True)    
    




def uni_hashtag_plot(data):
    uni_hashtag = data[data['hashtag_category'] == 'Uni Variate']
    uni_hashtag = uni_hashtag.sort_values('count')
    fig = px.bar(uni_hashtag, y='hashtag', x='count',color='username', orientation='h',title='Uni Hashtags Frequency')
    fig.update_layout(yaxis = dict(tickfont = dict(size=8)))
    st.plotly_chart(fig,use_container_width = True)  


def bi_hashtag_plot(data):
    bi_hashtag = data[data['hashtag_category'] == 'Bi Variate']
    bi_hashtag = bi_hashtag.sort_values('count')
    fig = px.bar(bi_hashtag, y='hashtag', x='count',color='username', orientation='h',title='Bi Hashtags Frequency')
    fig.update_layout(yaxis = dict(tickfont = dict(size=8)))
    st.plotly_chart(fig,use_container_width = True)  





def tri_hashtag_plot(data):
    tri_hashtag = data[data['hashtag_category'] == 'Tri Variate']
    tri_hashtag = tri_hashtag.sort_values('count')
    fig = px.bar(tri_hashtag, y='hashtag', x='count',color='username', orientation='h',title='Tri Hashtags Frequency')
    fig.update_layout(yaxis = dict(tickfont = dict(size=8)))
    st.plotly_chart(fig,use_container_width = True)  


def multi_hashtag_plot(data):
    multi_hashtag = data[data['hashtag_category'] == 'Multi Variate']
    multi_hashtag = multi_hashtag.sort_values('count')
    fig = px.bar(multi_hashtag, y='hashtag', x='count',color='username', orientation='h',title='Multi Hashtags Frequency')
    fig.update_layout(yaxis = dict(tickfont = dict(size=8)))
    st.plotly_chart(fig,use_container_width = True)  



def overall_mentions_plot(data):
    mensionss_category_data = data.sort_values('count')
    fig = px.bar(mensionss_category_data, y='mentions', x='count',color='username', orientation='h',title='Overall mentions Frequency')
    fig.update_layout(yaxis = dict(tickfont = dict(size=8)))
    st.plotly_chart(fig,use_container_width = True)   


def uni_mentions_plot(data):
    uni_mentions = data[data['mentions_category'] == 'Uni Variate']
    uni_mentions = uni_mentions.sort_values('count')
    fig = px.bar(uni_mentions, y='mentions', x='count',color='username', orientation='h',title='Uni mention Frequency')
    fig.update_layout(yaxis = dict(tickfont = dict(size=8)))
    st.plotly_chart(fig,use_container_width = True)   


def bi_mentions_plot(data):
    bi_mentions = data[data['mentions_category'] == 'Bi Variate']
    bi_mentions = bi_mentions.sort_values('count')
    fig = px.bar(bi_mentions, y='mentions', x='count',color='username', orientation='h',title='Bi mentions Frequency')
    fig.update_layout(yaxis = dict(tickfont = dict(size=8)))
    st.plotly_chart(fig,use_container_width = True)   


def tri_mentions_plot(data):
    tri_mentions = data[data['mentions_category'] == 'Tri Variate']
    tri_mentions = tri_mentions.sort_values('count')
    fig = px.bar(tri_mentions, y='mentions', x='count',color='username', orientation='h',title='Tri mentions Frequency')
    fig.update_layout(yaxis = dict(tickfont = dict(size=8)))
    st.plotly_chart(fig,use_container_width = True)   



def multi_mentions_plot(data):
    multi_mentions = data[data['mentions_category'] == 'Multi Variate']
    multi_mentions = multi_mentions.sort_values('count')
    fig = px.bar(multi_mentions, y='mentions', x='count',color='username', orientation='h',title='Multi mentions Frequency')
    fig.update_layout(yaxis = dict(tickfont = dict(size=8)))
    st.plotly_chart(fig,use_container_width = True)   






def m_overall_hashtag_plot(data):
    hashtag_category_data = data.sort_values('count')
    fig = px.bar(hashtag_category_data, y='hashtag', x='count',color='mentioned_user', orientation='h',title='Overall Hashtags Frequency')
    fig.update_layout(yaxis = dict(tickfont = dict(size=8)))
    st.plotly_chart(fig,use_container_width = True)        



def m_uni_hashtag_plot(data):
    uni_hashtag = data[data['hashtag_category'] == 'Uni Variate']
    uni_hashtag = uni_hashtag.sort_values('count')
    fig = px.bar(uni_hashtag, y='hashtag', x='count',color='mentioned_user', orientation='h',title='Uni Hashtags Frequency')
    fig.update_layout(yaxis = dict(tickfont = dict(size=8)))
    st.plotly_chart(fig,use_container_width = True)  


def m_bi_hashtag_plot(data):
    bi_hashtag = data[data['hashtag_category'] == 'Bi Variate']
    bi_hashtag = bi_hashtag.sort_values('count')
    fig = px.bar(bi_hashtag, y='hashtag', x='count',color='mentioned_user', orientation='h',title='Bi Hashtags Frequency')
    fig.update_layout(yaxis = dict(tickfont = dict(size=8)))
    st.plotly_chart(fig,use_container_width = True)  





def m_tri_hashtag_plot(data):
    tri_hashtag = data[data['hashtag_category'] == 'Tri Variate']
    tri_hashtag = tri_hashtag.sort_values('count')
    fig = px.bar(tri_hashtag, y='hashtag', x='count',color='mentioned_user', orientation='h',title='Tri Hashtags Frequency')
    fig.update_layout(yaxis = dict(tickfont = dict(size=8)))
    st.plotly_chart(fig,use_container_width = True)  


def m_multi_hashtag_plot(data):
    multi_hashtag = data[data['hashtag_category'] == 'Multi Variate']
    multi_hashtag = multi_hashtag.sort_values('count')
    fig = px.bar(multi_hashtag, y='hashtag', x='count',color='mentioned_user', orientation='h',title='Multi Hashtags Frequency')
    fig.update_layout(yaxis = dict(tickfont = dict(size=8)))
    st.plotly_chart(fig,use_container_width = True)  
















def m_overall_mentions_plot(data):
    mensionss_category_data = data.sort_values('count')
    fig = px.bar(mensionss_category_data, y='mentions', x='count',color='mentioned_user', orientation='h',title='Overall mentions Frequency')
    fig.update_layout(yaxis = dict(tickfont = dict(size=8)))
    st.plotly_chart(fig,use_container_width = True)      



def m_uni_mentions_plot(data):
    uni_mentions = data[data['mentions_category'] == 'Uni Variate']
    uni_mentions = uni_mentions.sort_values('count')
    fig = px.bar(uni_mentions, y='mentions', x='count',color='mentioned_user', orientation='h',title='Uni mention Frequency')
    fig.update_layout(yaxis = dict(tickfont = dict(size=8)))
    st.plotly_chart(fig,use_container_width = True)   


def m_bi_mentions_plot(data):
    bi_mentions = data[data['mentions_category'] == 'Bi Variate']
    bi_mentions = bi_mentions.sort_values('count')
    fig = px.bar(bi_mentions, y='mentions', x='count',color='mentioned_user', orientation='h',title='Bi mentions Frequency')
    fig.update_layout(yaxis = dict(tickfont = dict(size=8)))
    st.plotly_chart(fig,use_container_width = True)   


def m_tri_mentions_plot(data):
    tri_mentions = data[data['mentions_category'] == 'Tri Variate']
    tri_mentions = tri_mentions.sort_values('count')
    fig = px.bar(tri_mentions, y='mentions', x='count',color='mentioned_user', orientation='h',title='Tri mentions Frequency')
    fig.update_layout(yaxis = dict(tickfont = dict(size=8)))
    st.plotly_chart(fig,use_container_width = True)   



def m_multi_mentions_plot(data):
    multi_mentions = data[data['mentions_category'] == 'Multi Variate']
    multi_mentions = multi_mentions.sort_values('count')
    fig = px.bar(multi_mentions, y='mentions', x='count',color='mentioned_user', orientation='h',title='Multi mentions Frequency')
    fig.update_layout(yaxis = dict(tickfont = dict(size=8)))
    st.plotly_chart(fig,use_container_width = True)   
