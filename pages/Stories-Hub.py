
from gtts import gTTS
import streamlit as st
import os
import streamlit as st

st.set_page_config(page_title="Stories Hub", page_icon="📚", layout="centered")
st.title("My Stories 📚")
st.write("The  all the user stories will be displayed here!")

def text_to_speech(text, lang='en'):
    speech = gTTS(text = text, lang = lang, slow = False)
    speech.save("text.mp3")
    
user_input = st.text_input("Write something here.") 
if st.button('Generate Speech'):
    text_to_speech(user_input)
    st.audio("text.mp3", format='audio/mp3')