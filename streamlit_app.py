import streamlit as st
import requests

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""


with st.echo(code_location='below'):     
    result = st.button("Clear daily checklist")
    
    if result:
        st.write("starting")

        url = "https://api.notion.com/v1/databases/496f4943fe29407098c94d5b7b4e8ce4"
        
        payload = {"properties": {"Done": {"title": [{"checkbox": {"content": 0}}]}}}
        st.write(payload)
        headers = {
            "Accept": "application/json",
            "Notion-Version": "2021-08-16",
            "Content-Type": "application/json",
            "Authorization": "Bearer secret_bbkXQFbGmg9G8hqXxzPPc4QMwAv1mmFQgoRDfSC7jfx"
        }
        st.write(headers)
        response = requests.request("PATCH", url, json=payload, headers=headers)

        st.write(response.text)
        
