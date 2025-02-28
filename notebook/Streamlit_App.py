import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

# Loading the trained model
@st.cache_resource
def load_model():
    with open('Gradient Boosting_pipeline.pkl', 'rb') as f:
        model = pickle.load(f)
    return model

# Loading the dataset (for visualization)
@st.cache_data
def load_data():
    data = pd.read_csv(r'D:\GUVI-DS\Mini-Project4\Cleaned.csv')
    return data

# Function to predict flight price
def predict_price(model, input_data):
    prediction = model.predict(input_data)
    return prediction[0]

# Streamlit app
def main():
    st.title("Flight Price Prediction App ✈️")
    st.write("Explore flight price trends and predict prices based on your inputs.")

    # Load data and model
    data = load_data()
    model = load_model()

    # Sidebar for user inputs
    st.sidebar.header("User Inputs")
    st.sidebar.write("Filter data and predict flight prices.")

    # Filter data by route, airline, and time
    st.sidebar.subheader("Filter Data")
    airline = st.sidebar.selectbox("Select Airline", data['Airline'].unique())
    source = st.sidebar.selectbox("Select Source City", data['Source'].unique())
    destination = st.sidebar.selectbox("Select Destination City", data['Destination'].unique())
    month = st.sidebar.slider("Select Journey Month", 1, 12, 6)
    day = st.sidebar.slider("Select Journey Day", 1, 31, 15)

    # Filtered data for visualization
    filtered_data = data[
        (data['Airline'] == airline) &
        (data['Source'] == source) &
        (data['Destination'] == destination) &
        (data['Journey_Month'] == month) &
        (data['Journey_Day'] == day)
    ]

    # Display filtered data
    st.subheader("Filtered Flight Data")
    st.write(filtered_data)

    # Visualizations
    st.subheader("Flight Price Trends")
    fig, ax = plt.subplots(1, 2, figsize=(15, 5))

    # Price vs Duration
    sns.scatterplot(x='Duration_mins', y='Price', data=filtered_data, ax=ax[0])
    ax[0].set_title("Price vs Duration")
    ax[0].set_xlabel("Duration (Minutes)")
    ax[0].set_ylabel("Price")

    # Price vs Airline
    sns.boxplot(x='Airline', y='Price', data=filtered_data, ax=ax[1])
    ax[1].set_title("Price by Airline")
    ax[1].set_xlabel("Airline")
    ax[1].set_ylabel("Price")
    plt.xticks(rotation=45)

    st.pyplot(fig)

    # Prediction Section
    st.sidebar.subheader("Predict Flight Price")
    st.sidebar.write("Enter details to predict flight price.")

    # User inputs for prediction
    dep_hour = st.sidebar.slider("Departure Hour", 0, 23, 12)
    dep_minute = st.sidebar.slider("Departure Minute", 0, 59, 30)
    arrival_hour = st.sidebar.slider("Arrival Hour", 0, 23, 14)
    arrival_minute = st.sidebar.slider("Arrival Minute", 0, 59, 45)
    duration_mins = st.sidebar.number_input("Duration (Minutes)", min_value=0, value=120)
    stops = st.sidebar.selectbox("Total Stops", [0, 1, 2, 3, 4])
    additional_info = st.sidebar.selectbox("Additional Info", data['Additional_Info'].unique())

    # Create input DataFrame for prediction
    input_data = pd.DataFrame([{
        'Journey_Month': month,
        'Journey_Day': day,
        'Dep_Hour': dep_hour,
        'Dep_Minute': dep_minute,
        'Arrival_Hour': arrival_hour,
        'Arrival_Minute': arrival_minute,
        'Duration_mins': duration_mins,
        'Price_per_minute': 0.5,  # Example value, replace with actual logic if needed
        'Airline_encoded': airline,  # Replace with encoded value
        'Source_encoded': source,  # Replace with encoded value
        'Destination_encoded': destination,  # Replace with encoded value
        'Total_Stops_encoded': stops,
        'Additional_Info_encoded': additional_info,  # Replace with encoded value
        'Route_1_encoded': 0,  # Replace with actual logic if needed
        'Route_2_encoded': 0,
        'Route_3_encoded': 0,
        'Route_4_encoded': 0,
        'Route_5_encoded': 0,
        'Route_6_encoded': 0
    }])

    # Predict flight price
    if st.sidebar.button("Predict Price"):
        predicted_price = predict_price(model, input_data)
        st.sidebar.success(f"Predicted Flight Price: ₹{predicted_price:.2f}")

# Run the app
if __name__ == "__main__":
    main()