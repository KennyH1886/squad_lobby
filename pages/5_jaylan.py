import streamlit as st
import streamlit as st
from openai import OpenAI
import time
import base64
from io import BytesIO
import os
from dotenv import load_dotenv



# st.write(password)
# Load environment variables from .env file
load_dotenv()

# Access the API key using the variable name defined in the .env file
key = os.getenv("openai_api_key_squal_lobby")




client = OpenAI(api_key=key)

st.set_page_config(page_title="Squad Lobby",  initial_sidebar_state="auto")
st.header("Spring Break Vacay", divider = 'red')

with st.spinner("Generating scenario..."):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a HBCU fiction author thats popular with the students with a passion for real world finance lessons through your content. You are part of the 'Breaking the Piggy Bank, Reviving Personal Budgeting in the Virtual World' event. Be helpful and kind. This is for CS students, so use emojis when needed. "
            },
            {
                "role": "user",
                "content": f" A group of friends that attend North Carolina A&T are planning a Spring Break trip to Turks and Caicos. They have been planning this trip out a year in advance. Please give a great scenario for this with emojis. dont give budgetary advice just describe a very enticing advice for instant gradificaiton versus delayed , make it very hard for the student to choose"
            }
        ],
        model="gpt-4o-mini",
    )
    scenario = chat_completion.choices[0].message.content
    
    
    response = client.images.generate(
            model="dall-e-3",
            prompt=f"generate an image for a captial one cs hackathon, for the following scenario {scenario}. Make sure diverse HBCU student are depicted in the image with blue and gold school colors.",
            size="1024x1024",
            quality="standard",
            n=1,
            )
    image_url = response.data[0].url
    st.image(image_url)
    
    
    
    st.markdown(scenario)





# st.image('squad-lobby-logo3.png')

whatiwoulddo = st.text_input("tell us what you would do in this scenario and we will provide feedback.")
if st.button("Submit"):
    
    
    
    with st.spinner("Gathering Budgeting Advice..."):
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a Capital One budget virtual assistant. You are part of the 'Breaking the Piggy Bank, Reviving Personal Budgeting in the Virtual World' event. Be helpful and kind. This is for CS students, so use emojis when needed. make sure oyu show dollars and cents , numbers and calculations for a years worth of budgeting , always show a very good and very bad example."
                },
                {
                    "role": "user",
                    "content": f"evaluate the student response based on {whatiwoulddo} give constructive feedback but still make it fun."
                }
            ],
            model="gpt-4o-mini",
        )
        response = chat_completion.choices[0].message.content
        st.markdown(response)



code = """
import streamlit as st
import streamlit as st
from openai import OpenAI
import time
import base64
from io import BytesIO
import os
from dotenv import load_dotenv



# st.write(password)
# Load environment variables from .env file
load_dotenv()

# Access the API key using the variable name defined in the .env file
key = os.getenv("openai_api_key_squal_lobby")




client = OpenAI(api_key=key)

st.set_page_config(page_title="Squad Lobby",  initial_sidebar_state="auto")
st.header("Scenario One: GHOE Cruise 2025", divider = 'red')

with st.spinner("Generating scenario..."):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a HBCU fiction author thats popular with the students with a passion for real world finance lessons through your content. You are part of the 'Breaking the Piggy Bank, Reviving Personal Budgeting in the Virtual World' event. Be helpful and kind. This is for CS students, so use emojis when needed. "
            },
            {
                "role": "user",
                "content": f"there is a greatest homecoming on earth cruise happening at an hbcu and a student wants to budget his trip but usually spends all their money partying but really wants ot take this senior trip. Please give a great scenario for this with emojis. dont give budgetary advice just describe a very enticing advice for instant gradificaiton versus delayed , make it very hard for the student to choose"
            }
        ],
        model="gpt-4o-mini",
    )
    scenario = chat_completion.choices[0].message.content
    
    
    response = client.images.generate(
            model="dall-e-3",
            prompt=f"generate an image for a captial one cs hackathon, for the following scenario {scenario}. Make sure diverse HBCU student are depicted in the image with blue and gold school colors.",
            size="1024x1024",
            quality="standard",
            n=1,
            )
    image_url = response.data[0].url
    st.image(image_url)
    
    
    
    st.markdown(scenario)





# st.image('squad-lobby-logo3.png')

whatiwoulddo = st.text_input("tell us what you would do in this scenario and we will provide feedback.")
if st.button("Submit"):
    
    
    
    with st.spinner("Gathering Budgeting Advice..."):
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a Capital One budget virtual assistant. You are part of the 'Breaking the Piggy Bank, Reviving Personal Budgeting in the Virtual World' event. Be helpful and kind. This is for CS students, so use emojis when needed. make sure oyu show dollars and cents , numbers and calculations for a years worth of budgeting , always show a very good and very bad example."
                },
                {
                    "role": "user",
                    "content": f"evaluate the student response based on {whatiwoulddo} give constructive feedback but still make it fun."
                }
            ],
            model="gpt-4o-mini",
        )
        response = chat_completion.choices[0].message.content
        st.markdown(response)



"""
st.code(code, language = "python")
