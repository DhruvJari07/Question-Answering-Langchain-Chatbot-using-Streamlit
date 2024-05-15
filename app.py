import streamlit as st
from langchain_community.llms import HuggingFaceEndpoint
import os
from dotenv import load_dotenv

load_dotenv()

Huggingface_api = os.getenv("Huggingface_api")

# Set the app's title
st.title('🦜🔗 Quickstart App')


# Function to generate a response using the OpenAI model from LangChain
def generate_response(input_text):
  repo_id = "mistralai/Mistral-7B-Instruct-v0.2"
  llm = HuggingFaceEndpoint(repo_id=repo_id, huggingfacehub_api_token=Huggingface_api, temperature=0.3)
  st.info(llm.invoke(input_text))

# Creating a form for user input
with st.form('my_form'):

  # Text area for users to enter their query
  text = st.text_area('Enter your question:', placeholder = 'Input your question here', height=100)

  # Button to submit the form
  submitted = st.form_submit_button('Submit')

  # Warning message if the API key is not entered correctly
  # if not openai_api_key.startswith('sk-'):
  #   st.warning('Please enter your OpenAI API key!', icon='⚠')

  # Processing the form submission and generating a response
  if submitted: # and openai_api_key.startswith('sk-'):
    generate_response(text)