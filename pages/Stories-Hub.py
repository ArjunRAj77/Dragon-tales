import streamlit as st
import requests
import json
import random
import os
import re
from gtts import gTTS

# Define the API endpoint
API_ENDPOINT = "https://mongo-gcp-project.uc.r.appspot.com/api/v1/"

st.set_page_config(page_title="Stories Hub", page_icon="📚", layout="centered")
st.title("My Stories 📚")
st.write("All your generated user storie will be displayed here!")
# Function to get the api response from springboot application.
def get_story():
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("GET", API_ENDPOINT, headers=headers)
    # Parse the JSON response
    story = response.text
    #st.write(story)
    return story

# Cleaning up the text from emojis
def remove_emoji(text):
    return re.sub(r'[^\x00-\x7F]+', '', text)

def main():
    data= get_story()
    story_data = json.loads(data)
    # st.write(story_data)
    for i, story in enumerate(story_data, start=1):
        st.header(f' {i} . {story["title"]}')
        # st.write(story)
        st.subheader(f'Genre: {story["genre"]}')
        with st.expander("📚🚀 Ready for an Adventure? Unfold a Magical Tale Here! 🧙‍♀️🌟 "):
            st.write(story["story"])
            if st.button("Read Aloud!",type="primary",key=f'{story["id"]}',help="Generates an audio file for the story."):
                with st.spinner("Generating your story into an audio file...."):
                    cleaned_input = remove_emoji(story["story"])
                    clean_title=remove_emoji(f'{story["title"]}')
                    audio_file_name=f"{clean_title}"
                    st.info("Read the story aloud by playing the below audio file!")    
                    speech = gTTS(text = cleaned_input, lang='en-uk', slow = False)
                    speech.save(f"{audio_file_name}.mp3")
                    st.audio(f"{audio_file_name}.mp3", format='audio/mp3')  

if __name__ == "__main__":
    main()