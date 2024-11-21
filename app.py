import joblib
import streamlit as st
import numpy as np
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
st.set_page_config(layout = "wide")
st.title("Restaurant Rating Prediction App")
st.caption("This app helps predict a restaurant's review class")
st.divider()

averageCost = st.number_input("Please enter the estimated average cost for two", min_value=50, max_value=999999, value=1000, step=200)
tableBooking = st.selectbox("Does the restaurant have table booking?", ["Yes", "No"])
onlineDelivery = st.selectbox("Does the restaurant have online delivery?", ["Yes", "No"])
priceRange = st.selectbox("What is the restaurant's price range? (1 - Cheapest, 4 - Most Expensive)", [1,2,3,4])
btnPredict = st.button("Predict the review!")
st.divider()

model = joblib.load("resto_model.pkl")
bookingStatus = 1 if tableBooking == "Yes" else 0
deliveryStatus = 1 if onlineDelivery == "Yes" else 0

averageCost = scaler.fit_transform(averageCost)
bookingStatus = scaler.fit_transform(bookingStatus)
deliveryStatus = scaler.fit_transform(deliveryStatus)
priceRange = scaler.fit_transform(priceRange)

if btnPredict:
    st.snow()
    model.predict([[averageCost, bookingStatus, deliveryStatus, priceRange]])
    st.write(prediction)