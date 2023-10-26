import streamlit as st
import pandas as pd
import altair as alt
import datetime
import pickle
import streamlit_authenticator as stauth
from pathlib import Path

# --- USER AUTH -------------------------

names = ['admin']
usernames = ['admin']

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

    st.header("Додаткові методи дослідження в цифровій стоматології")
    st.subheader("Хвилини та УОПи")
    st.caption("Електронна аксіографія")

    doctor_1 = 0
    yop_doctor_1 = 0
    ms_1 = 0
    yop_ms_1 = 0
    doctor_2 = 0
    yop_doctor_2 = 0
    ms_2 = 0
    yop_ms_2 = 0

    d = st.date_input("Дата проведення", datetime.date(2023, 10, 10))
    st.write('Дата проведення:', d)

    some_data = pd.read_csv("df.csv")
    st.write(some_data)

    options_1 = st.multiselect(
        'Клінічні етапи',
        ['Заповнення документації',
        'Первинне обстеження і підготовка до дослідження',
        'Адаптація параоклюзійної прикусної вилки',
        'Підключення і калібрування аксіографа',
        'Власне реєстраціярухів нижньої щелепи',
        'Зняття пристроя і очищення зубіd пацієнта',
        'Аналіз отриманих даних та підготовка заключення'],
        [])

    if 'Заповнення документації' in options_1:
        doctor_1 += 5
        yop_doctor_1 += 0.08
        ms_1 += 1.7
        yop_ms_1 += 0.02 

    if 'Первинне обстеження і підготовка до дослідження' in options_1:
        doctor_1 += 10
        yop_doctor_1 += 0.16
        ms_1 += 3.3
        yop_ms_1 += 0.05

    if 'Адаптація параоклюзійної прикусної вилки' in options_1:
        doctor_1 += 30
        yop_doctor_1 += 0.5
        ms_1 += 10
        yop_ms_1 += 0.16

    if 'Підключення і калібрування аксіографа' in options_1:
        doctor_1 += 15
        yop_doctor_1 += 0.25
        ms_1 += 5
        yop_ms_1 += 0.08

    if 'Власне реєстраціярухів нижньої щелепи' in options_1:
        doctor_1 += 30
        yop_doctor_1 += 0.5
        ms_1 += 10
        yop_ms_1 += 0.16

    if 'Зняття пристроя і очищення зубіd пацієнта' in options_1:
        doctor_1 += 15
        yop_doctor_1 += 0.25
        ms_1 += 5
        yop_ms_1 += 0.08

    if 'Аналіз отриманих даних та підготовка заключення' in options_1:
        doctor_1 += 60
        yop_doctor_1 += 1
        ms_1 += 20
        yop_ms_1 += 0.33

    yop_doctor_1 = round(yop_doctor_1, 2)
    yop_ms_1 = round(yop_ms_1, 2)

    st.write(f"Разом: Лікар - {doctor_1} хв, {yop_doctor_1} УОП. М/С – {ms_1} хв {yop_ms_1} УОП.")

    st.caption("Аналіз вібрацій СНЩС (JVA)")


    date_2 = st.date_input("Дата проведення", datetime.date(2023, 10, 11))
    st.write('Дата проведення:', date_2)

    options_2 = st.multiselect(
        'Клінічні етапи',
        ['Заповнення документації',
        'Первинне обстеження і підготовка до дослідження',
        'Оцінка ступеня відкривання рота та рухів нижньої щелепи',
        'Запис даних прибором',
        'Аналіз отриманих даних і підготовка заключення'],
        [])

    if 'Заповнення документації' in options_2:
        doctor_2 += 15
        yop_doctor_2 += 0.25
        ms_2 += 5
        yop_ms_2 += 0.08 

    if 'Первинне обстеження і підготовка до дослідження' in options_2:
        doctor_2 += 15
        yop_doctor_2 += 0.25
        ms_2 += 5
        yop_ms_2 += 0.08

    if 'Оцінка ступеня відкривання рота та рухів нижньої щелепи' in options_2:
        doctor_2 += 10
        yop_doctor_2 += 0.16
        ms_2 += 3.3
        yop_ms_2 += 0.05

    if 'Запис даних прибором' in options_2:
        doctor_2 += 15
        yop_doctor_2 += 0.25
        ms_2 += 5
        yop_ms_2 += 0.08

    if 'Аналіз отриманих даних і підготовка заключення' in options_2:
        doctor_2 += 30
        yop_doctor_2 += 0.5
        ms_2 += 10
        yop_ms_2 += 0.16

    yop_doctor_2 = round(yop_doctor_2, 2)
    yop_ms_2 = round(yop_ms_2, 2)

    st.write(f"Разом: Лікар - {doctor_2} хв, {yop_doctor_2} УОП. М/С – {ms_2} хв {yop_ms_2} УОП.")

    df = pd.DataFrame({'numbers': [1, 2, 3], 'colors': ['red', 'white', 'blue']})

    st.write(df)
    if st.button('save dataframe'):
        data = [4, "BLACK"]
        some_data.loc[len(some_data)] = data
        open('df.csv', 'w').write(some_data.to_csv(index=False))
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

    authenticator.logout("Logout", "sidebar")
    st.sidebar.title(f"Welcome {name}")