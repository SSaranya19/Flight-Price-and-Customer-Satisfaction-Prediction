import streamlit as st

# Set page config
st.set_page_config(page_title="Flight Price and  Customer Satisfaction Prediction", page_icon="✈️", layout="wide")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["Home", "Flight Price Prediction", "Customer Satisfaction Analysis"])

# Display the selected page
if page == "Home":
    st.title("Welcome to the Flight Price and  Customer Satisfaction Prediction App! 🎯")
    st.write("Use the sidebar to navigate between pages.")

elif page == "Flight Price Prediction":
    exec(open("Flight-Price-Prediction.py", encoding="utf-8").read()) 

elif page == "Customer Satisfaction Analysis":
    exec(open("customer_satisfaction.py", encoding="utf-8").read())
