import streamlit as st
import pickle
import sklearn
from sklearn.metrics import DistanceMetric

st.title("Vamos a predecir con el dataset de parkinson")


@st.cache_resource
def  cargar_modelo(modelName):
  with open(f'models\{modelName}.pkl', 'rb') as archivo:
    modelo = pickle.load(archivo)
  return modelo

model_text = st.selectbox("Select Slider", options=["KNN", "MLP"])

model = None
try:
  if model_text == "KNN":
    st.write("modelKNN")
    modelo = cargar_modelo("modelKNN")
  elif model_text == "MLP":
    st.write("modelMLP")
    modelo = cargar_modelo("modelMLP")

  st.sidebar.success(f"Modelo {model_text} cargado correctamente")

  print(modelo)
except:
  st.sidebar.error(f"Modelo {model_text} no encontrado")

