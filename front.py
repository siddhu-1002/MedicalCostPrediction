import streamlit as st
import pandas as pd
import pickle

cols = ['age', 'bmi', 'children', 'smoker_no', 'smoker_yes', 'sex_female',
       'sex_male', 'region_northeast', 'region_northwest', 'region_southeast',
       'region_southwest']

st.title("Medical Expenses Prediction")

age = st.number_input("What is your age?",0, 80, step = 1)
sex = st.selectbox("What is your gender?", ("male", "female"))

if sex == "male":
    sex_male = 1
    sex_female = 0

if sex == "female":
    sex_male = 0
    sex_female = 1


bmi = st.number_input("What is your body mass index?", 1.0, 60.0, step = 0.01)
children = st.slider("How many children do you have?", 0, 10, 1)

smoker = st.selectbox("Do you smoke?", ("yes", "no"))
if smoker == "no":
    smoker_no = 1
    smoker_yes = 0

if smoker == "yes":
    smoker_no = 0
    smoker_yes = 1

region = st.selectbox("Where do you live?", ("northeast", "northwest", "southeast", "southwest"))

if region == "northeast":
    region_northeast = 1
    region_southeast = 0
    region_northwest = 0
    region_southwest = 0

elif region == "northwest":
    region_northeast = 0
    region_southeast = 0
    region_northwest = 1
    region_southwest = 0

elif region == "southeast":
    region_northeast = 0
    region_southeast = 1
    region_northwest = 0
    region_southwest = 0

elif region == "southwest":
    region_northeast = 0
    region_southeast = 0
    region_northwest = 0
    region_southwest = 1


model = pickle.load(open('model.pkl', 'rb'))
y_pred = model.predict(pd.DataFrame([[age, bmi, children, smoker_no, smoker_yes, sex_female, sex_male,
region_northeast, region_northwest, region_southeast, region_southwest]], columns = cols))

if st.button("Predict", type = "primary"):
    st.write("The predicted charges are : ", y_pred[0])