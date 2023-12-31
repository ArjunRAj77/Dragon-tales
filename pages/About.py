import streamlit as st

st.set_page_config(page_title="About 📚", page_icon="📚", layout="centered")

def app():
    st.title("About Dragon Tales 🐉📚")

    st.markdown("## Project Description 📝")
    st.markdown("""
    Welcome to Dragon Tales, a powerful and user-friendly short story generator! This project uses artificial intelligence to generate unique, immersive, and engaging short stories based on a genre selected by the user. With an elegant Streamlit UI, Dragon Tales provides a clean and simple interface for users to navigate their stories, filter them by genre, and mark them as favorites for easy access later.
    """)

    st.markdown("## Team Members 👥")
    st.markdown("""
    **Team Inevitables**

    - [**Arjun Raj**](https://www.linkedin.com/in/arjun-raj-pala/)
    - [**Akshay V Anil**](https://www.linkedin.com/in/akshayvanil/)
    - [**Akshaymon K V**](https://www.linkedin.com/in/akshaymonkvn3/)
    - [**Akhil M Anil**](https://www.linkedin.com/in/akhil-m-anil-2bb54a122/)
    """)

    st.markdown("## Benefits 🎁")
    st.markdown("""
    - **Creativity Boost**: Dragon Tales offers a limitless pool of stories, inspiring writers and fueling their creativity.
    - **Educational Tool**: It can be used to engage students in classrooms, making learning interactive and enjoyable.
    - **Reading Anytime, Anywhere**: With the 'Download' and 'Read Aloud' features, you can enjoy your unique stories wherever you go, even without internet access.
    """)

    st.markdown("## Motivation 💡")
    st.markdown("""
    Our main motivation behind this project was to create a tool that makes reading and writing more accessible and enjoyable. We wanted to provide a platform where anyone can generate a unique story and delve into an adventure with just a click of a button.
    """)

    st.markdown("## Future Improvements 💼")
    st.markdown("""
    We are always looking to improve and add new features to Dragon Tales. If you have any suggestions or feedback, feel free to reach out to us!
    """)
    st.write("\n\nMade with :heart: by **Team ⚡Inevitables**")
    st.markdown("Made for **ATLAS Madness Hackathon by Google Cloud and MongoDB ,2023**")
if __name__ == '__main__':
    app()
