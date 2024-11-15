# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 18:28:07 2024

@author: umara
"""
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading the saved model

diabetes_model= pickle.load(open('C:/Deploy Models/Streamlit app on Heruko/dibaetic_model.sav','rb'))

heart_disease_model= pickle.load(open('C:/Deploy Models/Streamlit app on Heruko/heart_disease_model.sav','rb'))

parkinsons_model=  pickle.load(open('C:/Deploy Models/Streamlit app on Heruko/parkinsons_model.sav','rb'))


#sidebar for navigate

with st.sidebar:
    
    selected = option_menu('HUMAN DISEASE DETECTION SYSTEM',
                           
                         ['Diabetes Detection',
                          'Heart Disease Detection',
                          'Parkinsons Disease Detection'],
                         
                         icons=['activity','heart','person'],
                         # from https://icons.getbootstrap.com/
                          default_index=0)
    
    # deafault 0 means when you open App 'Diabetes Prediction' is selected by default
    # if default was 1 then 'Heart Disease Prediction' will be selected by default
    # default 3 for 'Parkinsons Disease Prediction'

#Diabetes Prediction Page
if(selected=='Diabetes Detection'):
    
    #page title
    st.title('DIABETES DETECTION')
    #st.image('C:/Deploy Models/Muliple Disease Detection Web App/diabetes_unsplash.jpg')
    
    #getting the input data from the user (All independent variables)
    
    Age = st.slider('Age',min_value=0,max_value=100,value=30,step=2)
    
    # columns for input field 3 columns in 1 row
    col1,col2,col3=st.columns(3)
     
    with col1:
        Pregnancies=st.text_input('No. of Pregnancies')
        
    with col2:
        Glucose=st.text_input('Glucose level')
    
    with col3:
        BloodPressure=st.text_input('BloodPressure level')
    
    with col1:
        SkinThickness=st.text_input('Skin Thickness Value')
    
    with col2:
        Insulin=st.text_input('Insulin Level')
    
    with col3:
        BMI=st.text_input('BMI Value')
    
    with col2:
        DiabetesPedigreeFunction=st.text_input('Diabetes Pedigree Function Value')
    
   
    
    # Code for Prediction
    
    diab_diagnosis=''
    #this will store the result
    
    #creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction=diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        # instead of reshaping the array we use 2d array('[[]]') to store the above input in his app which is different fom 'Diabetes Web App'
    
        if(diab_prediction[0]==1):
            diab_diagnosis='The Person is Diabetic'
            st.balloons()
        
        else:
            diab_diagnosis='The Person is not Diabetic'
            
    st.success(diab_diagnosis)
    # to print the diagnosis
    
    
#Heart Disease Prediction Page

    # to print the diagnosis
if selected == 'Heart Disease Detection':

    # page title
    st.title('HEART DISEASE DETECTION')
    #st.image('C:/Deploy Models/Muliple Disease Detection Web App/heart-disease-stock-photo-021423.jpg')
    
    age = st.slider('Age',min_value=0,max_value=100,value=30,step=2)

    col1, col2, col3 = st.columns(3)

    #with col1:
    

    with col1:
        sex = st.text_input('Sex')

    with col2:
        cp = st.text_input('Chest Pain types')

    with col3:
        trestbps = st.text_input('Resting Blood Pressure')

    with col1:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col2:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col3:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col1:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col2:
        exang = st.text_input('Exercise Induced Angina')

    with col3:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col1:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col2:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col3:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
            st.balloons()
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)    
    
#Parkinsons Disease Prediction Page
if(selected=='Parkinsons Disease Detection'):
    
    #page title
    st.title('PARKINSON DISEASE')
    #st.image('C:/Deploy Models/Muliple Disease Detection Web App/th.jpg',width=700)
    #getting the input data from the user (All independent variables)
    
    # columns for input field 3 columns in 1 row
    col1,col2,col3=st.columns(3)
    
    with col1:
        Fo=st.text_input('MDVP:Fo(Hz)')
    with col2:
        Fhi=st.text_input('MDVP:Fhi(Hz)')
    with col3:
        Flo=st.text_input('MDVP:Flo(Hz)')
    with col1:
        Jitter_percent=st.text_input('MDVP:Jitter(%)')
    with col2:
        Jitter_Abs=st.text_input('MDVP:Jitter(Abs)')
    with col3:
        MDVP_RAP=st.text_input('MDVP:RAP')
    with col1:
        MDVP_PPQ=st.text_input('MDVP:PPQ')
    with col2:
        Jitter_DDP=st.text_input('Jitter:DDP')
    with col3:
        MDVP_Shimmer=st.text_input('MDVP:Shimmer')
    with col1:
        MDVP_Shimmer_dB=st.text_input('MDVP:Shimmer(dB)')
    with col2:
        Shimmer_APQ3=st.text_input('Shimmer:APQ3')
    with col3:
        Shimmer_APQ5=st.text_input('Shimmer:APQ5')
    with col1:
        MDVP_APQ=st.text_input('MDVP:APQ')
    with col2:
        Shimmer_DDA=st.text_input('Shimmer:DDA')
    with col3:
        NHR=st.text_input('NHR')
    with col1:
        HNR=st.text_input('HNR')
    with col2:
        RPDE=st.text_input('RPDE')
    with col3:
        DFA=st.text_input('DFA')
    with col1:
        spread1=st.text_input('spread1')
    with col2:
        spread2=st.text_input('spread2')
    with col3:
        D2=st.text_input('D2')
    with col2:
        PPE=st.text_input('PPE')
    
    
    # Code for Prediction
    
    park_diagnosis=''
    #this will store the result
    
    #creating a button for Prediction
    
    if st.button('Parkinsons Test Result'):
        park_prediction=parkinsons_model.predict([[Fo,Fhi,Flo,Jitter_percent,Jitter_Abs,MDVP_RAP,MDVP_PPQ,Jitter_DDP,MDVP_Shimmer,MDVP_Shimmer_dB,Shimmer_APQ3,Shimmer_APQ5,MDVP_APQ,Shimmer_DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])
        # instead of reshaping the array we use 2d array('[[]]') to store the above input in his app which is different fom 'Diabetes Web App'
    
        if(park_prediction[0]==1):
            park_diagnosis='The Person has Parkinson'
            st.balloons()
        
        else:
            park_diagnosis='The Person does not has Parkinson'
            
    st.success(park_diagnosis)
    # to print the diagnosis
    
    
    

# streamlit run "C:\Deploy Models\Muliple Disease Detection Web App\multile disease prediction.py" 
