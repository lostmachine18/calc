import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
import datetime
import pickle
import streamlit_authenticator as stauth
from pathlib import Path
from datetime import date
import plotly.graph_objects as go

from pages.data.table_2 import *

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
  selected_db = st.selectbox("Виберіть необхідну звітність",
                              ['Додаткові методи дослідження',
                              'Етапи виготовлення вінірів з пресованої кераміки',
                              "Етапи виготовлення вкладок з пресованої кераміки",
                              "Етапи виготовлення коронок з пресованої кераміки",
                              "Етапи виготовлення цирконієвих вінірів",
                              "Етапи виготовлення цирконієвих вкладок",
                              "Етапи виготовлення цирконієвих коронок",
                              "Етапи виготовлення цирконієвих мостоподібних протезів"],
                              )
  
  if selected_db == "Додаткові методи дослідження":
      
      df1 = pd.read_csv("calc_axiography_methods_1.csv")
      df1.columns = ["Доктор","Дата","Етапи","Доктор, хв","Доктор, УОП","Молодший персонал, хв","Молодший персонал, УОП"]

      df2 = pd.read_csv("calc_jva_methods_1.csv")
      df2.columns = ["Доктор","Дата","Етапи","Доктор, хв","Доктор, УОП","Молодший персонал, хв","Молодший персонал, УОП"]

      df3 = pd.read_csv("calc_miography_methods_1.csv")
      df3.columns = ["Доктор","Дата","Етапи","Доктор, хв","Доктор, УОП","Молодший персонал, хв","Молодший персонал, УОП"]

      df4 = pd.read_csv("calc_tscan_methods_1.csv")
      df4.columns = ["Доктор","Дата","Етапи","Доктор, хв","Доктор, УОП","Молодший персонал, хв","Молодший персонал, УОП"]


      df5 = pd.read_csv("calc_segmentation_methods_1.csv")
      df5.columns = ["Доктор","Дата","Етапи","Доктор, хв","Доктор, УОП","Молодший персонал, хв","Молодший персонал, УОП"]

      st.subheader("Електронна аксіографія")

      st.write(df1)
      data1 = df1.groupby("Доктор")[["Доктор, хв", "Доктор, УОП",   "Молодший персонал, хв","Молодший персонал, УОП"]].sum().reset_index()
      st.write(data1)

      fig1 = px.bar(data1, x='Доктор', y='Доктор, хв', title='Доктор, загальний час, хв')
      fig1.update_layout(yaxis_title='Доктор, хв')
      st.plotly_chart(fig1)
      
      doctors = df1['Доктор'].unique()

      selected_doctor = st.selectbox("Виберіть лікаря", doctors)
      data2 = df1[df1["Доктор"] == selected_doctor]
      st.write(data2)

      d1 = st.date_input("Виберіть місяць", date.today())
      selected_year = d1.year
      selected_month = d1.month
      data2["Дата"] = pd.to_datetime(data2["Дата"])
      date_filter = (data2['Дата'].dt.year == selected_year) & (data2['Дата'].dt.month == selected_month)
      data3 = data2[date_filter]
      st.write(data3)
      
      
      
      fig2 = px.bar(data3, x='Дата', y='Доктор, хв', title=f'Доктор {selected_doctor}, загальний час, хв')
      fig2.update_layout(yaxis_title='Доктор, хв')
      #fig2.update_layout(xaxis=dict(tickvals=[]))
      data3_sorted = data3.sort_values(by = "Дата")
      data3_sorted['cum'] = data3_sorted['Доктор, хв'].cumsum()

      fig2.add_trace(go.Scatter(x=data3_sorted['Дата'], y=data3_sorted['cum'], line=dict(color='orange'), mode='lines', name='Разом, хв'))
      st.plotly_chart(fig2)

      
      # ------------------JVA---------------------------
      st.subheader("Аналіз вібрацій СНЩС (JVA)")
      st.write(df2)
      data2 = df2.groupby("Доктор")[["Доктор, хв", "Доктор, УОП","Молодший персонал, хв","Молодший персонал, УОП"]].sum().reset_index()
      st.write(data2)

      fig1 = px.bar(data2, x='Доктор', y='Доктор, хв', title='Доктор, загальний час, хв')
      fig1.update_layout(yaxis_title='Доктор, хв')
      st.plotly_chart(fig1)
      
      doctors = df2['Доктор'].unique()

      selected_doctor = st.selectbox("Виберіть лікаря", doctors)
      data2 = df2[df2["Доктор"] == selected_doctor]
      st.write(data2)

      d2 = st.date_input("Виберіть місяць", date.today(), key=2)
      selected_year = d2.year
      selected_month = d2.month
      data2["Дата"] = pd.to_datetime(data2["Дата"])
      date_filter = (data2['Дата'].dt.year == selected_year) & (data2['Дата'].dt.month == selected_month)
      data3 = data2[date_filter]
      st.write(data3)
      
      
      fig2 = px.bar(data3, x='Дата', y='Доктор, хв', title=f'Доктор {selected_doctor}, загальний час, хв')
      fig2.update_layout(yaxis_title='Доктор, хв')
      #fig2.update_layout(xaxis=dict(tickvals=[]))
      data3_sorted = data3.sort_values(by = "Дата")
      data3_sorted['cum'] = data3_sorted['Доктор, хв'].cumsum()

      fig2.add_trace(go.Scatter(x=data3_sorted['Дата'], y=data3_sorted['cum'], line=dict(color='orange'), mode='lines', name='Разом, хв'))
      st.plotly_chart(fig2)


      # ----------------------MIOGRAPHY---------------------
      st.subheader("Електоміографія")
      st.write(df3)

      data1 = df3.groupby("Доктор")[["Доктор, хв", "Доктор, УОП","Молодший персонал, хв","Молодший персонал, УОП"]].sum().reset_index()
      st.write(data1)

      fig1 = px.bar(data1, x='Доктор', y='Доктор, хв', title='Доктор, загальний час, хв')
      fig1.update_layout(yaxis_title='Доктор, хв')
      st.plotly_chart(fig1)
      
      doctors = df3['Доктор'].unique()

      selected_doctor = st.selectbox("Виберіть лікаря", doctors)
      data2 = df3[df3["Доктор"] == selected_doctor]
      st.write(data2)

      d1 = st.date_input("Виберіть місяць", date.today(), key=3)
      selected_year = d1.year
      selected_month = d1.month
      data2["Дата"] = pd.to_datetime(data2["Дата"])
      date_filter = (data2['Дата'].dt.year == selected_year) & (data2['Дата'].dt.month == selected_month)
      data3 = data2[date_filter]
      st.write(data3)
      
      
      
      fig2 = px.bar(data3, x='Дата', y='Доктор, хв', title=f'Доктор {selected_doctor}, загальний час, хв')
      fig2.update_layout(yaxis_title='Доктор, хв')
      #fig2.update_layout(xaxis=dict(tickvals=[]))
      data3_sorted = data3.sort_values(by = "Дата")
      data3_sorted['cum'] = data3_sorted['Доктор, хв'].cumsum()

      fig2.add_trace(go.Scatter(x=data3_sorted['Дата'], y=data3_sorted['cum'], line=dict(color='orange'), mode='lines', name='Разом, хв'))
      st.plotly_chart(fig2)

      # -------------------TSCAN------------------------
      st.subheader("T-SCAN")
      st.write(df4)

      data1 = df4.groupby("Доктор")[["Доктор, хв", "Доктор, УОП","Молодший персонал, хв","Молодший персонал, УОП"]].sum().reset_index()
      st.write(data1)

      fig1 = px.bar(data1, x='Доктор', y='Доктор, хв', title='Доктор, загальний час, хв')
      fig1.update_layout(yaxis_title='Доктор, хв')
      st.plotly_chart(fig1)
      
      doctors = df4['Доктор'].unique()

      selected_doctor = st.selectbox("Виберіть лікаря", doctors, key=55)
      data2 = df4[df4["Доктор"] == selected_doctor]
      st.write(data2)

      d1 = st.date_input("Виберіть місяць", date.today(), key=5)
      selected_year = d1.year
      selected_month = d1.month
      data2["Дата"] = pd.to_datetime(data2["Дата"])
      date_filter = (data2['Дата'].dt.year == selected_year) & (data2['Дата'].dt.month == selected_month)
      data3 = data2[date_filter]
      st.write(data3)
      
      
      
      fig2 = px.bar(data3, x='Дата', y='Доктор, хв', title=f'Доктор {selected_doctor}, загальний час, хв')
      fig2.update_layout(yaxis_title='Доктор, хв')
      #fig2.update_layout(xaxis=dict(tickvals=[]))
      data3_sorted = data3.sort_values(by = "Дата")
      data3_sorted['cum'] = data3_sorted['Доктор, хв'].cumsum()

      fig2.add_trace(go.Scatter(x=data3_sorted['Дата'], y=data3_sorted['cum'], line=dict(color='orange'), mode='lines', name='Разом, хв'))
      st.plotly_chart(fig2)


      st.subheader("Цефалометричний аналіз, сегментація")
      st.write(df5)

      data1 = df5.groupby("Доктор")[["Доктор, хв", "Доктор, УОП","Молодший персонал, хв","Молодший персонал, УОП"]].sum().reset_index()
      st.write(data1)

      fig1 = px.bar(data1, x='Доктор', y='Доктор, хв', title='Доктор, загальний час, хв')
      fig1.update_layout(yaxis_title='Доктор, хв')
      st.plotly_chart(fig1)
      
      doctors = df5['Доктор'].unique()

      selected_doctor = st.selectbox("Виберіть лікаря", doctors)
      data2 = df5[df5["Доктор"] == selected_doctor]
      st.write(data2)

      d1 = st.date_input("Виберіть місяць", date.today(), key=6)
      selected_year = d1.year
      selected_month = d1.month
      data2["Дата"] = pd.to_datetime(data2["Дата"])
      date_filter = (data2['Дата'].dt.year == selected_year) & (data2['Дата'].dt.month == selected_month)
      data3 = data2[date_filter]
      st.write(data3)
      
      
      
      fig2 = px.bar(data3, x='Дата', y='Доктор, хв', title=f'Доктор {selected_doctor}, загальний час, хв')
      fig2.update_layout(yaxis_title='Доктор, хв')
      #fig2.update_layout(xaxis=dict(tickvals=[]))
      data3_sorted = data3.sort_values(by = "Дата")
      data3_sorted['cum'] = data3_sorted['Доктор, хв'].cumsum()

      fig2.add_trace(go.Scatter(x=data3_sorted['Дата'], y=data3_sorted['cum'], line=dict(color='orange'), mode='lines', name='Разом, хв'))
      st.plotly_chart(fig2)
  
  
  if selected_db == "Етапи виготовлення вінірів з пресованої кераміки":
      
      df1 = pd.read_csv("1.csv")
      df1.columns = ["Доктор","Дата", "Тип кострукції", "Кількість", "Етапи","Доктор, хв","Доктор, УОП", "Технік, хв", "Технік, УОП", "Молодший персонал, хв","Молодший персонал, УОП"]
      st.write(df1)

      data1 = df1.groupby("Доктор")[["Доктор, хв", "Доктор, УОП", "Технік, хв", "Технік, УОП",  "Молодший персонал, хв","Молодший персонал, УОП"]].sum().reset_index()
      st.write(data1)

      fig1 = px.bar(data1, x='Доктор', y='Доктор, хв', title='Доктор, загальний час, хв')
      fig1.update_layout(yaxis_title='Доктор, хв')
      st.plotly_chart(fig1)
      
      doctors = df1['Доктор'].unique()

      selected_doctor = st.selectbox("Виберіть лікаря", doctors)
      data2 = df1[df1["Доктор"] == selected_doctor]
      st.write(data2)

      d1 = st.date_input("Виберіть місяць", date.today())
      selected_year = d1.year
      selected_month = d1.month
      data2["Дата"] = pd.to_datetime(data2["Дата"])
      date_filter = (data2['Дата'].dt.year == selected_year) & (data2['Дата'].dt.month == selected_month)
      data3 = data2[date_filter]
      st.write(data3)
      
      
      
      fig2 = px.bar(data3, x='Дата', y='Доктор, хв', title=f'Доктор {selected_doctor}, загальний час, хв')
      fig2.update_layout(yaxis_title='Доктор, хв')
      #fig2.update_layout(xaxis=dict(tickvals=[]))
      data3_sorted = data3.sort_values(by = "Дата")
      data3_sorted['cum'] = data3_sorted['Доктор, хв'].cumsum()

      fig2.add_trace(go.Scatter(x=data3_sorted['Дата'], y=data3_sorted['cum'], line=dict(color='orange'), mode='lines', name='Разом, хв'))
      st.plotly_chart(fig2)

  if selected_db == "Етапи виготовлення вкладок з пресованої кераміки":
      
      df1 = pd.read_csv("2.csv")
      df1.columns = ["Доктор","Дата", "Тип кострукції", "Кількість", "Етапи","Доктор, хв","Доктор, УОП", "Технік, хв", "Технік, УОП", "Молодший персонал, хв","Молодший персонал, УОП"]
      st.write(df1)

      data1 = df1.groupby("Доктор")[["Доктор, хв", "Доктор, УОП", "Технік, хв", "Технік, УОП",  "Молодший персонал, хв","Молодший персонал, УОП"]].sum().reset_index()
      st.write(data1)

      fig1 = px.bar(data1, x='Доктор', y='Доктор, хв', title='Доктор, загальний час, хв')
      fig1.update_layout(yaxis_title='Доктор, хв')
      st.plotly_chart(fig1)
      
      doctors = df1['Доктор'].unique()

      selected_doctor = st.selectbox("Виберіть лікаря", doctors)
      data2 = df1[df1["Доктор"] == selected_doctor]
      st.write(data2)

      d1 = st.date_input("Виберіть місяць", date.today())
      selected_year = d1.year
      selected_month = d1.month
      data2["Дата"] = pd.to_datetime(data2["Дата"])
      date_filter = (data2['Дата'].dt.year == selected_year) & (data2['Дата'].dt.month == selected_month)
      data3 = data2[date_filter]
      st.write(data3)
      
      
      
      fig2 = px.bar(data3, x='Дата', y='Доктор, хв', title=f'Доктор {selected_doctor}, загальний час, хв')
      fig2.update_layout(yaxis_title='Доктор, хв')
      #fig2.update_layout(xaxis=dict(tickvals=[]))
      data3_sorted = data3.sort_values(by = "Дата")
      data3_sorted['cum'] = data3_sorted['Доктор, хв'].cumsum()

      fig2.add_trace(go.Scatter(x=data3_sorted['Дата'], y=data3_sorted['cum'], line=dict(color='orange'), mode='lines', name='Разом, хв'))
      st.plotly_chart(fig2)

  if selected_db == "Етапи виготовлення коронок з пресованої кераміки":
      
      df1 = pd.read_csv("3.csv")
      df1.columns = ["Доктор","Дата", "Тип кострукції", "Кількість", "Етапи","Доктор, хв","Доктор, УОП", "Технік, хв", "Технік, УОП", "Молодший персонал, хв","Молодший персонал, УОП"]
      st.write(df1)

      data1 = df1.groupby("Доктор")[["Доктор, хв", "Доктор, УОП", "Технік, хв", "Технік, УОП",  "Молодший персонал, хв","Молодший персонал, УОП"]].sum().reset_index()
      st.write(data1)

      fig1 = px.bar(data1, x='Доктор', y='Доктор, хв', title='Доктор, загальний час, хв')
      fig1.update_layout(yaxis_title='Доктор, хв')
      st.plotly_chart(fig1)
      
      doctors = df1['Доктор'].unique()

      selected_doctor = st.selectbox("Виберіть лікаря", doctors)
      data2 = df1[df1["Доктор"] == selected_doctor]
      st.write(data2)

      d1 = st.date_input("Виберіть місяць", date.today())
      selected_year = d1.year
      selected_month = d1.month
      data2["Дата"] = pd.to_datetime(data2["Дата"])
      date_filter = (data2['Дата'].dt.year == selected_year) & (data2['Дата'].dt.month == selected_month)
      data3 = data2[date_filter]
      st.write(data3)
      
      
      
      fig2 = px.bar(data3, x='Дата', y='Доктор, хв', title=f'Доктор {selected_doctor}, загальний час, хв')
      fig2.update_layout(yaxis_title='Доктор, хв')
      #fig2.update_layout(xaxis=dict(tickvals=[]))
      data3_sorted = data3.sort_values(by = "Дата")
      data3_sorted['cum'] = data3_sorted['Доктор, хв'].cumsum()

      fig2.add_trace(go.Scatter(x=data3_sorted['Дата'], y=data3_sorted['cum'], line=dict(color='orange'), mode='lines', name='Разом, хв'))
      st.plotly_chart(fig2)
  
  if selected_db == "Етапи виготовлення цирконієвих вінірів":
      
      df1 = pd.read_csv("4.csv")
      df1.columns = ["Доктор","Дата", "Тип кострукції", "Кількість", "Етапи","Доктор, хв","Доктор, УОП", "Технік, хв", "Технік, УОП", "Молодший персонал, хв","Молодший персонал, УОП"]
      st.write(df1)

      data1 = df1.groupby("Доктор")[["Доктор, хв", "Доктор, УОП", "Технік, хв", "Технік, УОП",  "Молодший персонал, хв","Молодший персонал, УОП"]].sum().reset_index()
      st.write(data1)

      fig1 = px.bar(data1, x='Доктор', y='Доктор, хв', title='Доктор, загальний час, хв')
      fig1.update_layout(yaxis_title='Доктор, хв')
      st.plotly_chart(fig1)
      
      doctors = df1['Доктор'].unique()

      selected_doctor = st.selectbox("Виберіть лікаря", doctors)
      data2 = df1[df1["Доктор"] == selected_doctor]
      st.write(data2)

      d1 = st.date_input("Виберіть місяць", date.today())
      selected_year = d1.year
      selected_month = d1.month
      data2["Дата"] = pd.to_datetime(data2["Дата"])
      date_filter = (data2['Дата'].dt.year == selected_year) & (data2['Дата'].dt.month == selected_month)
      data3 = data2[date_filter]
      st.write(data3)
      
      
      
      fig2 = px.bar(data3, x='Дата', y='Доктор, хв', title=f'Доктор {selected_doctor}, загальний час, хв')
      fig2.update_layout(yaxis_title='Доктор, хв')
      #fig2.update_layout(xaxis=dict(tickvals=[]))
      data3_sorted = data3.sort_values(by = "Дата")
      data3_sorted['cum'] = data3_sorted['Доктор, хв'].cumsum()

      fig2.add_trace(go.Scatter(x=data3_sorted['Дата'], y=data3_sorted['cum'], line=dict(color='orange'), mode='lines', name='Разом, хв'))
      st.plotly_chart(fig2)

  if selected_db == "Етапи виготовлення цирконієвих вкладок":
      
      df1 = pd.read_csv("5.csv")
      df1.columns = ["Доктор","Дата", "Тип кострукції", "Кількість", "Етапи","Доктор, хв","Доктор, УОП", "Технік, хв", "Технік, УОП", "Молодший персонал, хв","Молодший персонал, УОП"]
      st.write(df1)

      data1 = df1.groupby("Доктор")[["Доктор, хв", "Доктор, УОП", "Технік, хв", "Технік, УОП",  "Молодший персонал, хв","Молодший персонал, УОП"]].sum().reset_index()
      st.write(data1)

      fig1 = px.bar(data1, x='Доктор', y='Доктор, хв', title='Доктор, загальний час, хв')
      fig1.update_layout(yaxis_title='Доктор, хв')
      st.plotly_chart(fig1)
      
      doctors = df1['Доктор'].unique()

      selected_doctor = st.selectbox("Виберіть лікаря", doctors)
      data2 = df1[df1["Доктор"] == selected_doctor]
      st.write(data2)

      d1 = st.date_input("Виберіть місяць", date.today())
      selected_year = d1.year
      selected_month = d1.month
      data2["Дата"] = pd.to_datetime(data2["Дата"])
      date_filter = (data2['Дата'].dt.year == selected_year) & (data2['Дата'].dt.month == selected_month)
      data3 = data2[date_filter]
      st.write(data3)
      
      
      
      fig2 = px.bar(data3, x='Дата', y='Доктор, хв', title=f'Доктор {selected_doctor}, загальний час, хв')
      fig2.update_layout(yaxis_title='Доктор, хв')
      #fig2.update_layout(xaxis=dict(tickvals=[]))
      data3_sorted = data3.sort_values(by = "Дата")
      data3_sorted['cum'] = data3_sorted['Доктор, хв'].cumsum()

      fig2.add_trace(go.Scatter(x=data3_sorted['Дата'], y=data3_sorted['cum'], line=dict(color='orange'), mode='lines', name='Разом, хв'))
      st.plotly_chart(fig2)

  if selected_db == "Етапи виготовлення цирконієвих коронок":
      
      df1 = pd.read_csv("6.csv")
      df1.columns = ["Доктор","Дата", "Тип кострукції", "Кількість", "Етапи","Доктор, хв","Доктор, УОП", "Технік, хв", "Технік, УОП", "Молодший персонал, хв","Молодший персонал, УОП"]
      st.write(df1)

      data1 = df1.groupby("Доктор")[["Доктор, хв", "Доктор, УОП", "Технік, хв", "Технік, УОП",  "Молодший персонал, хв","Молодший персонал, УОП"]].sum().reset_index()
      st.write(data1)

      fig1 = px.bar(data1, x='Доктор', y='Доктор, хв', title='Доктор, загальний час, хв')
      fig1.update_layout(yaxis_title='Доктор, хв')
      st.plotly_chart(fig1)
      
      doctors = df1['Доктор'].unique()

      selected_doctor = st.selectbox("Виберіть лікаря", doctors)
      data2 = df1[df1["Доктор"] == selected_doctor]
      st.write(data2)

      d1 = st.date_input("Виберіть місяць", date.today())
      selected_year = d1.year
      selected_month = d1.month
      data2["Дата"] = pd.to_datetime(data2["Дата"])
      date_filter = (data2['Дата'].dt.year == selected_year) & (data2['Дата'].dt.month == selected_month)
      data3 = data2[date_filter]
      st.write(data3)
      
      
      
      fig2 = px.bar(data3, x='Дата', y='Доктор, хв', title=f'Доктор {selected_doctor}, загальний час, хв')
      fig2.update_layout(yaxis_title='Доктор, хв')
      #fig2.update_layout(xaxis=dict(tickvals=[]))
      data3_sorted = data3.sort_values(by = "Дата")
      data3_sorted['cum'] = data3_sorted['Доктор, хв'].cumsum()

      fig2.add_trace(go.Scatter(x=data3_sorted['Дата'], y=data3_sorted['cum'], line=dict(color='orange'), mode='lines', name='Разом, хв'))
      st.plotly_chart(fig2)

  if selected_db == "Етапи виготовлення цирконієвих мостоподібних протезів":
      
      df1 = pd.read_csv("7.csv")
      df1.columns = ["Доктор","Дата", "Тип кострукції", "Кількість", "Етапи","Доктор, хв","Доктор, УОП", "Технік, хв", "Технік, УОП", "Молодший персонал, хв","Молодший персонал, УОП"]
      st.write(df1)

      data1 = df1.groupby("Доктор")[["Доктор, хв", "Доктор, УОП", "Технік, хв", "Технік, УОП",  "Молодший персонал, хв","Молодший персонал, УОП"]].sum().reset_index()
      st.write(data1)

      fig1 = px.bar(data1, x='Доктор', y='Доктор, хв', title='Доктор, загальний час, хв')
      fig1.update_layout(yaxis_title='Доктор, хв')
      st.plotly_chart(fig1)
      
      doctors = df1['Доктор'].unique()

      selected_doctor = st.selectbox("Виберіть лікаря", doctors)
      data2 = df1[df1["Доктор"] == selected_doctor]
      st.write(data2)

      d1 = st.date_input("Виберіть місяць", date.today())
      selected_year = d1.year
      selected_month = d1.month
      data2["Дата"] = pd.to_datetime(data2["Дата"])
      date_filter = (data2['Дата'].dt.year == selected_year) & (data2['Дата'].dt.month == selected_month)
      data3 = data2[date_filter]
      st.write(data3)
      
      
      
      fig2 = px.bar(data3, x='Дата', y='Доктор, хв', title=f'Доктор {selected_doctor}, загальний час, хв')
      fig2.update_layout(yaxis_title='Доктор, хв')
      #fig2.update_layout(xaxis=dict(tickvals=[]))
      data3_sorted = data3.sort_values(by = "Дата")
      data3_sorted['cum'] = data3_sorted['Доктор, хв'].cumsum()

      fig2.add_trace(go.Scatter(x=data3_sorted['Дата'], y=data3_sorted['cum'], line=dict(color='orange'), mode='lines', name='Разом, хв'))
      st.plotly_chart(fig2)
  
  st.sidebar.title(f"Welcome {name}")
  authenticator.logout("Logout", "sidebar")