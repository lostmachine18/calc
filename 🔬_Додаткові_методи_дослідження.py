import streamlit as st
import pandas as pd
import altair as alt
import datetime
import pickle
import streamlit_authenticator as stauth
from pathlib import Path

from data.table_1 import *

st.sidebar.markdown("""
    <style>
    [data-testid='stSidebarNav'] > ul {
        min-height: 50vh;
    } 
    </style>
    """, unsafe_allow_html=True)


# --- USER AUTH -------------------------

names = ['guest']
usernames = ['guest']

file_path = Path(__file__).parent / "hashed_pw.pkl"
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

    st.header("Додаткові методи дослідження в цифровій стоматології. Хвилини та УОПи")
    st.subheader("Електронна аксіографія")

    doctor_name = st.text_input("ПІБ доктора", placeholder="Введіть ПІБ доктора", key=1)

    d1 = st.date_input("Дата проведення", datetime.date(2023, 10, 10))
    st.write('Дата проведення:', d1)

    # some_data = pd.read_csv("df.csv")
    # st.write(some_data)

    el_acsiography_options = st.multiselect(
        'Клінічні етапи',
        list(el_acsiography.keys()),
        [], placeholder="Виберіть із списку")
    
    el_acsiography_doctor, el_acsiography_doctor_yop, el_acsiography_ms, el_acsiography_ms_yop = calculate_time(el_acsiography, el_acsiography_options)

    st.write(f"Разом: Лікар - {el_acsiography_doctor} хв, \
              {el_acsiography_doctor_yop} УОП. М/С – {el_acsiography_ms} хв, {el_acsiography_ms_yop} УОП.")
    
    if st.button('Зберегти інформацію', key=2):
        df = pd.read_csv("calc_axiography_methods_1.csv")
        if doctor_name == "":
            st.warning("Будь ласка, введіть лікаря!")
        elif len(el_acsiography_options) == 0:
            st.warning("Будь ласка, виберіть клінічні етапи!")
        else:
          data = [doctor_name,
                  d1,
                  el_acsiography_options,
                  el_acsiography_doctor,
                  el_acsiography_doctor_yop,
                  el_acsiography_ms,
                  el_acsiography_ms_yop
                  ]
          df.loc[len(df)] = data
          df.to_csv('calc_axiography_methods_1.csv', index=False)
          
          st.success("Дані були збережні.")

# --- JVA --------------------------------------------------------
    
    st.subheader("Аналіз вібрацій СНЩС (JVA)")
    #st.text_input("ПІБ доктора", placeholder="Введіть ПІБ доктора", key=2)

    d2 = st.date_input("Дата проведення", datetime.date(2023, 10, 11))
    st.write('Дата проведення:', d2)

    


    jva_options = st.multiselect(
        'Клінічні етапи',
        list(jva.keys()),
        [], placeholder="Виберіть із списку")
    
    jva_doctor, jva_doctor_yop, jva_ms, jva_ms_yop = calculate_time(jva, jva_options)

    st.write(f"Разом: Лікар - {jva_doctor} хв, {jva_doctor_yop} УОП. М/С – {jva_ms} хв {jva_ms_yop} УОП.")
    
    if st.button('Зберегти інформацію', key=3):
        df = pd.read_csv("calc_jva_methods_1.csv")
        if doctor_name == "":
            st.warning("Будь ласка, введіть лікаря!")
        elif len(jva_options) == 0:
            st.warning("Будь ласка, виберіть клінічні етапи!")
        else:
          data = [doctor_name,
                  d2,
                  jva_options,
                  jva_doctor,
                  jva_doctor_yop,
                  jva_ms,
                  jva_ms_yop
                  ]
          df.loc[len(df)] = data
          df.to_csv('calc_jva_methods_1.csv', index=False)
          st.success("Дані були збережні.")

    # --- MIOGRAPHY ---------------------------------------------

    st.subheader("Електоміографія")

    #st.text_input("ПІБ доктора", placeholder="Введіть ПІБ доктора", key=3)

    d3 = st.date_input("Дата проведення", datetime.date(2023, 10, 13))
    st.write('Дата проведення:', d3)


    el_miography_options = st.multiselect(
        'Клінічні етапи',
        list(el_miography.keys()),
        [], placeholder="Виберіть із списку")
    
    el_miography_doctor, el_miography_doctor_yop, el_miography_ms, el_miography_ms_yop = calculate_time(el_miography, el_miography_options)

    st.write(f"Разом: Лікар - {el_miography_doctor} хв, {el_miography_doctor_yop} УОП. М/С – {el_miography_ms} хв {el_miography_ms_yop} УОП.")
    if st.button('Зберегти інформацію', key=4):
        df = pd.read_csv("calc_miography_methods_1.csv")
        if doctor_name == "":
            st.warning("Будь ласка, введіть лікаря!")
        elif len(el_miography_options) == 0:
            st.warning("Будь ласка, виберіть клінічні етапи!")
        else:
          data = [doctor_name,
                  d3,
                  el_miography_options,
                  el_miography_doctor,
                  el_miography_doctor_yop,
                  el_miography_ms,
                  el_miography_ms_yop
                  ]
          df.loc[len(df)] = data
          df.to_csv('calc_miography_methods_1.csv', index=False)
          st.success("Дані були збережні.")

    # --- T-SCAN ---------------------------------------------

    st.subheader("T-SCAN")

    #st.text_input("ПІБ доктора", placeholder="Введіть ПІБ доктора", key=4)


    d4 = st.date_input("Дата проведення", datetime.date(2023, 10, 14))
    st.write('Дата проведення:', d4)

    t_scan_options = st.multiselect(
        'Клінічні етапи',
        list(t_scan.keys()),
        [], placeholder="Виберіть із списку")
    
    t_scan_doctor, t_scan_doctor_yop, t_scan_ms, t_scan_ms_yop = calculate_time(t_scan, t_scan_options)

    st.write(f"Разом: Лікар - {t_scan_doctor} хв, {t_scan_doctor_yop} УОП. М/С – {t_scan_ms} хв {t_scan_ms_yop} УОП.")
    if st.button('Зберегти інформацію', key=5):
        df = pd.read_csv("calc_tscan_methods_1.csv")
        if doctor_name == "":
            st.warning("Будь ласка, введіть лікаря!")
        elif len(t_scan_options) == 0:
            st.warning("Будь ласка, виберіть клінічні етапи!")
        else:
          data = [doctor_name,
                  d4,
                  t_scan_options,
                  t_scan_doctor,
                  t_scan_doctor_yop,
                  t_scan_ms,
                  t_scan_ms_yop
                  ]
          df.loc[len(df)] = data
          df.to_csv('calc_tscan_methods_1.csv', index=False)
          st.success("Дані були збережні.")

    # --- Цефалометричний аналіз,сегментація---------------------------------------------

    st.subheader("Цефалометричний аналіз, сегментація")
    #st.text_input("ПІБ доктора", placeholder="Введіть ПІБ доктора", key=5)

    d5 = st.date_input("Дата проведення", datetime.date(2023, 10, 15))
    st.write('Дата проведення:', d5)

    segmentation_options = st.multiselect(
        'Клінічні етапи',
        list(segmentation.keys()),
        [], placeholder="Виберіть із списку")
    
    segmentation_doctor, segmentation_doctor_yop, segmentation_ms, segmentation_ms_yop = calculate_time(segmentation, segmentation_options)

    st.write(f"Разом: Лікар - {segmentation_doctor} хв, {segmentation_doctor_yop} УОП. М/С – {segmentation_ms} хв {segmentation_ms_yop} УОП.")
    if st.button('Зберегти інформацію', key=6):
        df = pd.read_csv("calc_segmentation_methods_1.csv")
        if doctor_name == "":
            st.warning("Будь ласка, введіть лікаря!")
        elif len(segmentation_options) == 0:
            st.warning("Будь ласка, виберіть клінічні етапи!")
        else:
          data = [doctor_name,
                  d5,
                  segmentation_options,
                  segmentation_doctor,
                  segmentation_doctor_yop,
                  segmentation_ms,
                  segmentation_ms_yop
                  ]
          df.loc[len(df)] = data
          df.to_csv('calc_segmentation_methods_1.csv', index=False)
          st.success("Дані були збережні.")

    # df = pd.DataFrame({'numbers': [1, 2, 3], 'colors': ['red', 'white', 'blue']})

    # st.write(df)
    
    #     data = [4, "BLACK"]
    #     some_data.loc[len(some_data)] = data
    #     open('df.csv', 'w').write(some_data.to_csv(index=False))
    # source = pd.DataFrame({
    #         'Price ($)': [10, 15, 20],
    #         'Month': ['January', 'February', 'March']
    #      })
    
    # bar_chart = alt.Chart(source).mark_bar().encode(
    #         y='Price ($):Q',
    #         x='Month:O',
    #     )
    
    # st.altair_chart(bar_chart, use_container_width=True)

    # data_1 = pd.DataFrame({'Лікар': [doctor_1]})
    # st.bar_chart(data_1, width=50)

    st.sidebar.title(f"Welcome {name}")
    authenticator.logout("Logout", "sidebar")


