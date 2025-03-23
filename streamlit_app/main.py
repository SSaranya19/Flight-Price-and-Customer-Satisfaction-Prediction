import streamlit as st

# Set page config
st.set_page_config(page_title="Flight Price and Customer Satisfaction Prediction", page_icon="✈️", layout="wide")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["Home", "Flight Price Prediction", "Customer Satisfaction Analysis"])

# Display the selected page
if page == "Home":
    st.title("✈️ Welcome to the Flight Price and Customer Satisfaction Prediction App!")
    st.write("This app helps you predict flight prices and analyze customer satisfaction to make better travel decisions.")
    
    # Load and display a single image from URL
    image_url = (r"D:\GUVI-DS\Mini-Project4\flights.jpg")
    st.image(image_url, use_column_width=True)
    
    st.write("Use the sidebar to navigate between pages and explore the predictions!")

elif page == "Flight Price Prediction":
    exec(open("Flight-Price-Prediction.py", encoding="utf-8").read())

elif page == "Customer Satisfaction Analysis":
    exec(open("Customer-Satisfaction-Prediction.py", encoding="utf-8").read())
