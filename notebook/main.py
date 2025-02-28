import streamlit as st

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Flight Price Prediction", "Another App"])

# Display the selected page
if page == "Flight Price Prediction":
    st.sidebar.write("You are on the Flight Price Prediction page.")
elif page == "Another App":
    st.sidebar.write("You are on the Another App page.")

