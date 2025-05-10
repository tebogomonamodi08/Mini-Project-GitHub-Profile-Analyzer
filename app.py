# app.py

import streamlit as st
import plotly.express as px
from github_analyzer import fetch_user_repos, extract_languages

st.set_page_config(page_title="GitHub Language Visualizer", layout="centered")

st.title("🐙 GitHub Language Visualizer")

username = st.text_input("Enter GitHub Username")

if username:
    try:
        repos = fetch_user_repos(username)
        languages = extract_languages(repos)

        st.success(f"Found {len(repos)} repositories for user **{username}**.")

        if languages:
            st.subheader("Most Used Languages")
            fig = px.pie(
                names=list(languages.keys()),
                values=list(languages.values()),
                title="Languages Distribution"
            )
            st.plotly_chart(fig)
        else:
            st.warning("No language data found.")

    except ValueError as e:
        st.error(str(e))