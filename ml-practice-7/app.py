import streamlit as st
import requests

st.title("Iris Prediction App")

sepal_length = st.number_input("Sepal Length")
sepal_width = st.number_input("Sepal Width")
petal_length = st.number_input("Petal Length")
petal_width = st.number_input("Petal Width")

if st.button("Predict"):
    data = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width
    }

    response = requests.post("http://127.0.0.1:8000/predict", json=data)

    if response.status_code == 200:
        prediction = response.json()["prediction"]

        classes = {
            0: "Setosa",
            1: "Versicolor",
            2: "Virginica"
        }

        flower_name = classes[prediction]
        st.success(f" Prediction: {flower_name}")
    else:
        st.error("Error in prediction")