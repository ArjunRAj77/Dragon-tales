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
Welcome to the **My Stories Hub** ! 

Here you will find all your unique and intriguing user-generated stories. Dive in and let your imagination soar!
""")
# Add color to your text using HTML 
st.markdown("---")
# Get list of all genres
all_genres = ['Fantasy', 'Sci-Fi', 'Mystery', 'Romance', 'Action', 'Horror', 'Thriller', 'Adventure', 'Comedy', 'Drama', 'Historical', 'Non-fiction','Dark-humour']


# Function to get the api response from springboot application.
def get_story():
    with st.spinner("Connecting with the MongoDB ....."):
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

# Function for favourite button handling.
def update_favourite_status(story_id, is_favourite):
    url = f"https://mongo-gcp-project.uc.r.appspot.com/api/v1/{story_id}"
    data = {"favorite": "false" if is_favourite else "true"}
    response = requests.put(url, data=data)
    if response.status_code == 200:
        st.success(f"Successfully {'added to' if is_favourite else 'removed from'} favourites!")
    else:
        st.error("Failed to update favourite status.")


def display_story_df(story_data):
    st.subheader("📚 Your Story Archive 🗺️")
    story_df = pd.DataFrame(story_data)
    story_df = story_df.rename(columns={"title": "Story Title", "genres": "Story Genre"})
    # Display the DataFrame
    st.dataframe(story_df[["Story Title","Story Genre"]],use_container_width=True)

def display_story(i, story, read_aloud):
    with st.container():
        st.header(f'{i+1}. {story["title"]}')
        combined_genres = ', '.join(story["genres"])  # Join the genres with a comma
        st.subheader(f"Genre: {combined_genres}")
        st.info("Click on the expander to read the story. Happy reading! :)")
        with st.expander("📚🚀 Unfold Your Tale 🧙‍♀️🌟"):
            st.write(story["story"])
            if read_aloud and st.button("Read Aloud!",type="primary",key=f'{story["id"]}',help="Generates an audio file for the story."):
                with st.spinner("Generating your story into an audio file...."):
                    cleaned_input = remove_emoji(story["story"])
                    clean_title=remove_emoji(f'{story["title"]}')
                    audio_file_name=f"{clean_title}"
                    st.info("Read the story aloud by playing the below audio file!")    
                    speech = gTTS(text = cleaned_input, lang='en-uk', slow = False)
                    speech.save(f"{audio_file_name}.mp3")
                    st.audio(f"{audio_file_name}.mp3", format='audio/mp3')
                        # Favourite status button
            button_key = f"fav_button_{i}_{story['id']}"
            if st.button('Add to favourites' if story['favorite'] == 'false' else 'Added to favourites', key=f'{button_key}'):
                update_favourite_status(story['id'], story['favorite'] == 'true')  # here, we pass True if the story is already a favourite, and False otherwise
                st.experimental_rerun()


def display_stories(story_data, read_aloud=False):
    for i, story in enumerate(story_data):
        display_story(i, story, read_aloud)
        # Add a horizontal rule to visually separate each story
        if i < len(story_data) - 1:  # Avoid adding a horizontal rule after the last story
            st.markdown("---") 

def filter_stories(filter_input_data):
    selected_genres = st.multiselect('Select genres', options=list(all_genres))
    filtered_data = [story for story in filter_input_data if set(selected_genres).intersection(set(story["genres"]))]
    if not filtered_data:
        st.warning("🔍 No stories found with the selected genre. Try a different filter!")
        return []
    else:
        return filtered_data

def reset_all_favourites(story_data):
    for story in story_data:
        if story['favorite'] == 'true':
            url = f"https://mongo-gcp-project.uc.r.appspot.com/api/v1/{story['id']}"
            data = {"favorite": "false"}
            response = requests.put(url, data=data)
            if response.status_code != 200:
                st.error(f"Failed to reset favourite status for story with ID {story['id']}")

def main():
    data= get_story()
    story_data = json.loads(data)
    # Display the DataFrame
    display_story_df(story_data)
    st.markdown("---")
    st.info("🔍 Check the box below to filter stories by genre!")
    agree = st.checkbox('🔍 Apply Story Filter')

    # Let the user decide if they want to see only favourite stories
    show_favourites_only = st.checkbox("🌟 Show only favourite stories", value=False)

    if show_favourites_only:
        # Filter the stories to include only the favourites
        favourite_stories = [story for story in story_data if story['favorite'] == 'true']

        if not favourite_stories:
            # If the user doesn't have any favourite stories, display a message
            st.info("😞 You don't have any favourite stories yet. Add some to see them here!")
        else:
            # If the user has favourite stories, display them
            st.markdown("## 🌟 Your Favourite Tales")
            st.success("Your favourite short stories are here. Happy reading! 😊")
            # Add this in your main function
            if st.button("Reset all favourites"):
                reset_all_favourites(story_data)
                st.success("Successfully reset all favourites!")
                st.experimental_rerun()
            else:
                display_stories(favourite_stories,read_aloud=True)
    else:
        if agree :
            st.markdown("## 🌟 Filtered Tales")
            st.success("All your selected short stories are here. Happy reading! :)")
            filtered_data = filter_stories(story_data)
            display_stories(filtered_data, read_aloud=True)
        else:
            st.markdown("## 📚 Complete List of Short Stories")
            st.success("All your short stories are here. Happy reading! :)")
            display_stories(story_data, read_aloud=True)

# def main():
#     data= get_story()
#     story_data = json.loads(data)
#     filter_input_data=story_data#Simply copying the data
#     # Create a DataFrame from the stories data
#     st.subheader("📚 Your Story Archive 🗺️")
#     story_df = pd.DataFrame(story_data)
#     story_df = story_df.rename(columns={"title": "Story Title", "genres": "Story Genre"})
#     # Display the DataFrame
#     st.dataframe(story_df[["Story Title","Story Genre"]],use_container_width=True)
#     st.markdown("---")
#     # st.write(story_data)
#     st.info("🔍 Check the box below to filter stories by genre!")
#     agree = st.checkbox('🔍 Apply Story Filter')

#     if agree :
#         st.markdown("## 🌟 Filtered Tales")
#         st.success("All your selected short stories are here. Happy reading! :)")
#         selected_genres = st.multiselect('Select genres', options=list(all_genres))
#         filtered_data = [story for story in filter_input_data if set(selected_genres).intersection(set(story["genres"]))]
#         if not filtered_data:
#             st.warning("🔍 No stories found with the selected genre. Try a different filter!")
#         else :
#             # Printing out the filtered content!
#             for i,story in enumerate(filtered_data):
#                 with st.container():
#                     st.header(f'{i+1}. {story["title"]}')
#                     combined_genres = ', '.join(story["genres"])  # Join the genres with a comma
#                     st.subheader(f"Genre: {combined_genres}")
#                     st.info("Click on the expander to read the story. Happy reading! :)")
#                     with st.expander("📚🚀 Unfold Your Tale 🧙‍♀️🌟"):
#                         st.write(story["story"])
#                         if st.button("Read Aloud!",type="primary",key=f'{story["id"]}',help="Generates an audio file for the story."):
#                             with st.spinner("Generating your story into an audio file...."):
#                                 cleaned_input = remove_emoji(story["story"])
#                                 clean_title=remove_emoji(f'{story["title"]}')
#                                 audio_file_name=f"{clean_title}"
#                                 st.info("Read the story aloud by playing the below audio file!")    
#                                 speech = gTTS(text = cleaned_input, lang='en-uk', slow = False)
#                                 speech.save(f"{audio_file_name}.mp3")
#                                 st.audio(f"{audio_file_name}.mp3", format='audio/mp3') 
#     else:
#         st.markdown("## 📚 Complete List of Short Stories")
#         st.success("All your short stories are here. Happy reading! :)")
#         for i, story in enumerate(story_data):
#             # Create a new container for each story
#             with st.container():
#                 st.header(f'{i+1}. {story["title"]}')
#                 combined_genres = ', '.join(story["genres"])  # Join the genres with a comma
#                 st.subheader(f"Genre: {combined_genres}")
#                 st.info("Click on the expander to read the story. Happy reading! :)")
#                 with st.expander("📚🚀 Unfold Your Tale 🧙‍♀️🌟"):
#                     st.write(story["story"])
#                     if st.button("Read Aloud!",type="primary",key=f'{story["id"]}',help="Generates an audio file for the story."):
#                         with st.spinner("Generating your story into an audio file...."):
#                             cleaned_input = remove_emoji(story["story"])
#                             clean_title=remove_emoji(f'{story["title"]}')
#                             audio_file_name=f"{clean_title}"
#                             st.info("Read the story aloud by playing the below audio file!")    
#                             speech = gTTS(text = cleaned_input, lang='en-uk', slow = False)
#                             speech.save(f"{audio_file_name}.mp3")
#                             st.audio(f"{audio_file_name}.mp3", format='audio/mp3')  

#                 # Add a horizontal rule to visually separate each story
#                 if i < len(story_data) - 1:  # Avoid adding a horizontal rule after the last story
#                     st.markdown("---")


if __name__ == "__main__":
    main()