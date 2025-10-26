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
  ![m1](https://github.com/user-attachments/assets/ddb8e1fe-131a-47d6-9e02-412ad2706cc6)

  ![m2](https://github.com/user-attachments/assets/4864c5f9-df67-4ee9-bf58-ff85663bbe3e)


- **Streamlit app** for flight price prediction.
 https://flight-price-and-customer-satisfaction-prediction.streamlit.app/
  ![s1](https://github.com/user-attachments/assets/cf7d1646-30c4-40ad-893b-920b5790559b)
 ![f1](https://github.com/user-attachments/assets/365b6797-ef85-4a8e-afa3-ded6e97ab4b0)

 

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
  ![m3](https://github.com/user-attachments/assets/1bcd2844-d03a-48ec-b8c5-9fe1f0d0e358)

  ![m4](https://github.com/user-attachments/assets/0e85f3e3-9cd0-4990-bd15-4bb37214f7d2)

- **Streamlit app** for customer satisfaction prediction.
  
  ![c1](https://github.com/user-attachments/assets/2301d834-80bc-4e65-a40b-779240fee8f8)

  ![c2](https://github.com/user-attachments/assets/64ac6e01-aed3-4ad5-aa49-7c23f7370477)


---

### **💻 Installation:**
1. Clone this repository:
   ```bash
   git clone https://github.com/SSaranya19/Flight-Price-and-Customer-Satisfaction-Prediction.git
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```bash
   streamlit run main.py
   ```
