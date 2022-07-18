import pandas as pd
import psycopg2
import sqlalchemy
from sqlalchemy import create_engine
import streamlit as st


@st.cache(allow_output_mutation=True)
def conn():
    connection_url ='postgresql://mindshare:mindshare@postgresql-76953-0.cloudclusters.net:19477/postgres'
    engine = create_engine(connection_url)
    connection = engine.connect()
    return connection