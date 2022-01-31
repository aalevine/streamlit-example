import streamlit as st
import requests

"""
# Clear Daily Checklist
"""


with st.echo(code_location='below'):     

    def clear_daily():
        
        url = "https://api.notion.com/v1/databases/496f4943fe29407098c94d5b7b4e8ce4"
        
        payload = {"properties": {"Done": {"checkbox": {"value": False}}}}

        headers = {
            "Accept": "application/json",
            "Notion-Version": "2021-08-16",
            "Content-Type": "application/json",
            "Authorization": "Bearer secret_mduk29ERIsnmXXmLrkwdy11c0G2DVdm9K2LTqohkBDH"
        }

        response = requests.request("PATCH", url, json=payload, headers=headers)

        st.write(response.text)
        
    st.button("Clear daily checklist", on_click=clear_daily)
