import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
def app() :
    st.title('Analysis')
    st.subheader('Spotify Analysis')
    spotify_option = st.selectbox('Select The sorting axis',options = ['Danceability' , 'Energy' , 'Liveness', 'Valence', 'Speechiness'],key = 'spotify' )
    df=pd.read_csv('Streamlit Visualiztion.csv')
    year = st.slider("Select a range of values", 1918, 2023, (1981, 2023))
    year_filtered_df = df[(df['Year Of Release'] >=year[0]) & (df['Year Of Release'] <=year[1])]
    fig1 = px.scatter(year_filtered_df, x=spotify_option ,hover_data = ['Artist','Track','Danceability','Energy','Speechiness','Liveness','Valence'],y="Track Popularity",size=year_filtered_df['Stream'])
    st.plotly_chart(fig1, use_container_width=True)
    st.subheader('Album Type')
    fig2 = px.pie(df, names='Album Type')
    fig2.update_traces(textposition='inside')
    fig2.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
    st.plotly_chart(fig2, use_container_width=True)
    def licensed_official_combination(x):
        if x['Licensed']==True and x['Official Video']==True :
            return "The Track has official licensed video" 
        if x['Licensed']==False and x['Official Video']==False :
            return "The Track Doesnot have official licensed video" 
        if x['Licensed']==True and x['Official Video']==False :
            return "The Track has unofficial licensed video"
        if x['Licensed']==False and x['Official Video']==True :
            return "The Track has official unlicensed video"
    df['Official Licensed Combination'] = df.apply(licensed_official_combination,axis=1, result_type='expand')
    st.subheader('Youtube Analysis')
    youtube_option = st.selectbox('Select The sorting axis',options = ['Comments','Likes'],key = 'youtube' )
    views_range = st.select_slider(
    "Select a range of Views u want it",
    options=['0 views',
            '1K Views',
            ' 10K Views',
            '100K Views',
            ' 1 Million Views',
            ' 10 Million Views',
            '100 Million Views',
            '1 billion Views',
            '10 billion Views'],
            value=['0 views', '10 billion Views'],
    )
    dct = {'0 views' : 0, '1K Views' : 3, ' 10K Views' : 4, '100K Views' : 5, ' 1 Million Views' : 6, ' 10 Million Views' : 7, '100 Million Views' : 8,'1 billion Views' : 9, '10 billion Views' : 10}
    min_range = dct[views_range[0]]
    max_range = dct[views_range[1]]
    if min_range != 0 :
        min_range = 10**min_range
    if max_range != 0 :
        max_range = 10**max_range
    views_filtered_df=df[ (df['Views']>=min_range) & (df['Views']<=max_range)]
    fig3=px.scatter(data_frame=views_filtered_df,x='Views',y=youtube_option,hover_data=['Title','Channel','Views','Likes','Comments','Official Licensed Combination'],size=views_filtered_df['Views'].tolist(),color='Official Licensed Combination')
    st.plotly_chart(fig3, use_container_width=True)