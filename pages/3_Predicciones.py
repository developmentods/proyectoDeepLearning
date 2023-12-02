import streamlit as st
import pickle

st.title("Vamos a predecir con el dataset de parkinson")

with open('models\modelKNN.pkl', 'rb') as archivo:
  modelMLP_cargado = pickle.load(archivo)