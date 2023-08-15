import streamlit as st
import pandas as pd
import pickle

songs_df = pickle.load(open('songs.pkl','rb'))
songs = songs_df['name'].values

dff = pickle.load(open('data.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

def recommend(song):
    song_index = songs_df[songs_df["name"]==song].index[0]
    distance = similarity[song_index]
    songs_list = sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:11]
    recommended_song= []
    for i in songs_list:
        recommended_song.append((songs_df.iloc[i[0]]['name']))
    return recommended_song


st.title('Songs Recommender System')

selected_song = st.selectbox(
    'How would you like to be contacted?', songs)
if st.button('Recoemmend'):
    recommendation = recommend(selected_song)
    for i in recommendation:
        st.write(i)
