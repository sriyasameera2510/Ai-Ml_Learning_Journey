
import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load model (Random Forest model from Week 6)
model = pickle.load(open('../week6_end_to_end_ML_project/model.pkl', 'rb'))

def predict_heart_disease(input_data):
    input_df = pd.DataFrame([input_data])
    prediction = model.predict(input_df)
    return prediction[0]


st.title('Heart Disease Predictor')

# Numeric inputs
age = st.number_input('Age', 20, 100)
resting_bp = st.number_input('Resting Blood Pressure')
cholesterol = st.number_input('Cholesterol')
fasting_bs = st.selectbox('Fasting Blood Sugar > 120 mg/dl?', [0, 1])
max_hr = st.number_input('Max Heart Rate Achieved')
oldpeak = st.number_input('Oldpeak (ST depression)', min_value=0.0, max_value=10.0, step=0.1)

# Categorical binary inputs (already one-hot encoded)
sex_m = st.selectbox('Sex: Male?', [0, 1])
chest_ata = st.selectbox('Chest Pain Type: ATA?', [0, 1])
chest_nap = st.selectbox('Chest Pain Type: NAP?', [0, 1])
chest_ta = st.selectbox('Chest Pain Type: TA?', [0, 1])
restecg_normal = st.selectbox('Resting ECG: Normal?', [0, 1])
restecg_st = st.selectbox('Resting ECG: ST?', [0, 1])
ex_angina_y = st.selectbox('Exercise Induced Angina?', [0, 1])
st_slope_flat = st.selectbox('ST Slope: Flat?', [0, 1])
st_slope_up = st.selectbox('ST Slope: Up?', [0, 1])

# Prepare input dictionary
input_data = {
    'Age': age,
    'RestingBP': resting_bp,
    'Cholesterol': cholesterol,
    'FastingBS': fasting_bs,
    'MaxHR': max_hr,
    'Oldpeak': oldpeak,
    'Sex_M': sex_m,
    'ChestPainType_ATA': chest_ata,
    'ChestPainType_NAP': chest_nap,
    'ChestPainType_TA': chest_ta,
    'RestingECG_Normal': restecg_normal,
    'RestingECG_ST': restecg_st,
    'ExerciseAngina_Y': ex_angina_y,
    'ST_Slope_Flat': st_slope_flat,
    'ST_Slope_Up': st_slope_up
}

if st.button('Predict'):
    result = predict_heart_disease(input_data)
    st.success(f'🧠 Prediction: {"Has Heart Disease 🚨" if result == 1 else "No Heart Disease ✅"}')
