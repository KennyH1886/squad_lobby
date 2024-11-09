import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
# Access the API key using the variable name defined in the .env file
key = os.getenv("openai_api_key_squal_lobby")

# Initialize OpenAI client
client = OpenAI(api_key=key)

st.set_page_config(page_title="Squad Lobby", initial_sidebar_state="auto")
st.header("Scenario One: GHOE Cruise 2025", divider='red')

# Caching scenario and image URL using session state
if "scenario" not in st.session_state:
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a HBCU fiction author popular with students, with a passion for real-world finance lessons. You are part of the 'Breaking the Piggy Bank' event. Be helpful and kind. This is for CS students, so use emojis when needed."
            },
            {
                "role": "user",
                "content": "There is a 'Greatest Homecoming on Earth' cruise happening at an HBCU, and a student wants to budget for the trip but usually spends all their money partying. The student really wants to take this senior trip. Describe a scenario that presents an enticing choice between instant gratification and delayed gratification, without giving budgetary advice. Make it hard for the student to choose."
            }
        ],
        model="gpt-4o-mini",
    )
    st.session_state["scenario"] = chat_completion.choices[0].message.content

if "image_url" not in st.session_state:
    response = client.images.generate(
        model="dall-e-3",
        prompt=f"Generate an image for a Capital One CS hackathon for the scenario: {st.session_state['scenario']}. Depict diverse HBCU students in blue and gold school colors.",
        size="1024x1024",
        quality="standard",
        n=1,
    )
    st.session_state["image_url"] = response.data[0].url

# Display the scenario and image from session state
with st.spinner("Gathering scenario..."):
    st.image(st.session_state["image_url"])
    st.markdown(st.session_state["scenario"])


# Get user input for scenario response
whatiwoulddo = st.text_input("Tell us what you would do in this scenario and we will provide feedback.")
if st.button("Submit"):
    with st.spinner("Gathering Budgeting Advice..."):
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a Capital One budget virtual assistant for the 'Breaking the Piggy Bank' event. Be helpful and kind. This is for CS students, so use emojis when needed. Show dollars, cents, numbers, and calculations for a year's budget, always with a very good and very bad example."
                },
                {
                    "role": "user",
                    "content": f"Evaluate the student's response based on '{whatiwoulddo}' and provide constructive feedback, making it fun."
                }
            ],
            model="gpt-4o-mini",
        )
        response = chat_completion.choices[0].message.content
        st.markdown(response)

# Display code in Streamlit
code = """
import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("openai_api_key_squal_lobby")
client = OpenAI(api_key=key)

st.set_page_config(page_title="Squad Lobby", initial_sidebar_state="auto")
st.header("Scenario One: GHOE Cruise 2025", divider='red')

if "scenario" not in st.session_state:
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a HBCU fiction author..."},
            {"role": "user", "content": "A student wants to budget for the GHOE cruise..."}
        ],
        model="gpt-4o-mini",
    )
    st.session_state["scenario"] = chat_completion.choices[0].message.content

if "image_url" not in st.session_state:
    response = client.images.generate(
        model="dall-e-3",
        prompt=f"Generate an image for Capital One hackathon: {st.session_state['scenario']}...",
        size="1024x1024",
        quality="standard",
        n=1,
    )
    st.session_state["image_url"] = response.data[0].url

st.markdown(st.session_state["scenario"])
st.image(st.session_state["image_url"])

whatiwoulddo = st.text_input("Tell us what you would do...")
if st.button("Submit"):
    with st.spinner("Gathering Budgeting Advice..."):
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a Capital One budget virtual assistant..."},
                {"role": "user", "content": f"Evaluate based on {whatiwoulddo}."}
            ],
            model="gpt-4o-mini",
        )
        response = chat_completion.choices[0].message.content
        st.markdown(response)
"""
st.code(code, language="python")
