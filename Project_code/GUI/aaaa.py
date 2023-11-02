import streamlit as st

page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1501426026826-31c667bdf23d");
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)
st.title("AI Detector")