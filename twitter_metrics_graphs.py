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

def year_wise_total_tweets_plot(data):
    fig = px.line(data, x = "year", y = 'total_tweets',color='username',text='total_tweets',title = 'Year Wise Total Tweets',markers = True)
    fig.update_layout(margin=dict(l=0,r=0))    
    fig.update_traces(textposition='top center')
    fig.update_layout(legend=dict(title_font_family="Times New Roman",font=dict(size= 8), itemwidth = 30))
    st.plotly_chart(fig,use_container_width = True)

def year_wise_total_likes_plot(data):
    fig = px.line(data, x = "year", y = 'total_likes',color='username',text='total_likes',title = 'Year Wise Total Likes',markers = True)
    fig.update_layout(margin=dict(l=0,r=0))
    fig.update_layout(legend=dict(title_font_family="Times New Roman",font=dict(size= 8), itemwidth = 30))    
    fig.update_traces(textposition='top center')
    st.plotly_chart(fig,use_container_width = True)

def year_wise_total_replies_plot(data):
    fig = px.line(data, x = "year", y = 'total_replies',color='username',text='total_replies',title = 'Year Wise Total Replies',markers = True)
    fig.update_layout(margin=dict(l=0,r=0))
    fig.update_layout(legend=dict(title_font_family="Times New Roman",font=dict(size= 8), itemwidth = 30))    
    fig.update_traces(textposition='top center')
    st.plotly_chart(fig,use_container_width = True)

def year_wise_total_retweets_plot(data):
    fig = px.line(data, x = "year", y = 'total_retweets',color='username',title = 'Year Wise Total Retweets',markers = True)
    fig.update_layout(margin=dict(l=0,r=0))
    fig.update_layout(legend=dict(title_font_family="Times New Roman",font=dict(size= 8), itemwidth = 30))    
    fig.update_traces(textposition='top center')
    st.plotly_chart(fig,use_container_width = True)

def year_wise_total_quotes_plot(data):
    fig = px.line(data, x = "year", y = 'total_quotes',color='username',title = 'Year Wise Total Quotes',markers = True)
    fig.update_traces(textposition='top center')
    fig.update_layout(legend=dict(title_font_family="Times New Roman",font=dict(size= 8), itemwidth = 30))    
    st.plotly_chart(fig,use_container_width = True)

def subplotss(data):
    fig1=px.line(data, x = "year", y = 'total_tweets',color='username',title = 'Total Tweets',markers = True)
    fig2=px.line(data, x = "year", y = 'total_likes',color='username',title = 'Total Likes',markers = True)
    fig2=fig2.update_traces(showlegend=False)
    fig3=px.line(data, x = "year", y = 'total_replies',color='username',title = 'Total Replies',markers = True)
    fig3=fig3.update_traces(showlegend=False)    
    figures = [fig1,fig2,fig3]

    fig = make_subplots(rows=1, cols=len(figures)) 

    for i, figure in enumerate(figures):
        for trace in range(len(figure["data"])):
            fig.append_trace(figure["data"][trace], row=1, col=i+1)
    st.plotly_chart(fig)







def month_wise_total_tweets_plot(data):
    fig = px.line(data, x = "month_year", y = 'total_tweets',color='username',title = 'Year Wise Total Tweets',markers = True) 
    fig.update_traces(textposition='top center') 
    fig.update_layout(legend=dict(title_font_family="Times New Roman",font=dict(size= 8), itemwidth = 30))       
    st.plotly_chart(fig,use_container_width = True)

def month_wise_total_likes_plot(data):
    fig = px.line(data, x = "month_year", y = 'total_likes',color='username',title = 'Month Wise Total Likes',markers = True)
    fig.update_traces(textposition='top center')   
    fig.update_layout(legend=dict(title_font_family="Times New Roman",font=dict(size= 8), itemwidth = 30))        
    st.plotly_chart(fig,use_container_width = True)

def month_wise_total_replies_plot(data):
    fig = px.line(data, x = "month_year", y = 'total_replies',color='username',title = 'Month Wise Total Replies',markers = True) 
    fig.update_traces(textposition='top center')   
    fig.update_layout(legend=dict(title_font_family="Times New Roman",font=dict(size= 8), itemwidth = 30))    
    st.plotly_chart(fig,use_container_width = True)

def month_wise_total_retweets_plot(data):
    fig = px.line(data, x = "month_year", y = 'total_retweets',color='username',title = 'Month Wise Total Retweets',markers = True)
    fig.update_traces(textposition='top center')     
    fig.update_layout(legend=dict(title_font_family="Times New Roman",font=dict(size= 8), itemwidth = 30))    
    st.plotly_chart(fig,use_container_width = True)

def month_wise_total_quotes_plot(data):
    fig = px.line(data, x = "month_year", y = 'total_quotes',color='username',title = 'Month Wise Total Quotes',markers = True)
    fig.update_traces(textposition='top center')       
    fig.update_layout(legend=dict(title_font_family="Times New Roman",font=dict(size= 8), itemwidth = 30))    
    st.plotly_chart(fig,use_container_width = True)


def week_wise_total_tweets_plot(data):
    fig = px.line(data, x = "week", y = 'total_tweets',color='username',title = 'Week Wise Total Tweets')
    fig.update_layout(margin=dict(l=0,r=0))    
    fig.update_layout(legend=dict(title_font_family="Times New Roman",font=dict(size= 8), itemwidth = 30))
    st.plotly_chart(fig,use_container_width = True)

def week_wise_total_likes_plot(data):
    fig = px.line(data, x = "week", y = 'total_likes',color='username',title = 'Week Wise Total Likes')
    fig.update_layout(margin=dict(l=0,r=0))
    fig.update_layout(legend=dict(title_font_family="Times New Roman",font=dict(size= 8), itemwidth = 30))    
    st.plotly_chart(fig,use_container_width = True)

def week_wise_total_replies_plot(data):
    fig = px.line(data, x = "week", y = 'total_replies',color='username',text='total_replies',title = 'Week Wise Total Replies',markers = True)
    fig.update_layout(margin=dict(l=0,r=0))
    fig.update_layout(legend=dict(title_font_family="Times New Roman",font=dict(size= 8), itemwidth = 30))    
    st.plotly_chart(fig,use_container_width = True)

def week_wise_total_retweets_plot(data):
    fig = px.line(data, x = "week", y = 'total_retweets',color='username',title = 'Week Wise Total Retweets')
    fig.update_layout(margin=dict(l=0,r=0))
    fig.update_layout(legend=dict(title_font_family="Times New Roman",font=dict(size= 8), itemwidth = 30))    
    st.plotly_chart(fig,use_container_width = True)

def week_wise_total_quotes_plot(data):
    fig = px.line(data, x = "week", y = 'total_quotes',color='username',title = 'Week Wise Total Quotes',markers = True)
    fig.update_layout(legend=dict(title_font_family="Times New Roman",font=dict(size= 8), itemwidth = 30))    
    st.plotly_chart(fig,use_container_width = True)














def day_wise_total_tweets_plot(data):
    fig = px.line(data, x = "computed_date", y ='total_tweets',color='username',title ='Day Wise Total Tweets')
    fig.update_layout(legend=dict(title_font_family="Times New Roman",font=dict(size= 8), itemwidth = 30))     
    st.plotly_chart(fig,use_container_width = True)

def day_wise_total_likes_plot(data):
    fig = px.line(data, x = "computed_date", y = 'total_likes',color='username',title = 'Day Wise Total Likes')
    fig.update_layout(legend=dict(title_font_family="Times New Roman",font=dict(size= 8), itemwidth = 30))    
    st.plotly_chart(fig,use_container_width = True)

def day_wise_total_replies_plot(data):
    fig = px.line(data, x = "computed_date", y = 'total_replies',color='username',title = 'Day Wise Total Replies')
    fig.update_layout(legend=dict(title_font_family="Times New Roman",font=dict(size= 8), itemwidth = 30))    
    st.plotly_chart(fig,use_container_width = True)

def day_wise_total_retweets_plot(data):
    fig = px.line(data, x = "computed_date", y = 'total_retweets',color='username',title = 'Day Wise Total Retweets')
    st.plotly_chart(fig,use_container_width = True)

def day_wise_total_quotes_plot(data):
    fig = px.line(data, x = "computed_date", y = 'total_quotes',color='username',title = 'Date Wise Total Quotes')
    st.plotly_chart(fig,use_container_width = True)


def hour_wise_total_tweets_plot(data):
    fig = px.line(data, x = "hour", y ='total_tweets',color='username',title ='Hour Wise Total Tweets') 
    fig.update_xaxes(rangeslider_visible=True)
    st.plotly_chart(fig,use_container_width = True)

def hour_wise_total_likes_plot(data):
    fig = px.line(data, x = "hour", y = 'total_likes',color='username',title = 'Hour Wise Total Likes')
    st.plotly_chart(fig,use_container_width = True)

def hour_wise_total_replies_plot(data):
    fig = px.line(data, x = "hour", y = 'total_replies',color='username',title = 'Hour Wise Total Replies')
    st.plotly_chart(fig,use_container_width = True)

def hour_wise_total_retweets_plot(data):
    fig = px.line(data, x = "hour", y = 'total_retweets',color='username',title = 'Hour Wise Total Retweets')
    st.plotly_chart(fig,use_container_width = True)

def hour_wise_total_quotes_plot(data):
    fig = px.line(data, x = "hour", y = 'total_quotes',color='username',title = 'Hour Wise Total Quotes')
    st.plotly_chart(fig,use_container_width = True)




