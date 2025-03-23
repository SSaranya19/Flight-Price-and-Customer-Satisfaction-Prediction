# ✈️ Flight Price & Customer Satisfaction Prediction 🌟

Welcome to the **Flight Price and Customer Satisfaction Prediction** project! This repository includes two end-to-end predictive models for the **Travel** and **Customer Experience** domains. One model predicts **flight ticket prices**, and the other predicts **customer satisfaction** based on various features. Both models are built with **Python**, **Machine Learning**, and deployed using **Streamlit**, with **MLflow** used for experiment tracking and model management.

---

## 🛫 **Project 1: Flight Price Prediction (Regression)** 🏷️

### **🔧 Skills Learned:**
- Python
- Streamlit
- Machine Learning (Regression)
- Data Analysis
- MLflow

### **🌍 Domain:**
Travel & Tourism

### **📝 Problem Statement:**
This project builds an **end-to-end solution** to predict flight ticket prices based on factors such as departure time, source, destination, and airline type. The solution involves cleaning and processing the dataset, performing feature engineering, training regression models, and deploying them in a **Streamlit** app where users can input filters (route, time, and date) and get predicted flight prices. ✈️💰

### **💡 Business Use Cases:**
- **Helping travelers** plan their trips with price predictions.
- **Assisting travel agencies** in optimizing pricing and marketing.
- **Enabling businesses** to budget for employee travel expenses.
- **Supporting airlines** to optimize ticket pricing strategies. 💸📈

### **🛠️ Approach:**

#### **Step 1: Data Preprocessing** 🔄
- Load and clean the dataset.
- Handle missing values, duplicates, and standardize date/time formats.
- Perform feature engineering (e.g., calculate price per minute).

#### **Step 2: Flight Price Prediction** 💡
- Perform **Exploratory Data Analysis** (EDA) to uncover trends and correlations.
- Train multiple regression models (Linear Regression, Random Forest, XGBoost) to predict prices.
- **Integrate MLflow** to track experiments, log metrics (RMSE, R-squared), and save models. 📊

#### **Step 3: Streamlit App Development** 📱
- Build an interactive Streamlit app that:
  - Visualizes flight price trends.
  - Allows users to filter by route, airline, and time.
  - Predicts prices based on user input.

### **🔍 Results:**
- Cleaned and processed dataset ready for analysis.
- High-accuracy regression models for flight price predictions.
- An easy-to-use **Streamlit app** for flight price prediction and data visualization. 🎉

### **📍 Technical Tags:**
- Python 🐍
- Data Cleaning 🧹
- Feature Engineering 🔧
- Machine Learning (Regression) 📈
- Streamlit 🌐
- MLflow 🔄

### **📂 Dataset:**
- **Dataset Link**: [Flight_Price.csv](#)
- **Features**:
  - **Airline**: Name of the airline
  - **Date_of_Journey**: Date of departure
  - **Source & Destination**: Starting and ending airports
  - **Route**: Flight path (with stops)
  - **Dep_Time**: Departure time
  - **Arrival_Time**: Arrival time
  - **Duration**: Flight duration
  - **Total_Stops**: Number of stops
  - **Additional_Info**: Extra info like meal availability

### **📦 Project Deliverables:**
- Python scripts for data processing, model training, and MLflow integration.
- Cleaned dataset.
- Regression models logged with MLflow.
  ![f1](https://github.com/user-attachments/assets/0096a8bb-117b-43ba-8dce-9bf6a09d7a4f)
  ![f2](https://github.com/user-attachments/assets/f17947f1-f207-4eb6-b2e4-be3ae5506650)

- **Streamlit app** for flight price prediction.
  ![s1](https://github.com/user-attachments/assets/cf7d1646-30c4-40ad-893b-920b5790559b)
  ![s1f](https://github.com/user-attachments/assets/c41e9165-f6fb-41e8-8646-c2e1d2b2c233)
  ![s1f2](https://github.com/user-attachments/assets/29acda72-7841-4921-8ae8-42da030d5ea1)

---


## 👨‍💻 **Project 2: Customer Satisfaction Prediction (Classification)** 💬

### **🔧 Skills Learned:**
- Python
- Machine Learning (Classification)
- Data Analysis
- Streamlit
- MLflow

### **🌍 Domain:**
Customer Experience

### **📝 Problem Statement:**
In this project, we build a **classification model** to predict customer satisfaction levels based on various factors such as demographics, service ratings, and customer feedback. The dataset is processed, features are engineered, and classification models are trained and deployed in a **Streamlit** app, where users can input customer data and receive predicted satisfaction levels. 😊

### **💡 Business Use Cases:**
- **Enhancing customer experience** by predicting and addressing dissatisfaction.
- **Providing actionable insights** to improve services and offerings.
- **Supporting marketing teams** in targeting customer segments.
- **Assisting management** in improving customer retention strategies. 💡📊

### **🛠️ Approach:**

#### **Step 1: Data Preprocessing** 🔄
- Load and clean the dataset.
- Handle missing values, duplicates, and encode categorical variables.
- Normalize numerical features as needed.

#### **Step 2: Customer Satisfaction Prediction** 💡
- Perform **Exploratory Data Analysis** (EDA) to understand relationships between features.
- Train classification models (Logistic Regression, Random Forest, Gradient Boosting).
- **Integrate MLflow** to track experiments, log accuracy, F1-score, and save models. 🔍

#### **Step 3: Streamlit App Development** 📱
- Build an interactive Streamlit app that:
  - Visualizes customer satisfaction trends.
  - Allows users to input demographics and service ratings.
  - Predicts satisfaction levels. ✅

### **🔍 Results:**
- Cleaned and processed dataset ready for classification.
- High-accuracy classification models for predicting customer satisfaction.
- An intuitive **Streamlit app** for customer satisfaction prediction and data visualization. 🎉

### **📍 Technical Tags:**
- Python 🐍
- Data Cleaning 🧹
- Feature Engineering 🔧
- Machine Learning (Classification) 📊
- Streamlit 🌐
- MLflow 🔄

### **📂 Dataset:**
- **Dataset Link**: [Passenger_Satisfaction.csv](#)
- **Features**:
  - **Gender**: Gender of the passengers
  - **Customer Type**: Loyalty status (loyal/disloyal)
  - **Age**: Passenger age
  - **Type of Travel**: Travel purpose (personal/business)
  - **Class**: Travel class (business/eco/eco-plus)
  - **Flight distance**: Distance covered during flight
  - **Service satisfaction ratings**: Satisfaction ratings for various services (wifi, food, comfort, etc.)
  - **Satisfaction**: Customer satisfaction level (Satisfied, Neutral, Dissatisfied)

### **📦 Project Deliverables:**
- Python scripts for data preprocessing, model training, and MLflow integration.
- Cleaned dataset.
- Classification models logged with MLflow.
  ![c1](https://github.com/user-attachments/assets/21b46ed0-68a2-456b-9b4f-ab97486b8ebd)
  ![c2](https://github.com/user-attachments/assets/782b4531-1d4d-4589-a577-3caa2e362fb7)
- **Streamlit app** for customer satisfaction prediction.
  ![s2c1](https://github.com/user-attachments/assets/0cfe9f8a-1e98-4234-a448-939e30582b5c)
  ![s2c2](https://github.com/user-attachments/assets/055b1c3e-d057-45c3-b17b-c8b15d7eacf1)

---

### **💻 Installation:**
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/flight-price-customer-satisfaction-prediction.git
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```bash
   streamlit run main.py
   ```
