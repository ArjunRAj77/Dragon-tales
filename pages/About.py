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





# Assuming that stories is your list of story dictionaries
stories = [
    {"title": "The Enchanted Emoji Forest 🌳🌺🌟", "genre": "Fantasy/Adventure", "content": "Story 1..Embark on a thrilling journey of imagination and adventure! This application allows you to craft your own unique story by selecting various elements such as the setting, objective, obstacle, climax, resolution, and even the name of your main character.Once you've made your choices, click the 'Generate Story' button to bring your story to life. If you're feeling adventurous, try the 'Suprise Me' button for a surprise combination!So, what are you waiting for? Dive in, and let's create some unforgettable tales together.."},
    {"title": "The Lost Adventure 🗺️", "genre": "Adventure/Mystery", "content": "Story 2..."},
    {"title": "The Enchanted Garden 🌿", "genre": "Fantasy", "content": "Story 3..."},
    # Add more stories as needed...
]

for i, story in enumerate(stories):
    # Create a new container for each story
    with st.container():
        st.header(story["title"])
        st.subheader(f"Genre: {story['genre']}")
        with st.expander("📚🚀 Ready for an Adventure? Unfold a Magical Tale Here! 🧙‍♀️🌟"):
            st.write(story["content"])

        # Add a horizontal rule to visually separate each story
        if i < len(stories) - 1:  # Avoid adding a horizontal rule after the last story
            st.markdown("---")
