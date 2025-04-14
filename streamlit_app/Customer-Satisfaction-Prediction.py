import streamlit as st
import pandas as pd
import joblib # type: ignore
import matplotlib.pyplot as plt
import seaborn as sns


# === Streamlit UI Design ===
st.title("🛫 Customer Satisfaction Prediction App 🌟")

# === Function: Convert age to age group ===
def age_group(age):
    if age < 20:
        return "Teen"
    elif age < 35:
        return "Young Adult"
    elif age < 60:
        return "Adult"
    else:
        return "Senior"

# Age group encoding
age_group_mapping = {
    'Teen': 0,
    'Young Adult': 1,
    'Adult': 2,
    'Senior': 3
}

# === Load the trained model ===
model_best = joblib.load(r"D:\GUVI-DS\Mini-Project4\Class_model\Gradient_Boosting.pkl")

# === Load dataset for visualizations ===
df = pd.read_csv(r"D:\GUVI-DS\Mini-Project4\Passenger_Satisfaction.csv")

# === Tabs for Analysis and Prediction ===
tab1, tab2 = st.tabs(["📊 Flight Price Trends & Analysis", "🔮 Flight Price Prediction"])

# === Tab 1: Trend Analysis ===
with tab1:
    st.subheader("📈 Customer Satisfaction Trends")

    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    # Plot 1: Satisfaction distribution
    sns.countplot(data=df, x='satisfaction', ax=axes[0, 0], palette='coolwarm')
    axes[0, 0].set_title("Satisfaction Distribution")

    # Plot 2: Age distribution by satisfaction
    sns.boxplot(data=df, x='satisfaction', y='Age', ax=axes[0, 1], palette='coolwarm')
    axes[0, 1].set_title("Age Distribution by Satisfaction")

    # Plot 3: Flight Distance vs Satisfaction
    sns.histplot(data=df, x='Flight Distance', hue='satisfaction', kde=True, ax=axes[1, 0], palette='coolwarm')
    axes[1, 0].set_title("Flight Distance vs Satisfaction")

    # Plot 4: Gender distribution
    sns.countplot(data=df, x='Gender', hue='satisfaction', ax=axes[1, 1], palette='coolwarm')
    axes[1, 1].set_title("Gender Distribution by Satisfaction")

    plt.tight_layout()
    st.pyplot(fig)

# === Tab 2: Prediction ===
with tab2:
    st.sidebar.title("⚙️ User Input Features")

    # === Sidebar Inputs ===
    gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
    customer_type = st.sidebar.selectbox("Customer Type", ["Loyal Customer", "disloyal Customer"])
    travel_purpose = st.sidebar.selectbox("Travel Purpose", ["Business travel", "Personal Travel"])
    travel_class = st.sidebar.selectbox("Class", ["Business", "Eco", "Eco Plus"])
    age = st.sidebar.slider("Age", min_value=5, max_value=100, value=30)
    flight_distance = st.sidebar.slider("Flight Distance", 30, 5000, 500)
    total_delay = st.sidebar.slider("Total Delay (mins)", 0, 1000, 10)
    service_score = st.sidebar.slider("Service Score (0-5)", 0, 5, 4)

    # === Feature Engineering ===
    is_delayed = 1 if total_delay > 0 else 0
    age_group_label = age_group(age)
    age_group_encoded = age_group_mapping[age_group_label]

    # One-hot encode for categorical features
    gender_male = 1 if gender == "Male" else 0
    gender_female = 1 - gender_male

    customer_loyal = 1 if customer_type == "Loyal Customer" else 0
    customer_disloyal = 1 - customer_loyal

    # Travel Purpose + Class combined encoding
    travel_classes = [
        "Business travel - Business",
        "Business travel - Eco",
        "Business travel - Eco Plus",
        "Personal Travel - Business",
        "Personal Travel - Eco",
        "Personal Travel - Eco Plus"
    ]

    travel_combo = f"{travel_purpose} - {travel_class}"
    travel_purpose_class_encoding = {key: 1 if key == travel_combo else 0 for key in travel_classes}

    # === Final Input Feature List ===
    input_data = {
        "Flight Distance": flight_distance,
        "Total Delay": total_delay,
        "Is Delayed": is_delayed,
        "Age Group": age_group_encoded,
        "Service Score": service_score,
        "Gender_Female": gender_female,
        "Gender_Male": gender_male,
        "Customer Type_Loyal Customer": customer_loyal,
        "Customer Type_disloyal Customer": customer_disloyal
    }

    input_data.update({
        f"Travel Purpose Class_{k}": v for k, v in travel_purpose_class_encoding.items()
    })

    # Convert to DataFrame
    user_df = pd.DataFrame([input_data])

    # === Predict Button ===
    if st.sidebar.button("🎯 Predict Satisfaction"):
        prediction = model_best.predict(user_df)
        prediction_label = "😊 Satisfied" if prediction[0] == 1 else "😐 Neutral/Unhappy"

        st.subheader("🔍 Prediction Result")
        st.success(f"**Prediction:** {prediction_label}")
