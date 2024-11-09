import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
# Access the API key using the variable name defined in the .env file
key = os.getenv("openai_api_key_squal_lobby")




client = OpenAI(api_key=key)


# Caching function to generate scenario text from OpenAI
@st.cache_data
def generate_scenario():
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a HBCU fiction author popular with students, passionate about real-world finance lessons. You are part of the 'Breaking the Piggy Bank' event. Be helpful and kind. This is for CS students, so use emojis when needed."
            },
            {
                "role": "user",
                "content": "My car broke down, and I need to spend money out of pocket to fix it. I need to know how much to allocate from my paycheck to pay off repairs. Describe an enticing choice between instant gratification vs. delayed gratification without giving budgetary advice, making it hard for the student to choose."
            }
        ],
        model="gpt-4o-mini",
    )
    return chat_completion.choices[0].message.content

# Caching function to generate an image from DALL-E
@st.cache_data
def generate_image(scenario):
    response = client.images.generate(
        model="dall-e-3",
        prompt=f"Generate an image for a Capital One CS hackathon: {scenario}. Depict diverse HBCU students in blue and gold school colors.",
        size="1024x1024",
        quality="standard",
        n=1,
    )
    return response.data[0].url

# Function to get feedback based on user input
def get_feedback(user_input):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a Capital One budget virtual assistant for the 'Breaking the Piggy Bank' event. Be helpful and kind. Use emojis, show dollars, cents, and calculations for a year’s budget, with a good and bad example."
            },
            {
                "role": "user",
                "content": f"Evaluate the student's response based on '{user_input}' and provide constructive feedback, making it fun."
            }
        ],
        model="gpt-4o-mini",
    )
    return chat_completion.choices[0].message.content

# Initialize Streamlit app layout
st.set_page_config(page_title="Squad Lobby", initial_sidebar_state="auto")
st.header("Scenario Four: Car problems", divider='red')

# Use session state to store scenario and image URL so they don’t change after submission
if "scenario" not in st.session_state:
    st.session_state["scenario"] = generate_scenario()

if "image_url" not in st.session_state:
    st.session_state["image_url"] = generate_image(st.session_state["scenario"])

# Display the scenario and image from session state
st.image(st.session_state["image_url"])
st.markdown(st.session_state["scenario"])


# Get user input for scenario response
whatiwoulddo = st.text_input("Tell us what you would do in this scenario and we will provide feedback.")
if st.button("Submit"):
    with st.spinner("Gathering Budgeting Advice..."):
        response = get_feedback(whatiwoulddo)
        st.markdown(response)


code = """
import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
key = os.getenv("openai_api_key_squad_lobby")

# Initialize OpenAI client
client = OpenAI(api_key=key)

# Caching function to generate scenario text from OpenAI
@st.cache_data
def generate_scenario():
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a HBCU fiction author popular with students, passionate about real-world finance lessons. You are part of the 'Breaking the Piggy Bank' event. Be helpful and kind. This is for CS students, so use emojis when needed."
            },
            {
                "role": "user",
                "content": "My car broke down, and I need to spend money out of pocket to fix it. I need to know how much to allocate from my paycheck to pay off repairs. Describe an enticing choice between instant gratification vs. delayed gratification without giving budgetary advice, making it hard for the student to choose."
            }
        ],
        model="gpt-4o-mini",
    )
    return chat_completion.choices[0].message.content

# Caching function to generate an image from DALL-E
@st.cache_data
def generate_image(scenario):
    response = client.images.generate(
        model="dall-e-3",
        prompt=f"Generate an image for a Capital One CS hackathon: {scenario}. Depict diverse HBCU students in blue and gold school colors.",
        size="1024x1024",
        quality="standard",
        n=1,
    )
    return response.data[0].url

# Function to get feedback based on user input
def get_feedback(user_input):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a Capital One budget virtual assistant for the 'Breaking the Piggy Bank' event. Be helpful and kind. Use emojis, show dollars, cents, and calculations for a year’s budget, with a good and bad example."
            },
            {
                "role": "user",
                "content": f"Evaluate the student's response based on '{user_input}' and provide constructive feedback, making it fun."
            }
        ],
        model="gpt-4o-mini",
    )
    return chat_completion.choices[0].message.content

# Initialize Streamlit app layout
st.set_page_config(page_title="Squad Lobby", initial_sidebar_state="auto")
st.header("Scenario Four: Car problems", divider='red')

# Use session state to store scenario and image URL so they don’t change after submission
if "scenario" not in st.session_state:
    st.session_state["scenario"] = generate_scenario()

if "image_url" not in st.session_state:
    st.session_state["image_url"] = generate_image(st.session_state["scenario"])

# Display the scenario and image from session state
st.markdown(st.session_state["scenario"])
st.image(st.session_state["image_url"])

# Get user input for scenario response
whatiwoulddo = st.text_input("Tell us what you would do in this scenario and we will provide feedback.")
if st.button("Submit"):
    with st.spinner("Gathering Budgeting Advice..."):
        response = get_feedback(whatiwoulddo)
        st.markdown(response)
        """
st.code(code, language = "python")
