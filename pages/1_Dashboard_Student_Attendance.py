import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os


FILE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
dir_of_interest = os.path.join(PARENT_DIR, "resources")
IMAGE_PATH = os.path.join(dir_of_interest, "images", "iris.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "student.csv")
st.title("Dashboard - Student Attendance Data")

img = image.imread(IMAGE_PATH)
st.image(img)

df = pd.read_csv(DATA_PATH)
st.dataframe(df)

species = st.selectbox("Select the Species:", df['Sex'].unique())

col1, col2 = st.columns(2)

fig_1 = px.bar(df[df['Sex'] == species], x="Attendance(out of 100)")
col1.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.scatter(df[df['Sex'] == species], y="Attendance(out of 100)")
col2.plotly_chart(fig_2, use_container_width=True)