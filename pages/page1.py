import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


st.set_page_config(page_title="Proyecto Cierre", page_icon="♠")

st.title("Página")
entrada_texto = st.text_input("Text input")

st.success(entrada_texto)
st.date_input("Date input")

st.subheader("Dataset Mnist: ")
minset = pd.read_csv("dataset/mnist1.5k.csv.gz", compression="gzip", header=None).values
st.dataframe(minset)

#st.line_chart(minset)
X=(minset[:,1:785]/255.).astype(np.float32)
y=(minset[:,0]).astype(int)
st.write("dimension de las imagenes y las clases", X.shape, y.shape)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2)
st.write("Separamos en set de entrenamiento y test: X_train, y_train, X_test, y_test")
st.write(X_train.shape, y_train.shape, X_test.shape, y_test.shape)


