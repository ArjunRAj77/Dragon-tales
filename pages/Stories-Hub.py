import streamlit as st
import requests
import json
import random

# Define the API endpoint
API_ENDPOINT = "https://mongo-gcp-project.uc.r.appspot.com/api/v1/"

st.set_page_config(page_title="Stories Hub", page_icon="📚", layout="centered")
st.title("My Stories 📚")
st.write("The  all the user stories will be displayed here!")
def get_story():
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("GET", API_ENDPOINT, headers=headers)
    # Parse the JSON response
    story = response
    return story

def main():
    data= get_story()
    st.write(data)
    # for i, story in enumerate(data, start=1):
    #     st.header(f'Story {i}')
    #     st.subheader(f'ID: {story["id"]}')
    #     st.write(story["story"])

if __name__ == "__main__":
    main()