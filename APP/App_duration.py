# Librerias
import streamlit as st
import numpy as np
import pandas as pd
from pycaret.regression import load_model, predict_model
import calendar  # Importar el módulo calendar

# Leemos el modelo
model = load_model("modelo_tiempo1")

df = pd.read_csv(r'C:\Users\34650\Desktop\proyecto 3\Temario\Ovnis\UFO_final_csv.csv')

meses_numeros = {nombre: num for num, nombre in enumerate(calendar.month_name[1:], start=1)}

# Titulo
st.title('Predicción de Duración del Avistamiento de OVNIs')

def predict_duration(month, hour, country, UFO_shape):
    # Convertir el nombre del mes a su número correspondiente
    mes_numero = meses_numeros[month]
    
    input_data = pd.DataFrame({
        'Month': [mes_numero],
        'Hour': [hour],
        'Country': [country],
        'UFO_shape': [UFO_shape]
    })

    # Preprocesar los datos y realizar la predicción
    prediction = model.predict(input_data)[0]
    return prediction

# Añadir controles de entrada
# Convertir el nombre del mes a su número correspondiente

meses = list(calendar.month_name[1:])
month = st.selectbox('Mes', meses)
hour = st.slider('Hora', df['Hour'].min(), df['Hour'].max(), int(df['Hour'].mean()))
country = st.selectbox('País', df['Country'].unique())
UFO_shape = st.selectbox('Forma de OVNI', df['UFO_shape'].unique())

# Predecir la duración del avistamiento
if st.button('Predecir Duración'):
    prediction = predict_duration(month, hour, country, UFO_shape)
    st.success(f'La predicción de duración es: {prediction:.2f} segundos')