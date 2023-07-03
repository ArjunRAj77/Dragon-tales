import streamlit as st
import requests
import json
import random

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

def main():
    # Display a title
    st.title("Dragon🐉 Tales 📚")

    # Display some artwork (you'll need to provide the image file)
    st.image("dragontales.png")

    st.markdown("""
    # Welcome to the Dragon🐉 Tales! 📚✨

    Embark on a thrilling journey of imagination and adventure! This application allows you to craft your own unique story by selecting various elements such as the setting, objective, obstacle, climax, resolution, and even the name of your main character.

    Once you've made your choices, click the 'Generate Story' button to bring your story to life. If you're feeling adventurous, try the 'Randomize' button for a surprise combination!

    So, what are you waiting for? Dive in, and let's create some unforgettable tales together.
    
    Happy storytelling!✨
    """)

    # Ask the user to select a choice for each category
    with st.container():
        st.subheader("Setting 🌍")
        setting = st.selectbox("Please select a setting:", settings, key='sett')

    with st.container():
        st.subheader("Objective 🎯")
        objective = st.selectbox("Please select an objective:", objectives, key='objective')

    with st.container():
        st.subheader("Obstacle 🚧")
        obstacle = st.selectbox("Please select an obstacle:", obstacles, key='obstacle')

    with st.container():
        st.subheader("Climax 🌋")
        climax = st.selectbox("Please select a climax:", climaxes, key='climax')

    with st.container():
        st.subheader("Resolution 🏁")
        resolution = st.selectbox("Please select a resolution:", resolutions, key='resolution')

    with st.container():
        st.subheader("Main Character 🧑")
        character = st.text_input("Please enter a name for the main character:", key='character')

    # When the user clicks the "Generate Story" button, generate a story based on their choices
    if st.button("Generate Story",type="primary"):
        # data = {
        #       "message": "write me a story"
        #     }
        prompt="Write me a story with emojis included and with the following information. The environment will be"+setting+".The objective of the story is "+objective+". Obstacle type is "+obstacle+".Climax type is "+climax+".Resolution of the story will be "+resolution+". Main character name is "+character
        data = {
              "message": prompt
        }    
        # data = {
        #       "message": "write me a story with emojis included and using the storyPlot parameters provided.The main character name is Peter.",
        #       "storyPlot": {
        #         "environment": setting,
        #         "objective": objective,
        #         "obstacle": obstacle,
        #         "climax": climax,
        #         "resolution type ": resolution,
        #         "main character name": character
        #       }
        # }        
        # For now, display a sample text as the generated story
        #story = "Once upon a time, in a " + setting + ", " + character + " set out to " + objective + ". But they faced a major obstacle: " + obstacle + ". The climax of their journey was a " + climax + ". In the end, " + resolution + "."
        st.subheader("Generated Story 📖")
        # Temporary printing Response for troubleshooting purposes.
        st.write(data)
        story = get_story(data)
        st.write(story)


    
    # When the user clicks the "Randomize" button, select random choices for each category
    if st.button("Randomize",type="primary"):
        st.selectbox("Please select a setting:", settings, index=random.randint(0, len(settings)-1))
        st.selectbox("Please select an objective:", objectives, index=random.randint(0, len(objectives)-1))
        st.selectbox("Please select an obstacle:", obstacles, index=random.randint(0, len(obstacles)-1))
        st.selectbox("Please select a climax:", climaxes, index=random.randint(0, len(climaxes)-1))
        st.selectbox("Please select a resolution:", resolutions, index=random.randint(0, len(resolutions)-1))
        st.text_input("Please enter a name for the main character:", value="Character " + str(random.randint(1, 100)))
    
    # Set page footer 
    st.write("\n\nMade with :heart: by Team ⚡Inevitables ")
    st.write("ATLAS MADNESS Hackathon by Google Cloud and MongoDB ,2023")
if __name__ == "__main__":
    main()





