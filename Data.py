import streamlit as st
import pandas as pd
def app() :
    st.title('Data')
    st.header('This Data is Scraped From Spotify API and Youtube API')
    df=pd.read_csv("Final_Spotify_Youtube_Data.csv")
    df.drop('Unnamed: 0',axis=1,inplace=True)
    df.dropna(axis=0,inplace=True)
    st.dataframe(df)