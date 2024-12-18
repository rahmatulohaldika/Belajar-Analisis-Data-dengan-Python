import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set(style='dark')

dongsi_df = pd.read_csv('dongsi_pm25.csv')
all_df = pd.read_csv('all_pm25.csv')

st.header('Kualitas Udara Sesuai Kadar PM2.5')

st.subheader('Perbandingan Kadar PM2.5 di Station Dongsi pada Tahun 2015 dan 2016')
fig, ax = plt.subplots(figsize=(15, 6))

colors = ['#D3D3D3', '#72BCD4']

sns.barplot(x='year', y='PM2.5', data=dongsi_df, palette=colors)
ax.set_ylabel('PM2.5')
ax.set_xlabel('Year', fontsize=15)
ax.set_title('Average PM2.5 in Dongsi', loc='center', fontsize=20)
ax.tick_params(axis='y', labelsize=12)


plt.tight_layout()
st.pyplot(fig)


st.subheader('Daftar Station Berdasarkan Kadar PM2.5 Pada Tahun 2013 - 2017')
fig, ax = plt.subplots(figsize=(15, 6))

colors = ['#D3D3D3', '#72BCD4', '#D3D3D3', '#D3D3D3', '#D3D3D3', '#D3D3D3', '#D3D3D3', '#D3D3D3', '#D3D3D3', '#D3D3D3', '#D3D3D3']

sns.barplot(x='PM2.5', y='station', data=all_df, palette=colors)
ax.set_ylabel('Station')
ax.set_xlabel('PM2.5', fontsize=15)
ax.set_title('Average PM2.5 in All Station', loc='center', fontsize=20)
ax.tick_params(axis='y', labelsize=12)

plt.tight_layout()
st.pyplot(fig)