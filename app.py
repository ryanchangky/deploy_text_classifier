import streamlit as st
import numpy as np
import joblib
import sklearn

st.title("Text Classification: Computer Science VS Machine Learning Questions")

inputs = st.text_input("Enter post content")

if st.button("Predict"):
    model = joblib.load("gs_mnb.joblib")
    pred = model.predict([inputs])

    if pred == 0:
        st.markdown(f"### The post content belongs to Computer Science")
    else:
        st.markdown(f"### The post content belongs to Machine Learning Questions")