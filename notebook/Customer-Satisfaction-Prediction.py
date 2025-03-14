import streamlit as st
import pandas as pd
import joblib # type: ignore
import matplotlib.pyplot as plt
import seaborn as sns

# Load the best-performing model
model_best = joblib.load("xgboost.pkl")  # Assuming XGBoost performed the best

# Load dataset for visualizations
df = pd.read_csv(r"D:\GUVI-DS\Mini-Project4\Passenger_Satisfaction.csv")

# Streamlit UI Design
st.title("🛫 Smart Customer Satisfaction Prediction App 🌟")

# Tabs for Trends and Prediction
tab1, tab2 = st.tabs(["📊 Trends", "🔮 Prediction"])

with tab1:
    st.subheader("📈 Customer Satisfaction Trends")

    # Satisfaction distribution plot
    fig, ax = plt.subplots()
    sns.countplot(data=df, x='satisfaction', ax=ax, palette='coolwarm')
    ax.set_title("Satisfaction Distribution")
    st.pyplot(fig)

    # Age distribution by satisfaction
    fig, ax = plt.subplots()
    sns.boxplot(data=df, x='satisfaction', y='Age', ax=ax, palette='coolwarm')
    ax.set_title("Age Distribution by Satisfaction")
    st.pyplot(fig)

    # Flight Distance vs Satisfaction
    fig, ax = plt.subplots()
    sns.histplot(data=df, x='Flight Distance', hue='satisfaction', kde=True, ax=ax, palette='coolwarm')
    ax.set_title("Flight Distance vs Satisfaction")
    st.pyplot(fig)

    # Gender Distribution
    fig, ax = plt.subplots()
    sns.countplot(data=df, x='Gender', hue='satisfaction', ax=ax, palette='coolwarm')
    ax.set_title("Gender Distribution by Satisfaction")
    st.pyplot(fig)

with tab2:
    st.sidebar.title("⚙️ User Input Features")

    # User Input Features
    gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
    customer_type = st.sidebar.selectbox("Customer Type", ["Loyal Customer", "Disloyal Customer"])
    type_of_travel = st.sidebar.selectbox("Type of Travel", ["Business travel", "Personal travel"])
    travel_class = st.sidebar.selectbox("Class", ["Eco", "Eco Plus", "Business"])
    age = st.sidebar.slider("Age", min_value=1, max_value=100, value=30)
    flight_distance = st.sidebar.slider("Flight Distance", min_value=0, max_value=10000, value=500)
    total_delay = st.sidebar.slider("Total Delay (mins)", min_value=0, max_value=1000, value=10)
    ease_online_booking = st.sidebar.slider("Ease of Online Booking", min_value=0, max_value=5, value=3)
    inflight_wifi_service = st.sidebar.slider("Inflight Wi-Fi Service", min_value=0, max_value=5, value=3)
    inflight_entertainment = st.sidebar.slider("Inflight Entertainment", min_value=0, max_value=5, value=3)
    departure_arrival_time = st.sidebar.slider("Departure/Arrival Time", min_value=0, max_value=5, value=3)
    seat_comfort = st.sidebar.slider("Seat Comfort", min_value=0, max_value=5, value=3)
    cleanliness = st.sidebar.slider("Cleanliness", min_value=0, max_value=5, value=3)
    baggage_handling = st.sidebar.slider("Baggage Handling", min_value=0, max_value=5, value=3)
    checkin_service = st.sidebar.slider("Check-in Service", min_value=0, max_value=5, value=3)
    gate_location = st.sidebar.slider("Gate Location", min_value=0, max_value=5, value=3)
    food_drink = st.sidebar.slider("Food and Drink", min_value=0, max_value=5, value=3)
    onboard_service = st.sidebar.slider("On-board Service", min_value=0, max_value=5, value=3)
    leg_room_service = st.sidebar.slider("Leg Room Service", min_value=0, max_value=5, value=3)
    online_boarding = st.sidebar.slider("Online boarding", min_value=0, max_value=5, value=3)
    inflight_service = st.sidebar.slider("Inflight Service", min_value=0, max_value=5, value=3)

    # Create feature data for prediction
    user_data = pd.DataFrame({
        "Age": [age],
        "Flight Distance": [flight_distance],
        "Inflight wifi service": [inflight_wifi_service],
        "Departure/Arrival time convenient": [departure_arrival_time],
        "Ease of Online booking": [ease_online_booking],
        "Gate location": [gate_location],
        "Food and drink": [food_drink],
        "Online boarding": [online_boarding],
        "Seat comfort": [seat_comfort],
        "Inflight entertainment": [inflight_entertainment],
        "On-board service": [onboard_service],
        "Leg room service": [leg_room_service],
        "Baggage handling": [baggage_handling],
        "Checkin service": [checkin_service],
        "Inflight service": [inflight_service],
        "Cleanliness": [cleanliness],
        "Total Delay": [total_delay],
        "Gender_Male": [1 if gender == "Male" else 0],
        "Customer Type_disloyal Customer": [1 if customer_type == "Disloyal Customer" else 0],
        "Type of Travel_Personal Travel": [1 if type_of_travel == "Personal travel" else 0],
        "Class_Eco": [1 if travel_class == "Eco" else 0],
        "Class_Eco Plus": [1 if travel_class == "Eco Plus" else 0]
    })

    # Align feature order to match model expectations
    required_features = model_best.get_booster().feature_names
    user_data = user_data.reindex(columns=required_features, fill_value=0)

    # Prediction logic
    if st.sidebar.button("Predict Satisfaction"):
        prediction = model_best.predict(user_data)

        # Display prediction
        satisfaction_result = "😊 Satisfied" if prediction[0] == 1 else "😐 Neutral/Unhappy"
        st.subheader(f"Prediction Result: {satisfaction_result}")