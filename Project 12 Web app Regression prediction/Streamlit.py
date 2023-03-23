import pandas as pd
import numpy as np
import pickle
import streamlit as st

st.write("""
# US Health care cost Prediction 
This app predicts the **Health care cost claimed by US patients**!
""")
st.write('---')

pickle_in = open('SVRpipeline.pkl', 'rb')
Regressor = pickle.load(pickle_in)

def WeightRange(Bw, Ht):
    Weight_Range = ''
    BMI = Bw/(Ht/100)**2
    if BMI < 18.5:
      Weight_Range = 'underweight'
    elif (BMI >=18) & (BMI <25):
      Weight_Range = 'normal'
    elif (BMI >=25) & (BMI <30):
      Weight_Range = 'overweight'
    else: Weight_Range = 'obese'
    return Weight_Range

def AgeRange(Age):
  Age_Range = ''
  if Age < 65 :
    Age_Range = 'adult'
  else: Age_Range = 'elder'
  return Age_Range


def user_input_features():
    Age = st.slider('How old are you?', 18, 100, 50)
    Gender = st.radio("What\'s your gender", ('male', 'female'))
    Weight = st.number_input('Insert weight (kg)', min_value=20)
    Height = st.number_input('Insert weight (cm)', min_value=100)
    children = st.slider('How many children do you have?', 0, 5, 2)
    Smoker = st.radio("Are you smoker?", ('yes', 'no'))
    region = st.selectbox('Which region of US do you live?',
                          ('southwest', 'southeast', 'northwest', 'northeast'))

    BMI = Weight / (Height/100) ** 2

    Weight_Range = WeightRange(Weight, Height)
    Age_Range = AgeRange(Age)

    data = {'age': Age,
            'sex': Gender,
            'bmi': BMI,
            'children': children,
            'smoker': Smoker,
            'region': region,
            'Weight_Range': Weight_Range,
            'Age_Range': Age_Range}


    features = pd.DataFrame(data, index=[0])
    return features


user_info = user_input_features()


def prediction(user_info):
    prediction = Regressor.predict(user_info)
    predictionexp = np.expm1(prediction)
    return predictionexp

# Main Panel

st.write('---')

if st.button("Predict"):
    result = prediction(user_info)
    st.header('Prediction of health care cost')
    st.write(f'{result} usd')
st.write('---')



