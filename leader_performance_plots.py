from matplotlib.axis import XAxis
from matplotlib.pyplot import title
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



def leaders_overall_performance(data):
    leaders_performance = data.groupby('username').agg({'id':'count','likecount':'sum','replycount':'sum','retweetCount':'sum','quotecount':'sum'})
    leaders_performance = leaders_performance.reset_index()
    leaders_performance=leaders_performance.rename(columns={'id':'Total_Tweets','likecount':'total_likes','replycount':'total_replies','retweetCount':'total_retweets','quotecount':'total_quotes'})
    leaders_performance['Avg_Likes_per_Tweet'] = round(leaders_performance['total_likes']/leaders_performance['Total_Tweets'])
    leaders_performance['Avg_Replies_per_Tweet'] = round(leaders_performance['total_replies']/leaders_performance['Total_Tweets'])
    leaders_performance['Avg_Retweets_per_Tweet'] = round(leaders_performance['total_retweets']/leaders_performance['Total_Tweets'])
    leaders_performance['Avg_Quotes_per_Tweet'] = round(leaders_performance['total_quotes']/leaders_performance['Total_Tweets'])  
    return leaders_performance



def leader_overall_performance_radar_chart(data):
    data_value = data[['Total_Tweets','Avg_Likes_per_Tweet','Avg_Replies_per_Tweet','Avg_Retweets_per_Tweet','Avg_Quotes_per_Tweet']]
    data_value = pd.DataFrame(data_value)
    data_label = data['username']
    data_label = pd.DataFrame(data_label)  
    fig = go.Figure()

    for i in data_label.index.values:
        fig.add_trace(go.Scatterpolar(r=data_value.loc[i].values,theta=data_value.columns,fill='toself',name="WINE-%s"%data_label.username[i],showlegend=True,))

    fig.update_layout(polar=dict(radialaxis=dict(visible=True,)),title="Leaders OverAll Performance")

    st.plotly_chart(fig,use_container_width = True)  



def leader_overall_performance_radar_chart_selected_time_range(data):
    data_value = data[['Total_Tweets','Avg_Likes_per_Tweet','Avg_Replies_per_Tweet','Avg_Retweets_per_Tweet','Avg_Quotes_per_Tweet']]
    data_value = pd.DataFrame(data_value)
    data_label = data['username']
    data_label = pd.DataFrame(data_label)  
    fig = go.Figure()

    for i in data_label.index.values:
        fig.add_trace(go.Scatterpolar(r=data_value.loc[i].values,theta=data_value.columns,fill='toself',name="WINE-%s"%data_label.username[i],showlegend=True,))

    fig.update_layout(polar=dict(radialaxis=dict(visible=True,)),title="Leaders OverAll Performance Between Selected Time Range")

    st.plotly_chart(fig,use_container_width = True)  



