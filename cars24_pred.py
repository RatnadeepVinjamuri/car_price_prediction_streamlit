
import streamlit as st
import pandas as pd
import datetime
import pickle

st.title("Used Car Price Prediction")
st.subheader("Web Application to predict price (in Lakhs-INR)")

encode_dict = {
    "fuel_type" : {'Diesel':1, 'Petrol':2, 'CNG':3, 'LPG':4, 'Electric':5},
    "transmission_type" : {'Manual':1, 'Automatic':2}
}

def model_pred(year, fuel_type, engine, max_power, km_driven, mileage, transmission_type, seats):

    #Load the model
    with open("car_pred", 'rb') as file:
        reg_model = pickle.load(file)

        input_features = [[2018.0, 1, 4000, fuel_type, transmission_type, 19.70, engine, 86.30, seats]]
    
        return reg_model.predict(input_features)

## Inputs from User
col1, col2 = st.columns(2)

year = col2.slider("Select Year", 1991, 2021, step=1)
km_driven = col2.slider("Set Kilometers", 100, 1000000, step=500)
mileage = col2.slider("Select Mileage", 4, 34, step=4)
transmission_type = col1.selectbox("Select the Transmission type", ['Manual', 'Automatic'])
fuel_type = col1.selectbox("Select the Fuel type", ['Diesel', 'Petrol', 'CNG', 'LPG', 'Electic'])
seats = col1.selectbox("Select no. of seats", [2,4,5,6,7,8,9,10,14])

if(st.button("Predict Price")):
    fuel_type_encoded = encode_dict['fuel_type'][fuel_type]
    transmission_type_encoded = encode_dict['transmission_type'][transmission_type]

    price = model_pred(year, fuel_type_encoded, engine, max_power, km_driven, mileage, transmission_type_encoded, seats)
    st.write(price)

cars_df = pd.read_excel("./cars24.xlsx")
st.dataframe(cars_df)