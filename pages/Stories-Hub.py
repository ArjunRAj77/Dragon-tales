import streamlit as st
import requests
import json
import random

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

if __name__ == "__main__":
    main()