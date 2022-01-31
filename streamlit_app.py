import streamlit as st
import requests

"""
# Clear Daily Checklist
"""


with st.echo(code_location='below'):     

    def clear_daily():
        
        url = "https://api.notion.com/v1/databases/9cd756f45c024073a905ad528e75c75c/query"

        payload = {"page_size": 100}
        headers = {
            "Accept": "application/json",
            "Notion-Version": "2021-08-16",
            "Content-Type": "application/json",
            "Authorization": "Bearer secret_bbkXQFbGmg9G8hqXxzPPc4QMwAv1mmFQgoRDfSC7jfx"
        }

        response = requests.request("POST", url, json=payload, headers=headers)

        st.write(response.text)
        
    st.button("Clear daily checklist", on_click=clear_daily)
