import streamlit as st

st.set_page_config(page_title="About 📚", page_icon="📚", layout="centered")


st.markdown("""
# Welcome to the Dragon🐉 Tales! 📚✨

Embark on a thrilling journey of imagination and adventure! This application allows you to craft your own unique story by selecting various elements such as the setting, objective, obstacle, climax, resolution, and even the name of your main character.

Once you've made your choices, click the 'Generate Story' button to bring your story to life. If you're feeling adventurous, try the 'Suprise Me' button for a surprise combination!

So, what are you waiting for? Dive in, and let's create some unforgettable tales together.
    
Happy storytelling!✨
""")
st.markdown("---")
st.subheader("Meet the Team")
st.markdown("""
#### Team Inevitables
- Arjun Raj
- Akshaymon K V
- Akhil M Anil
- Akshay V Anil
""")

import streamlit as st

# Assume this is your data
data = [
    {
        "id": 1,
        "title": "The Enchanted Emoji Forest 🌳🌺🌟",
        "genre": ["Fantasy", "Adventure"],
        "story_link": "link_to_story1",
    },
    {
        "id": 2,
        "title": "\"The Lost Adventure 🗺️\"",
        "genre": ["Adventure", "Mystery"],
        "story_link": "link_to_story2",
    },
]

# Get list of all genres
all_genres = set([genre for story in data for genre in story["genre"]])

selected_genres = st.multiselect('Select genres', options=list(all_genres))

filtered_data = [story for story in data if set(selected_genres).intersection(set(story["genre"]))]

for story in filtered_data:
    link = f"[{story['title']}]({story['story_link']})"
    st.markdown(link, unsafe_allow_html=True)
