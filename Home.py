import streamlit as st
import requests
import json
import random
from gtts import gTTS
import os
import re

st.set_page_config(page_title="Dragon🐉 Tales 📚", page_icon="📚", layout="centered")
# Define the API endpoint
API_ENDPOINT = "https://mongo-gcp-project.uc.r.appspot.com/api/v1/chat"

# Define the set of choices for user input
settings = ['City', 'Forest', 'Beach', 'Space', 'Desert', 'Mountain', 'Underwater city', 'Ancient ruins', 'Haunted house', 'Alien planet', 'Medieval castle', 'Futuristic metropolis']
objectives = ['Find a hidden treasure', 'Rescue a kidnapped person', 'Solve a mystery', 'Survive in a hostile environment', 'Defeat a tyrant', 'Discover a lost civilization', 'Prevent an apocalypse', 'Win a competition', 'Uncover a conspiracy', 'Escape from captivity']
obstacles = ['A powerful enemy', 'Lack of resources', 'A difficult puzzle', 'A treacherous environment', 'A traitor in the team', 'A ticking clock', 'A moral dilemma', 'A haunting past', 'A prophecy or curse', 'A labyrinth or maze']
climaxes = ['Epic battle between good and evil', 'A race against time', 'A test of wits', 'A sacrifice for the greater good', 'A surprising betrayal', 'A revelation of truth', 'A tragic loss', 'A daring rescue', 'A difficult choice', 'A moment of courage']
genre = ['Fantasy', 'Sci-Fi', 'Mystery', 'Romance', 'Action', 'Horror', 'Thriller', 'Adventure', 'Comedy', 'Drama', 'Historical', 'Non-fiction','Dark-humour','Magical Realism']


# Function to send a message to API server and retrieve the response.
def get_story(data):
    payload = json.dumps(data)
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", API_ENDPOINT, headers=headers, data=payload)
    # Parse the JSON response
    story = response.text
    return story


# Cleaning up the text from emojis
def remove_emoji(text):
    return re.sub(r'[^\x00-\x7F]+', '', text)


def main():
    # Display a title
    st.title("Dragon🐉 Tales 📚")

    # Display some artwork (you'll need to provide the image file)
    st.image("dragontales.png")

    st.markdown("""
    # Welcome to the Dragon🐉 Tales! 📚✨

    Embark on a thrilling journey of imagination and adventure! This application allows you to craft your own unique story by selecting various elements such as the setting, objective, obstacle, climax, resolution, and even the name of your main character.

    Once you've made your choices, click the 'Generate Story' button to bring your story to life. If you're feeling adventurous, try the 'Suprise Me' button for a surprise combination!

    So, what are you waiting for? Dive in, and let's create some unforgettable tales together.
    
    Happy storytelling!✨
    """)
    tab1, tab2 = st.tabs(["Random Stories", "Personalised Stories"])
    with tab1 : 
        st.subheader("Story 📚 Board")
        st.info("Click on 'Surprise Me '  button for randomly generate a story for you!")
        # When the user clicks the "Suprise" button, create a random story .
        if st.button("Surprise Me!",type="primary"):
                prompt = " Create a random short story with a story title  . Include emojis in the story. Also mention genre of the story."
                data = {
                "message": prompt
                }
                st.subheader("Generated Story 📖")
                st.markdown("---")
                with st.spinner("Generating your story and audio file...."):
                    story = get_story(data)
                    story_data = json.loads(story)
                    story_title= story_data["title"]
                    combined_genres = ', '.join(story_data["genres"])
                    st.success('✨ Your short story was generated successfully! You can now view it in the 📚 Stories Hub.')
                    st.title(f'{story_title}')
                    st.subheader(f'Genre : {combined_genres}')
                    st.write(story_data["story"])
                    story_body=story_data["story"]
                    cleaned_input = remove_emoji(story_body)
                    st.info("Read the story aloud by playing the below audio file!")    
                    speech = gTTS(text = cleaned_input, lang='en-uk', slow = False)
                    speech.save("story.mp3")
                    st.audio("story.mp3", format='audio/mp3')     
    
    with tab2:
        # Ask the user to select a choice for each category
        st.subheader("Story 📚 Board")
        st.info("Choose your own personalised settings and hit 'Generate stories' button!")
        with st.expander("⚙️ Advanced Settings "):
        # Splitting the features into two column for better UI
            col1, col2 = st.columns(2)  
            with col1:
                with st.container():
                    st.markdown("**Main Character** 🧑")
                    character = st.text_input("Please enter a name for the main character:", key='character')
                with st.container():
                    st.markdown("**Genre** 🌍")
                    Genres = st.selectbox("Please select a resolution:", genre, key='genre')
                with st.container():
                    st.markdown("**Environment** 🌍")
                    setting = st.selectbox("Please select an environment:", settings, key='sett')


            with col2:
                with st.container():
                    st.markdown("**Objective** 🎯")
                    objective = st.selectbox("Please select an objective:", objectives, key='objective')
                with st.container():
                    st.markdown("**Obstacle** 🚧")
                    obstacle = st.selectbox("Please select an obstacle:", obstacles, key='obstacle')
                with st.container():
                    st.markdown("**Climax** 🌋")
                    climax = st.selectbox("Please select a climax:", climaxes, key='climax')


        # When the user clicks the "Generate Story" button, generate a story based on their choices
        if st.button("Generate Personalised Story",type="primary"):
            prompt="Write me a story with a story title and mention genre  and  include emojis in the story and include the following information. The environment will be"+setting+".The Genre of the story should be "+Genres+". The objective of the story is "+objective+". Obstacle type is "+obstacle+".Climax type is "+climax+". Main character name is "+character
            data = {
                "message": prompt
            }    
            st.subheader("Generated Story 📖")
            st.markdown("---")
            with st.spinner("Generating your story and audio file...."):
                story = get_story(data)
                story_data = json.loads(story)
                story_title= story_data["title"]
                combined_genres = ', '.join(story_data["genres"])  # Join the genres with a comma
                st.success('✨ Your short story was generated successfully! You can now view it in the 📚 Stories Hub.')
                st.title(f'{story_title}')
                st.subheader(f"Genre: {combined_genres}")
                st.write(story_data["story"])
                story_body=story_data["story"]
                cleaned_input = remove_emoji(story_body)
                st.info("Read the story aloud by playing the below audio file!")    
                speech = gTTS(text = cleaned_input, lang='en', slow = False)
                speech.save("personalstory.mp3")
                st.audio("personalstory.mp3", format='audio/mp3')  

    

    # Set page footer 
    st.write("\n\nMade with :heart: by **Team ⚡Inevitables**")
    st.markdown("Made for **ATLAS Madness Hackathon by Google Cloud and MongoDB ,2023**")
if __name__ == "__main__":
    main()





