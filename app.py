import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page

st.set_page_config(layout = "wide")
page = st.sidebar.selectbox("Explore or Predict", ("Explore", "Predict"))

if page == "Explore":
    show_explore_page()
else:
    show_predict_page()