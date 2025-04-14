import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import warnings

# Suppress warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)

# Streamlit App Title
st.title("✈️ Flight Price Prediction")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("feature.csv", low_memory=False)
    return df

try:
    df_cleaned = load_data()
    
    # Extract airline names from one-hot encoded columns
    airlines = ["Air Asia", "Air India", "GoAir", "IndiGo", "Jet Airways", "Jet Airways Business", 
                "Multiple carriers", "Multiple carriers Premium economy", "SpiceJet", "Trujet", "Vistara", "Vistara Premium economy"]
    sources = sorted(["Banglore", "Chennai", "Delhi", "Kolkata", "Mumbai"])
    destinations = sorted(["Cochin", "Delhi", "Hyderabad", "Kolkata", "New Delhi"])
    total_stops_options = sorted(["0", "1", "2", "3", "4"])
    
    # Load the trained model
    @st.cache_resource
    def load_model():
        with open("Gradient Boosting_model.pkl", "rb") as model_file:
            return pickle.load(model_file)
    
    model = load_model()
    expected_features = df_cleaned.drop(columns=["Price"]).columns
except Exception as e:
    st.error(f"Error loading data or model: {e}")
    st.stop()

# Sidebar for input selection
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3125/3125713.png", width=100)
    st.markdown("## 🛫 Flight Parameters")
    
    with st.expander("✈️ Flight Details", expanded=True):
        airline = st.selectbox("Airline", airlines)
        source = st.selectbox("Source", sources)
        valid_destinations = [d for d in destinations if d != source]
        destination = st.selectbox("Destination", valid_destinations)
        stops = st.selectbox("Total Stops", total_stops_options)
    
    with st.expander("📅 Date & 🕒 Time Details", expanded=True):
        today = datetime.now()
        journey_month = st.slider("Month", 1, 12, today.month)
        journey_day = st.slider("Day", 1, 31, today.day)
        dep_hour = st.slider("Departure Hour", 0, 23, 12)
        dep_minute = st.slider("Departure Minute", 0, 59, 30)
        arr_hour = st.slider("Arrival Hour", 0, 23, 15)
        arr_minute = st.slider("Arrival Minute", 0, 59, 45)
        duration_mins = st.sidebar.number_input("Flight Duration (in mins)", 30, 1440, 120)
        price_per_minute = st.sidebar.number_input("Price per Minute", 1, 500, 10)
    
    st.markdown("---")

# Prepare data for prediction
def prepare_prediction_data():
    test_data = pd.DataFrame({
        "Journey_Month": [journey_month],
        "Journey_Day": [journey_day],
        "Dep_Hour": [dep_hour],
        "Dep_Minute": [dep_minute],
        "Arrival_Hour": [arr_hour],
        "Arrival_Minute": [arr_minute],
        "Duration_mins": [duration_mins],
        "Price_per_minute": [price_per_minute],
        "Total_Stops": [stops]
    })
    
    # One-hot encode airlines
    for a in airlines:
        test_data[a] = [1 if a == airline else 0]
    
    # One-hot encode sources and destinations
    for s in sources:
        test_data[f"Source_{s}"] = [1 if s == source else 0]
    
    for d in destinations:
        test_data[f"Destination_{d}"] = [1 if d == destination else 0]

    # Initialize Route columns
    for i in range(1, 6):  # For Route1 to Route5
        test_data[f"Route{i}"] = [0]  # Initialize with 0 (you may need to implement specific logic here)
    
    # Ensure the columns match the expected features of the model
    test_data = test_data.reindex(columns=model.feature_names_in_, fill_value=0)
    
    return test_data

# Tabs layout
tabs = st.tabs(["📊 Flight Price Trends & Analysis", "✈️ Flight Price Prediction"])

# Flight Price Trends & Analysis Tab
with tabs[0]:
    st.subheader("📊 Flight Price Trends & Analysis")
    fig, axes = plt.subplots(4, 2, figsize=(20, 18))
    fig.subplots_adjust(hspace=0.8, wspace=0.4)
    fig.suptitle("Flight Price Trends", fontsize=18, fontweight='bold')

    # Price Distribution by Stops
    sns.barplot(x='Total_Stops', y='Price', data=df_cleaned, ax=axes[0, 0])
    axes[0, 0].set_title('Price by Stops')

    # Monthly Price Trends
    monthly_avg_price = df_cleaned.groupby('Journey_Month')['Price'].mean()
    axes[0, 1].plot(monthly_avg_price.index, monthly_avg_price.values, marker='o')
    axes[0, 1].set_title('Monthly Price Trends')

    # Price vs Duration
    sns.scatterplot(x='Duration_mins', y='Price', data=df_cleaned, ax=axes[1, 0])
    axes[1, 0].set_title('Price vs. Duration')

    # Price Heatmap (Month vs. Day)
    heatmap_data = df_cleaned.pivot_table(index='Journey_Month', columns='Journey_Day', values='Price', aggfunc='mean')
    sns.heatmap(heatmap_data, cmap='YlOrRd', annot=True, fmt=".0f", ax=axes[1, 1])
    axes[1, 1].set_title('Price Heatmap (Month vs. Day)')

    # Price Distribution by Source & Destination
    source_dest_price = df_cleaned.groupby(['Source', 'Destination'])['Price'].mean().reset_index()
    sns.barplot(x='Source', y='Price', hue='Destination', data=source_dest_price, ax=axes[2, 0])
    axes[2, 0].set_title('Price by Source & Destination')

    # Price Trends by Day of the Month
    daily_avg_price = df_cleaned.groupby('Journey_Day')['Price'].mean()
    axes[2, 1].plot(daily_avg_price.index, daily_avg_price.values, marker='o')
    axes[2, 1].set_title('Daily Price Trends')

    # Price Distribution Over Different Airlines
    sns.barplot(x='Airline', y='Price', data=df_cleaned, ax=axes[3, 0])
    axes[3, 0].set_title('Price Distribution by Airline')
    axes[3, 0].tick_params(axis='x', rotation=90)

    # Average Price by Airline
    avg_price_airline = df_cleaned.groupby('Airline')['Price'].mean()
    sns.barplot(x=avg_price_airline.index, y=avg_price_airline.values, ax=axes[3, 1])
    axes[3, 1].set_title('Avg Price by Airline')
    axes[3, 1].tick_params(axis='x', rotation=90)

    st.pyplot(fig)

# Flight Price Prediction Tab
with tabs[1]:
    st.subheader("✈️ Flight Price Prediction")

    # Prediction Button
    if st.button("🚀 Predict Flight Price", use_container_width=True, key="predict_btn"):
        with st.spinner("Calculating price..."):
            try:
                test_data_encoded = prepare_prediction_data()
                price = model.predict(test_data_encoded)[0]
            
                st.success(f"Predicted Price: ${price:.2f}")
                st.markdown(f"Estimated Price Range: ${price * 0.9:.2f} - ${price * 1.1:.2f}")
            except Exception as e:
                st.error(f"Error making prediction: {e}")
