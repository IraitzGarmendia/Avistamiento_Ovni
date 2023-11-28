# Librerias
import streamlit as st
import numpy as np
import pandas as pd
from pycaret.regression import load_model, predict_model
import calendar  # Importar el módulo calendar

# Leemos el modelo
model = load_model("modelo_tiempo1")

df = pd.read_csv(r'C:\Users\34650\Desktop\Avistamiento_Ovni\UFO_final_csv.csv')

# Mapeo de nombres de meses a números
meses_numeros = {nombre: num for num, nombre in enumerate(calendar.month_name[1:], start=1)}

# Diccionario de formas de OVNI en castellano
formas_ovni_es = {
    'circle': 'Círculo',
    'triangle': 'Triángulo',
    'light': 'Luz',
    'disk': 'Disco',
    'Fireball': 'Bola de fuego',
    'Unknown': 'Desconocido',
    'Oval': 'Ovalado',
    'Other': 'Otros',
    'Cigar': 'Cigarro',
    'Rectangle': 'Rectangulo',
    'Chevron': 'Compás',
    'Triangle': 'Triángulo',
    'Formation': 'Formacion',
    'No data': 'No data',
    'Delta': 'Delta',
    'Changing': 'Cambiante',
    'Egg': 'Huevo',
    'Diamond': 'Diamante',
    'Flash': 'Flash',
    'Teardrop': 'Lágrima', 
    'Cone': 'Cono',
    'Cross': 'Cros',
    'Pyramid': 'Pirámide',
    'Round': 'Redondo',
    'Crescent': 'Medialuna',
    'Flare': 'Llama',
    'Hexagon': 'Hexagonal',
    'Dome': 'Cúpula'
    
                }

# Título
st.title('Predicción de Duración del Avistamiento de OVNIs')

def predict_duration(month, hour, country, UFO_shape):
    # Convertir el nombre del mes a su número correspondiente
    #mes_numero = meses_numeros[month]
    
    input_data = pd.DataFrame({
        'Month': [m],
        'Hour': [hour],
        'Country': [country],
        'UFO_shape': [UFO_shape]
    })

    # Preprocesar los datos y realizar la predicción
    prediction = model.predict(input_data)[0]
    return prediction

# Añadir controles de entrada

# Cambiado de st.slider a st.selectbox para el mes
# Convertir el nombre del mes a su número correspondiente
meses_espanol = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
month = st.selectbox('Mes', meses_espanol)
hour = st.slider('Hora', df['Hour'].min(), df['Hour'].max(), int(df['Hour'].mean()))
country = st.selectbox('País', df['Country'].unique())
UFO_shape = st.selectbox('Forma de OVNI', list(formas_ovni_es.values()))

# Predecir la duración del avistamiento
if st.button('Predecir Duración'):
    prediction = predict_duration(month, hour, country, UFO_shape)
    st.success(f'La predicción de duración es: {prediction:.2f} segundos')