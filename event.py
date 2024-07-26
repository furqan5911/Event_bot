import streamlit as st
import os


import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown

API_KEY = "AIzaSyD4fcsx2GHbl4WNWgPkoJLof7uxmDf66MY"
genai.configure(api_key=API_KEY)
 
st.set_page_config(page_title="Q&A Demo")

st.header("Gemini Chat BOT")

# Initialize session state for chat history if it doesn't exist
if 'messages' not in st.session_state:
    st.session_state['messages'] = []

# Tech events data
data = [
    {
        "event": "Lahore Tech Summit 2024",
        "location": "Lahore International Expo Centre",
        "date": "August 5, 2024",
        "duration": "2 days",
        "speaker": "Dr. Sarah Khan",
        "expertise": "AI and Machine Learning"
    },
    {
        "event": "Karachi IT Expo 2024",
        "location": "Karachi Expo Centre",
        "date": "September 10, 2024",
        "duration": "3 days",
        "speaker": "Ahmed Ali",
        "expertise": "CEO of Tech Innovations Inc."
    },
    {
        "event": "Islamabad Cyber Security Conference",
        "location": "Islamabad Convention Centre",
        "date": "July 20, 2024",
        "duration": "1 day",
        "speaker": "Brigadier Imran Haider",
        "expertise": "Cyber Security Specialist"
    },
    {
        "event": "Future Tech Forum Lahore",
        "location": "Pearl Continental Hotel Lahore",
        "date": "October 15, 2024",
        "duration": "2 days",
        "speaker": "Ayesha Malik",
        "expertise": "Data Science Evangelist"
    },
    {
        "event": "AI and Robotics Summit Karachi",
        "location": "Marriott Hotel Karachi",
        "date": "November 25, 2024",
        "duration": "1 day",
        "speaker": "Dr. Faisal Mustafa",
        "expertise": "Robotics Engineer"
    }
]

# Function to interact with your model and get responses
def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text

# Display previous messages
for message in st.session_state['messages']:
    role = message["role"]
    content = message["content"]
    with st.chat_message(role):
        st.markdown(content)

# Chat input
prompt = st.chat_input("You:")

# Handle user input
if prompt:
    # Store user message in a variable named 'chat'
    chat = f"""
    You are a chat bot who has details about all the events given in the data variable. 
    You need to reply based on the data  Data: {data} when a user asks any query related to the event. 
    If the user's query is outside the event-related query, respond that you have no information about it. 
    Otherwise, give a response to the user related to their query.

   

    User query: {prompt}
    """

    # Add user message to session state
    st.session_state['messages'].append({"role": "user", "content": prompt})

    # Get response from Gemini model
    response = get_gemini_response(chat)

    # Add assistant message to session state
    st.session_state['messages'].append({"role": "assistant", "content": response})

    # Display user and assistant messages using st.chat_message
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        st.markdown(response)
