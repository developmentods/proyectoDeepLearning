import streamlit as st
import pickle
import sklearn
from sklearn.metrics import DistanceMetric
import pandas as pd

st.title("Vamos a predecir con el dataset de parkinson")
data = pd.read_csv("dataset\BDParkinson_Prediction.csv")
#st.dataframe(data)

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

predict_button, clear_button = st.columns(2)
predict_clicked = predict_button.button('PREDECIR')

prediction = None

if predict_clicked:
# Validar que todos los campos contengan valores numéricos
    for value in data.values.flatten():
        if not value or not value.isdigit():
            st.warning("Por favor, complete todos los datos con valores numéricos antes de hacer la predicción.")
            break
        else:
            prediction = modelo.predict(data) 
    
    st.success(f"El patrón de flujo es: {prediction[0]}")

    # Crear un diccionario para asociar las predicciones con sus descripciones
    prediction_descriptions = {
        'DB': 'Flujo de burbujas dispersas (DB)',
        'SS': 'Flujo estratificado uniforme (SS)',
        'SW': 'Flujo estratificado ondulado (SW)',
        'A': 'Flujo anular (A)',
        'I': 'Flujo intermitente (I)',
        'B': 'Flujo de burbujas (B)',

    }

    # Mostrar la descripción completa de la predicción
    st.success(prediction_descriptions[prediction[0]])

    if prediction[0] in ["I", "A"]:
        st.warning("Alerta: Presta atención a posibles fallos en la tubería.")