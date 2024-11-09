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
st.header("Scenario One", divider = 'red')

response = client.images.generate(
        model="dall-e-3",
        prompt=f"generate an image for a captial one cs hackathon, depicting a diverse CS college student trying to decide how to spend or save money, decide between instant and delayed gratification. just captial one and ncat logos, no other text",
        size="1024x1024",
        quality="standard",
        n=1,
        )
image_url = response.data[0].url
st.image(image_url)


# st.image('squad-lobby-logo3.png')

question = st.text_input("Ask your questions for budget help!")
if st.button("Submit"):
    
    
    
    with st.spinner("Gathering Budgeting Advice..."):
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a Capital One budget virtual assistant. You are part of the 'Breaking the Piggy Bank, Reviving Personal Budgeting in the Virtual World' event. Be helpful and kind. This is for CS students, so use emojis when needed. "
                },
                {
                    "role": "user",
                    "content": f"{question}"
                }
            ],
            model="gpt-4o-mini",
        )
        response = chat_completion.choices[0].message.content
        st.markdown(response)