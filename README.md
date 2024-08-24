# Station Air Quality Dashboard :sunglasses:
## Setup environment - Google Colab
### install streamlit library
```
!pip install streamlit
```
### import library
```
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from babel.numbers import format_currency
import streamlit as st
sns.set(style='white')
```
## Writing dashboard
### read clean dataset
```
dongsi_df = pd.read_csv("https://raw.githubusercontent.com/Myrachel/Proyek-Analisis-Data-Air-Quality-Dataset/main/dongsi_data.csv")
```
### set up data frame
```
def create_monthly_rain_df(df):
    monthly_rain = df.groupby(by="month").agg({"RAIN": "mean"})
    monthly_rain_df = monthly_rain.reset_index()
    monthly_rain_df.rename(columns={
        'month': "Bulan",
        'RAIN': "Curah Hujan (mm)"
        }, inplace=True)
    return monthly_rain_df

def create_monthly_temp_df(df):
    monthly_temp = df.groupby(by="month").agg({"TEMP": "mean"})
    monthly_temp_df = monthly_temp.reset_index()
    monthly_temp_df.rename(columns={
        'month': "Bulan",
        'TEMP': "Temperatur (°C)"
    }, inplace=True)
    return monthly_temp_df

def create_monthly_PM25_df(df):
    monthly_PM25 = df.groupby(by="month").agg({"PM2.5": "mean"})
    monthly_PM25_df = monthly_PM25.reset_index()
    monthly_PM25_df.rename(columns={
        'month': "Bulan",
        'PM2.5': "Indeks PM2.5" #salah satu indeks kualitas udara
    }, inplace=True)
    return monthly_PM25_df

monthly_rain_df = create_monthly_rain_df(dongsi_df)
monthly_temp_df = create_monthly_temp_df(dongsi_df)
monthly_PM25_df = create_monthly_PM25_df(dongsi_df)
```
### set up layout
```
st.set_page_config(
    page_title="Station Air Quality Dashboard",
    page_icon="🚉"
)

st.header('Station Air Quality Dashboard :sunglasses:')
```
### set up content
```
st.sidebar.title("Stasiun")
selected_station = st.sidebar.selectbox("Pilih Stasiun", ["Dongsi", "Stasiun Lain"])

if selected_station == "Dongsi":
    st.subheader('Curah Hujan per Bulan')
    fig, ax = plt.subplots(figsize=(16, 8))
    ax.plot(
        monthly_rain_df["Bulan"],
        monthly_rain_df["Curah Hujan (mm)"],
        marker='o',
        linewidth=2,
        color="#90CAF9"
    )
    ax.tick_params(axis='y', labelsize=20)
    ax.tick_params(axis='x', labelsize=20)
    ax.set_ylim(bottom=0)
    ax.set_xlabel("Bulan", fontsize=25)
    ax.set_ylabel("Curah Hujan (mm)", fontsize=25)
    st.pyplot(fig)

    st.subheader('Temperatur per Bulan')
    fig, ax = plt.subplots(figsize=(16, 8))
    ax.plot(
        monthly_temp_df["Bulan"],
        monthly_temp_df["Temperatur (°C)"],
        marker='o',
        linewidth=2,
        color="#90CAF9"
    )
    ax.tick_params(axis='y', labelsize=20)
    ax.tick_params(axis='x', labelsize=20)
    ax.set_ylim(bottom=0)
    ax.set_xlabel("Bulan", fontsize=25)
    ax.set_ylabel("Temperatur (°C)", fontsize=25)
    st.pyplot(fig)

    st.subheader('Indeks PM2.5 per Bulan')
    fig, ax = plt.subplots(figsize=(16, 8))
    ax.plot(
        monthly_PM25_df["Bulan"],
        monthly_PM25_df["Indeks PM2.5"],
        marker='o',
        linewidth=2,
        color="#90CAF9"
    )
    ax.tick_params(axis='y', labelsize=20)
    ax.tick_params(axis='x', labelsize=20)
    ax.set_ylim(bottom=0)
    ax.set_xlabel("Bulan", fontsize=25)
    ax.set_ylabel("Indeks PM2.5", fontsize=25)
    st.pyplot(fig)

elif selected_station == "Stasiun Lain":
    st.write("Visualisasi untuk stasiun lain akan ditambahkan di sini.")
```
## Run streamlit
```
!streamlit run dashboard.py & npx localtunnel --port 8501
```
copy the network url into the link that appear
