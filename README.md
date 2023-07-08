# Dragon Tales - Short Story Generator 🐉📚

![Project Image](Dragon-tales.png)

Welcome to Dragon Tales, a powerful and user-friendly short story generator! 

Access the website here : [Dragon Tales](http://35.224.204.110/)
## Table of Contents

1. [About the Project](#about)
2. [Features](#features)
3. [Benefits](#benefits)
4. [Getting Started](#getting-started)
5. [Contributing](#contributing)

<a name="about"></a>
## About The Project

Dragon Tales uses the power of artificial intelligence to generate immersive and engaging short stories based on the genre selected by the user. With an elegant Streamlit UI, Dragon Tales offers a clean and simple interface for users to navigate through their stories, filter them based on genre, and even mark them as favorites for easy access later.

<a name="features"></a>
## Features

1. **Generate Short Stories** - Create unique short stories just with a click of a button.

2. **Filtering Capabilities** - Search and filter your generated stories by genre.

3. **Favourites** - Mark any story as your favourite for quick access in the future. Easily add and remove stories from your favorites.

4. **Read Aloud** - Generates an audio file to read the stories aloud.



<a name="benefits"></a>
## Benefits

- **Creativity Boost** - Dragon Tales offers a limitless pool of stories that can help inspire writers and fuel their creativity.

- **Educational Tool** - It can be used as a tool to engage students in classrooms, making learning more interactive and enjoyable.

- **Reading Anytime, Anywhere** - With the download and read aloud features, enjoy your unique stories wherever you go, even without internet access.

<a name="getting-started"></a>
## Getting Started

To get a local copy up and running, follow these steps:

1. Clone the repository
```sh
git clone https://github.com/your_username_/Project-Name.git
```
2. Install the required libraries mentioned in the `requirements.txt`
```sh
pip install -r requirements.txt
```
3. Run the Streamlit app
```sh
streamlit run Home.py
```
<a name="Design"></a>
## System Design

The entire system is divided into 2 microservices.
- The Front End Streamlit Python application
- The Back End Springboot Java application

The backend utilises the Open AI chatGPT API services and the power of MongoDB Atlas to provide a seamless experience to the user.

Where as the front end UI is powered by Streamlit UI and the entire communication is happening through the dedicated API service of Dragon Tales.

The entire microservices are deployed and manged by Google Cloud services and Google Kuberenetes Engine.


The entire API documentation is available at : [Dragon Tales API docs](https://mongo-gcp-project.uc.r.appspot.com/swagger-ui/index.html#)
<a name="contributing"></a>
## Contributing

We welcome contributions.

Happy Reading with Dragon Tales 📖!

Made by Team Inevitables