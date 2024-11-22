import joblib
import numpy as np
import streamlit as st
from sklearn.preprocessing import StandardScaler

scaler = joblib.load("scaler.pkl")
model = joblib.load("resto_model.pkl")

def show_predict_page():
    st.title("Restaurant Rating Prediction")
    st.divider()

    averageCost = st.number_input("Please enter the estimated average cost for two people", min_value=50, max_value=999999, value=1000, step=200)
    tableBooking = st.selectbox("Does the restaurant have table booking?", ["Yes", "No"])
    onlineDelivery = st.selectbox("Does the restaurant have online delivery?", ["Yes", "No"])
    priceRange = st.selectbox("What is the restaurant's price range? (1 - Cheapest, 4 - Most Expensive)", [1,2,3,4])
    btnPredict = st.button("Predict the review!")
    st.divider()

    bookingStatus = 1 if tableBooking == "Yes" else 0
    deliveryStatus = 1 if onlineDelivery == "Yes" else 0

    values=[[averageCost,bookingStatus,deliveryStatus,priceRange]]
    my_X_values = np.array(values)
    X = scaler.transform(my_X_values)

    if btnPredict:
        rating = model.predict(X)
        
        if rating < 2.5:
            rateCategory = "Poor"
        elif rating < 3.5:
            rateCategory = "Average"
        elif rating < 4.0:
            rateCategory = "Good"
        elif rating < 4.5:
            rateCategory = "Very Good"
        else:
            rateCategory = "Excellent"

        st.subheader(f"The predicted rating is {rating[0]:.2f} - {rateCategory}")

    
