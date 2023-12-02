import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


st.set_page_config(page_title="Proyecto Cierre", page_icon="♠")

st.title("EDA")

file = st.file_uploader("Sube un archivo .csv", type=["csv"])

def plot_histograma(column, title):
    plt.figure(figsize=(10,5))
    plt.hist(data[column], bins=20, color='skyblue', edgecolor='black')
    plt.title(title)
    plt.xlabel(column)
    plt.ylabel('Frequency')
    return plt

def box_plot(column, title):
    plt.figure(figsize=(10,5))
    plt.boxplot(data[column])
    plt.title(title)
    plt.xlabel(column)
    plt.ylabel('Frequency')
    return plt

if file is not None:
    data = pd.read_csv(file)
    st.dataframe(data)

    st.header("Análisis exploratorio de datos - EDA")

    st.subheader("Descripción de los datos")
    st.dataframe(data.describe())
    #st.dataframe(data.corr())
    st.markdown("---")

    st.subheader("Frecuencia por clase")
    st.write(data["CLASS"].value_counts())

    ax = data['CLASS'].value_counts().plot(kind='bar')
    ax.set_title('Clases')
    ax.set_ylabel('Frecuencia')

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.write("Histograma")
        selected_column = st.selectbox("seleccione una columna", data.columns)
        st.pyplot(plot_histograma(selected_column, f"Histograma de {selected_column}"))
    with col2:
        st.write("Boxplot")
        selected_column = st.selectbox("seleccione otra columna", data.columns)
        st.pyplot(box_plot(selected_column, f"Histograma de {selected_column}"))
