import streamlit as st
import requests
import json
import random
from gtts import gTTS
import streamlit as st
import os

st.set_page_config(page_title="Dragon🐉 Tales 📚", page_icon="📚", layout="centered")
# Define the API endpoint
API_ENDPOINT = "https://mongo-gcp-project.uc.r.appspot.com/api/v1/chat"

# Define the set of choices for user input
settings = ['City', 'Forest', 'Beach', 'Space', 'Desert', 'Mountain', 'Underwater city', 'Ancient ruins', 'Haunted house', 'Alien planet', 'Medieval castle', 'Futuristic metropolis']
objectives = ['Find a hidden treasure', 'Rescue a kidnapped person', 'Solve a mystery', 'Survive in a hostile environment', 'Defeat a tyrant', 'Discover a lost civilization', 'Prevent an apocalypse', 'Win a competition', 'Uncover a conspiracy', 'Escape from captivity']
obstacles = ['A powerful enemy', 'Lack of resources', 'A difficult puzzle', 'A treacherous environment', 'A traitor in the team', 'A ticking clock', 'A moral dilemma', 'A haunting past', 'A prophecy or curse', 'A labyrinth or maze']
climaxes = ['Epic battle between good and evil', 'A race against time', 'A test of wits', 'A sacrifice for the greater good', 'A surprising betrayal', 'A revelation of truth', 'A tragic loss', 'A daring rescue', 'A difficult choice', 'A moment of courage']
resolutions = ['Justice prevails', 'Love conquers all', 'The truth is revealed', 'Peace is restored', 'A new beginning', 'A tearful farewell', 'A hard-earned victory', 'A lesson learned', 'A dream come true', 'A return to normalcy']

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

#Text to speech function created using Google text to speech API
def text_to_speech(text, lang='en'):
    speech = gTTS(text = text, lang = lang, slow = False)
    speech.save("text.mp3")


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
        st.info("Click on 'Suprise me '  button for randomly generate a story for you!")
        # When the user clicks the "Suprise" button, create a random story .
        if st.button("Surprise Me!",type="primary"):
                prompt = " Create a random short story with a story title  . Include emojis in the story. Also mention genre of the story."
                data = {
                "message": prompt
                }
                st.subheader("Generated Story 📖")
                st.markdown("---")
                # st.write(data)
                with st.spinner("Generating your story and audio file...."):
                    story=get_story(data)
                    st.write(story)
                    st.info("Read the story aloud by playing the below audio file!")    
                    speech = gTTS(text = story, lang='en-uk', slow = False)
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
                    st.markdown("**Environment** 🌍")
                    setting = st.selectbox("Please select an environment:", settings, key='sett')

                with st.container():
                    st.markdown("**Objective** 🎯")
                    objective = st.selectbox("Please select an objective:", objectives, key='objective')


            with col2:
                with st.container():
                    st.markdown("**Obstacle** 🚧")
                    obstacle = st.selectbox("Please select an obstacle:", obstacles, key='obstacle')
                with st.container():
                    st.markdown("**Climax** 🌋")
                    climax = st.selectbox("Please select a climax:", climaxes, key='climax')

                with st.container():
                    st.markdown("**Resolution** 🏁")
                    resolution = st.selectbox("Please select a resolution:", resolutions, key='resolution')



        # When the user clicks the "Generate Story" button, generate a story based on their choices
        if st.button("Generate personalised story",type="primary"):
            prompt="Write me a story with a story title and emojis included and with the following information. The environment will be"+setting+".The objective of the story is "+objective+". Obstacle type is "+obstacle+".Climax type is "+climax+".Resolution of the story will be "+resolution+". Main character name is "+character
            data = {
                "message": prompt
            }    
            st.subheader("Generated Story 📖")
            st.markdown("---")
            # Temporary printing Response for troubleshooting purposes.
            # st.write(data)
            with st.spinner("Generating your story and audio file...."):
                story = get_story(data)
                st.write(story)
                st.info("Read the story aloud by playing the below audio file!")    
                speech = gTTS(text = story, lang='en', slow = False)
                speech.save("personalstory.mp3")
                st.audio("personalstory.mp3", format='audio/mp3')  

    

    # Set page footer 
    st.write("\n\nMade with :heart: by **Team ⚡Inevitables**")
    st.markdown("Made for **ATLAS Madness Hackathon by Google Cloud and MongoDB ,2023**")
if __name__ == "__main__":
    main()





