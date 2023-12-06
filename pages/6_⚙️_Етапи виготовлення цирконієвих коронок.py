import streamlit as st
import pandas as pd
import altair as alt
import datetime
import pickle
import streamlit_authenticator as stauth
from pathlib import Path

from pages.data.table_7 import *

st.sidebar.markdown("""
    <style>
    [data-testid='stSidebarNav'] > ul {
        min-height: 50vh;
    } 
    </style>
    """, unsafe_allow_html=True)


# st.set_page_config(page_title="Plotting Demo", page_icon="📈")

names = ['admin']
usernames = ['admin']

file_path = Path(__file__).parent / "../hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
    "sales_dashboard", "abcdef", cookie_expiry_days=30)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Username/password is incorrect")

if authentication_status == None:
    st.warning("Please enter your username and password")

if authentication_status:
    st.markdown("# Етапи виготовлення цирконієвих коронок цифровим та аналоговим методом")

    doctor_name = st.text_input("ПІБ доктора", placeholder="Введіть ПІБ доктора", key=1)

    d1 = st.date_input("Дата проведення", datetime.date(2023, 10, 12))
    st.write('Дата проведення:', d1)

    constr_type = st.selectbox("Тип кострукції", ['Цифровий протокол', 'Аналоговий протокол'])

    quantity = st.number_input("Цирконієвa коронка", min_value=1, placeholder="Введіть кількість", value=1)
    
    st.write("Клініко-лабораторні етапи")

    if constr_type == "Цифровий протокол":
        
        selected_values = []
        selected_labels = []
        for label, value in checkbox_values_digital.items():
            if label == "Зняття відбитку з силіконової маси":
                st.write("Або за допомогою лабораторного сканеру:")
            is_selected = st.checkbox(label)
            if is_selected:
                selected_values.append(value)
                selected_labels.append(label)

        doctor = 0
        doctor_yop = 0
        tech = 0
        tech_yop = 0
        ms = 0
        ms_yop = 0

        for element in selected_values:
            doctor += element[0][0]
            doctor_yop += element[0][1]
            tech += element[1][0]
            tech_yop += element[1][1]
            ms += element[2][0]
            ms_yop += element[2][1]

        doctor *= quantity
        doctor_yop *= quantity
        tech *= quantity
        tech_yop *= quantity
        ms *= quantity
        ms_yop *= quantity

        doctor_yop = round(doctor_yop, 2)
        tech_yop = round(tech_yop, 2)
        ms_yop = round(ms_yop, 2)

        st.write(f'Загалом: лікар {doctor}хв {doctor_yop} УОП. Технік: {tech}хв {tech_yop} УОП. M/C: {ms}хв {ms_yop} УОП')
    else:
        
        selected_values = []
        selected_labels = []
        for label, value in checkbox_values_analog.items():
            
            is_selected = st.checkbox(label)
            if is_selected:
                selected_values.append(value)
                selected_labels.append(label)

        doctor = 0
        doctor_yop = 0
        tech = 0
        tech_yop = 0
        ms = 0
        ms_yop = 0

        for element in selected_values:
            doctor += element[0][0]
            doctor_yop += element[0][1]
            tech += element[1][0]
            tech_yop += element[1][1]
            ms += element[2][0]
            ms_yop += element[1][1]

        doctor *= quantity
        doctor_yop *= quantity
        tech *= quantity
        tech_yop *= quantity
        ms *= quantity
        ms_yop *= quantity

        doctor_yop = round(doctor_yop, 2)
        tech_yop = round(tech_yop, 2)
        ms_yop = round(ms_yop, 2)

        st.write(f'Загалом: лікар {doctor}хв {doctor_yop} УОП. Технік: {tech}хв {tech_yop} УОП. M/C: {ms}хв {ms_yop} УОП')
    if st.button('Зберегти інформацію', key=12):
      df = pd.read_csv("6.csv")
      if doctor_name == "":
          st.warning("Будь ласка, введіть лікаря!")
      
      elif len(selected_labels) == 0:
        st.warning("Будь ласка, виберіть клінічні етапи")
      else:
        data = [doctor_name,
                d1,
                constr_type,
                quantity,
                selected_labels,
                doctor,
                doctor_yop,
                tech,
                tech_yop,
                ms,
                ms_yop
                ]
        df.loc[len(df)] = data
        df.to_csv('6.csv', index=False)
        # st.write(df)
        st.success("Дані були збережні.")


    st.sidebar.title(f"Welcome {name}")
    authenticator.logout("Logout", "sidebar")
