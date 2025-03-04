import streamlit as st
import pandas as pd
def app() :
    st.title('Descrption')
    st.write('''This Dataset of songs of various artist in the world and for each song is present:
''',unsafe_allow_html =True)
    st.markdown('''
<ul>
  <li>Track: Name of the song, as visible on the Spotify platform.</li>
  <li>Artist: Name of the artist.</li>
  <li>Stream: Number of streams of the song on Spotify.</li>
  <li>Duration in ms: The duration of the track in milliseconds.</li>
  <li>Album: The album in Which the song is contained on Spotify.</li>
  <li>Album Type: Indicates if the song is relesead on Spotify as a single or contained in an album.</li>
  <li>Release Date : Release Date of the track.</li>
  <li>Popularity : Popularity of the track The value will be between 0 and 100, with 100 being the most popular.</li>
  <li>URL Spotify: The URL of the artist.</li>
  <li>URL: A Spotify link used to find the song through the API.</li>
  <li>Danceability: Describes how suitable a track is for dancing based on a combination of musical elements including tempo,
      rhythm stability, beat strength, and overall regularity. A value of 0.0 is least danceable and 1.0 is most danceable.</li>
  <li>Energy: A measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity. Typically, energetic tracks feel fast, loud, and noisy. For example, death metal has high energy, while a Bach prelude scores low on the scale. Perceptual features contributing to this attribute include dynamic range, perceived loudness, timbre, onset rate, and general entropy.</li>
  <li>Liveness: Detects the presence of an audience in the recording. Higher liveness values represent an increased probability that the track was performed live. A value above 0.8 provides strong likelihood that the track is live.</li>
  <li>Valence: A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. Tracks with high valence sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence sound more negative (e.g. sad, depressed, angry). </li>
   <li>Speechiness: “Speechiness detects the presence of spoken words in a track”. If the speechiness of a song is above 0.66, it is probably made of spoken words, a score between 0.33 and 0.66 is a song that may contain both music and words, and a score below 0.33 means the song does not have any speech.</li>
  <li>URL YouTube: URL of the video linked to the song on Youtube, if it have any.</li>
  <li>Title: Title of the videoclip on youtube.</li>
  <li>Channel: Name of the channel that have published the video.</li>
  <li>Views: Number of views.</li>
  <li>Likes: Number of likes.</li>
  <li>Comments: Number of comments.</li>
  <li>Licensed: Indicates whether the video represents licensed content, which means that the content was uploaded to a channel linked to a YouTube content partner and then claimed by that partner.</li>
  <li>Official Video: boolean value that indicates if the video found is the official video of the song.</li>
</ul>''', unsafe_allow_html=True)