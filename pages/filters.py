import streamlit as st
from utils.shared import create_connection
import pandas as pd

st.header("Data Filters")

engine= create_connection()

col1,col_space,col2,col_space,col3=st.columns([1,0.2,1,0.2,1])
with col1:
    duration=st.slider("Duration",min_value=0,max_value=300,value=(0,300),step=1)

with col2:
    rating=st.slider("Rating",min_value=0.0,max_value=10.0,value=(0.0,10.0),step=0.1)

with col3:
    votes=st.slider("Votes",min_value=0,max_value=1000000,value=(0,1000000),step=1000)

genre=st.multiselect("Genre",["Action","Adventure","Comedy","Crime","Drama"],default=["Action"])

df=pd.read_sql("SELECT * FROM movies",engine)

df=df[(df["Genre"].isin(genre)) & (df["Duration"]>duration[0]) & (df["Duration"]<duration[1]) & (df["Rating"]>rating[0]) & (df["Rating"]<rating[1]) & (df["Voting_Count"]>votes[0]) & (df["Voting_Count"]<votes[1])]

st.dataframe(df)