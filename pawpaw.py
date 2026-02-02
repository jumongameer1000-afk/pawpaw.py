import pandas as pd
import streamlit as st
st.title("Student Performance Analysis")
df=pd.read_csv("Analysis.csv")

st.subheader("Dataset Preview")
st.dataframe(df.head())
st.subheader("Dataset Summary")
st.write(df.describe())

if st.button("show Dataset"):
	st.dataframe(df)
min_age=st.slider("select minimum age",0,24,39)
filtered_df=df[df["age"]>=min_age]
st.dataframe(filtered_df) 

df=pd.read_csv("Analysis.csv")
st.dataframe(df)

st.bar_chart(df["name"].value_counts())

st.line_chart(df["score"])

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.hist(df["score"])
st.pyplot(fig)

st.sidebar.title("Navigation")
option = st.sidebar.selectbox(
    "Choose View",
    ["Dataset", "Summary", "Visualizations"]
)

if option == "Dataset":
    st.dataframe(df)

elif option == "Summary":
    st.write(df.describe())

elif option == "Visualizations":
    st.bar_chart(df["department"].value_counts())

st.line_chart(df["score"])

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.hist(df["score"])
st.pyplot(fig)

st.sidebar.title("Navigation")
option = st.sidebar.selectbox(
    "Select View",
    ["Dataset", "Summary", "Visualizations"]
)

if option == "Dataset":
    st.dataframe(df)

elif option == "Summary":
    st.write(df.describe())

elif option == "Visualizations":
    st.bar_chart(df["department"].value_counts())