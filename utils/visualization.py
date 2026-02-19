import streamlit as st

def show_score_bar(score):
    st.progress(float(score))
