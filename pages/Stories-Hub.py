import streamlit as st
import requests
import json
import random
import os
import re
from gtts import gTTS
import pandas as pd

# Define the API endpoint
API_ENDPOINT = "https://mongo-gcp-project.uc.r.appspot.com/api/v1/"

st.set_page_config(page_title="Stories Hub", page_icon="📚", layout="centered")
st.title("My Stories Hub📚")
st.markdown("""
Welcome to the **My Stories Hub** ! Here you will find all your unique and intriguing user-generated stories. Dive in and let your imagination soar!
""")
# Add color to your text using HTML 
st.markdown("---")

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
    # Create a DataFrame from the stories data
    st.subheader("List of stories 🗺️")
    story_df = pd.DataFrame(story_data)
    story_df = story_df.rename(columns={"title": "Story Title", "genre": "Story Genre"})
    # Display the DataFrame
    st.dataframe(story_df[["Story Title","Story Genre"]],use_container_width=True)
    st.markdown("---")
    st.info("Click on the expander to read the story. Happy reading! :)")
    # st.write(story_data)
    for i, story in enumerate(story_data):
        # Create a new container for each story
        with st.container():
            st.header(f'{i+1}. {story["title"]}')
            st.subheader(f"Genre: {story['genre']}")
            with st.expander("📚🚀 Ready for an Adventure? Unfold a Magical Tale Here! 🧙‍♀️🌟"):
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

            # Add a horizontal rule to visually separate each story
            if i < len(story_data) - 1:  # Avoid adding a horizontal rule after the last story
                st.markdown("---")


if __name__ == "__main__":
    main()