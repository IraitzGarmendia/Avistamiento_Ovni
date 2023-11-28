#-----------------------------LIBRERIAS-----------------------------
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import plotly_express as px
import streamlit.components.v1 as components
from pycaret.regression import load_model, predict_model
import calendar

#-----------------CONFIGURACION DE PAGINA--------------------------

st.set_page_config(page_title="Cazadores de OVNIs" , layout="wide", page_icon="🛸", initial_sidebar_state="collapsed")

#----------------------LECTURA DEL CSV------------------------------------------

df = pd.read_csv(r"C:\Users\34650\Desktop\proyecto 3\Temario\Ovnis\UFO_final_csv.csv")

#----------------------EMPIEZA NUESTRA APP------------------------------------------

# Título
st.markdown("<h1 style='color: white; font-size: 4em;'>Cazadores de OVNIs 👽</h1>", unsafe_allow_html=True)

# Imagen de portada
imagen_portada_path = "Fotos/OvniPortada.png"
st.image(imagen_portada_path, caption="Explorando el misterioso mundo de los OVNIs", width=900)

# Texto de presentación
st.write(
    "**¡Bienvenidos a nuestro proyecto de análisis de avistamientos de OVNIs!** "
    "**Exploramos datos recopilados a lo largo del tiempo para descubrir patrones, tendencias y misterios en el cielo**."
)

#----------------------SECCIONES------------------------------------------

# Nueva Sección 0: Introducción
with st.expander("Introducción"):
    st.markdown("## Introducción al Proyecto")

    # Texto de introducción
    st.write(
        "Integrantes: Somos **Iraitz Garmendia**, **Jaime Vecina** y **Javier Muñoz**, tres estudiantes del bootcamp de analítica de datos de **Upgrade Hub** que venimos a presentaros nuestro proyecto final."
        "\n\n"
        "Tema: El tema elegido para este proyecto son los **OVNIs** y para ello hemos seleccionado un conjunto de datos extraído de Kaggle correspondiente a los datos de **NUFORC**, que consta de más de 80k datos en 16 columnas sobre avistamientos en diferentes países desde **1906 hasta 2014**. Entre sus columnas encontramos datos sobre las coordenadas, fechas, tipo de objeto, descripción."
        "\n\n"
        "Objetivo: El **objetivo** de nuestro análisis ha sido ver las épocas del año, horarios y fechas donde se podría ver los diferentes tipos de ovnis en base a unas coordenadas, centrándonos en **España**."
    )

    # Imagen introduccion
    imagen_introduccion_path = "Fotos/OvniIntroduccion.png"  # Ruta de la imagen
    st.image(imagen_introduccion_path, caption="",width=900)

# Nueva Sección 1: Contexto
with st.expander("Contexto"):
    st.markdown("")

    # Ruta a la imagen PNG
    Contexto_path = "Fotos/Contexto.png"  # Ruta de la imagen

    # Mostrar la imagen
    st.image(Contexto_path, caption="", width=900, use_column_width=False)

# Nueva Sección 2: Datos interesantes
with st.expander("Datos interesantes"):
    st.markdown("")

    # Ruta a la imagen PNG
    Datos_interesantes_path = "Fotos/Datos interesantes.png"  # Ruta de la imagen

    # Mostrar la imagen
    st.image(Datos_interesantes_path, caption="", width=900, use_column_width=True)

# Nueva Sección 3: Eventos
with st.expander("Eventos"):
    st.markdown("")

    # Ruta a la imagen PNG
    eventos_path = "Fotos/Eventos.png"  # Ruta de la imagen

    # Mostrar la imagen
    st.image(eventos_path, caption="Eventos", width=900, use_column_width=True)

# Nueva Sección 4: Mapas
with st.expander("Mapas"):
    st.markdown("### Mapa de calor")

    # Ruta al primer archivo HTML del mapa
    heatmap_html_path = "Fotos/heatmap.html"

    # Mostrar el primer mapa interactivo directamente desde el archivo HTML usando st.components.v1.html
    st.components.v1.html(open(heatmap_html_path, "r", encoding="utf-8").read(), width=1080, height=500, scrolling=False)
    st.markdown("")
    st.text("- Estados Unidos cuenta con más de 70.000 avistamientos")

    # Ruta al segundo archivo HTML del mapa
    bolamundo_html_path = "Fotos/mundo.html"

    # Mostrar el segundo mapa interactivo directamente desde el archivo HTML usando st.components.v1.html
    st.components.v1.html(open(bolamundo_html_path, "r", encoding="utf-8").read(), width=1090, height=600, scrolling=False)
    st.markdown("### Europa")
    st.text("- Reino Unido cuenta con un total de 2348 avistamientos")
    st.text("- Europa cuenta con 985")


    # Ruta al tercer archivo HTML del mapa
    Europa_html_path = "Fotos/Europa.html"

    # Mostrar el tercer mapa interactivo directamente desde el archivo HTML usando st.components.v1.html
    st.components.v1.html(open(Europa_html_path, "r", encoding="utf-8").read(), width=1080, height=600, scrolling=False)

    st.markdown("### España")
    st.text("Total de 74 avistamientos")

    # Ruta al cuarto archivo HTML del mapa
    España_html_path = "Fotos/España.html"

    # Mostrar el tercer mapa interactivo directamente desde el archivo HTML usando st.components.v1.html
    st.components.v1.html(open(España_html_path, "r", encoding="utf-8").read(), width=1080, height=600, scrolling=False)

# Nueva Sección 5: España y Andalucía
with st.expander("España y Andalucía"):
    st.markdown("")

    # Dividimos el espacio en dos columnas
    col1, col2 = st.columns(2)

    # Ruta a la imagen PNG
    eventos_path = "Fotos/Avistamientos por provincia.png"  # Ruta de la imagen

    # Mostrar la imagen en la primera columna con ancho fijo
    col1.image(eventos_path, caption="", width=550, use_column_width=True)

        # Ruta a la imagen PNG
    eventos_path = "Fotos/Avistamientos Andalucia.png"  # Ruta de la imagen

    # Mostrar la imagen
    col2.image(eventos_path, caption="", width=550, use_column_width=True)

# Nueva Sección 6: Época y mes
with st.expander("Época y mes"):
    st.markdown("")

    # Dividimos el espacio en dos columnas
    col1, col2 = st.columns(2)

    # Ruta a la imagen PNG para la época del año
    imagen_epoca_path = "Fotos/Época del año.png"  # Ruta de la imagen

    # Mostrar la imagen
    col1.image(imagen_epoca_path, caption="", width=550, use_column_width=True)

    # Ruta a la imagen PNG para el mes del año
    imagen_mes_path = "Fotos/Mes del año.png"  # Ruta de la imagen

    # Mostrar la imagen
    col2.image(imagen_mes_path, caption="", width=550, use_column_width=True)

# Nueva Sección 7: Día y hora
with st.expander("Día y hora"):
    st.markdown("")

    # Dividimos el espacio en dos columnas
    col1, col2 = st.columns(2)

    # Ruta a la imagen PNG
    eventos_path = "Fotos/Día de la semana.png"  # Ruta de la imagen

    # Mostrar la imagen
    col1.image(eventos_path, caption="", width=550, use_column_width=True)

        # Ruta a la imagen PNG
    eventos_path = "Fotos/Horas del dia.png"  # Ruta de la imagen

    # Mostrar la imagen
    col2.image(eventos_path, caption="", width=550, use_column_width=True)

# Nueva Sección 8: Tipos de ovnis
with st.expander("Tipos de OVNIs"):
    st.markdown("")

    # Dividimos el espacio en dos columnas
    col1, col2 = st.columns(2)

    # Ruta a la imagen PNG
    tipos_ovnis_png_path = "Fotos/Tipos Ovnis Treemap.png"

    # Mostrar el otro gráfico interactivo directamente desde el archivo HTML usando st.components.v1.html
    col1.image(tipos_ovnis_png_path, caption="", width=550, use_column_width=True)

    # Ruta a la imagen PNG
    imagen_top5_ovnis_path = "Fotos/T-5-OVNIs.png"  # Ruta de la imagen

    # Mostrar la imagen
    col2.image(imagen_top5_ovnis_path, caption="", width=550, use_column_width=True)

# Nueva Sección 9: Aplicación de predicción de duración de avistamiento de OVNIs
with st.expander('Aplicación de predicción'):
    st.markdown("## Predicción de duración del avistamiento de OVNIs")
    
    meses_numeros = {nombre: num for num, nombre in enumerate(calendar.month_name[1:], start=1)}

    # Leemos el modelo
    model = load_model("modelo_tiempo1")

    # Añadir controles de entrada
    meses = list(calendar.month_name[1:])
    month = st.selectbox('Mes', meses)
    hour = st.slider('Hora', df['Hour'].min(), df['Hour'].max(), int(df['Hour'].mean()))
    country = st.selectbox('País', df['Country'].unique())
    UFO_shape = st.selectbox('Forma de OVNI', df['UFO_shape'].unique())

    # Función para predecir la duración del avistamiento
    def predict_duration(month, hour, country, UFO_shape):
        mes_numero = meses_numeros[month]
        input_data = pd.DataFrame({
            'Month': [mes_numero],
            'Hour': [hour],
            'Country': [country],
            'UFO_shape': [UFO_shape]
        })
        prediction = model.predict(input_data)[0]
        return prediction

    # Predecir la duración del avistamiento al hacer clic en el botón
    if st.button('Predecir Duración'):
        prediction = predict_duration(month, hour, country, UFO_shape)
        st.success(f'La predicción de duración es: {prediction:.2f} segundos')


# Nueva Sección 10: Área 51
with st.expander("Área 51"):
    # Agregamos el texto explicativo
    st.markdown("### **Información sobre el Área 51**:")
    st.write(
        "Instalación militar ubicada en la región desértica de **Nevada**, suroeste de EEUU."
        "\n\n"
        "Fue establecida durante la **guerra fría**."
        "\n\n"
        "La existencia fue mantenida en secreto durante mucho tiempo y generó teorías de conspiración, como la presunta presencia de **naves espaciales no identificadas** (OVNIs)."
    )

    # Mostrar el mapa (HTML)
    area51_html_path = "Fotos/Area51.html"
    st.components.v1.html(open(area51_html_path, "r", encoding="utf-8").read(), width=900, height=400, scrolling=False)

# Nueva Sección 11: Minería de datos
with st.expander("Minería de datos"):
    st.markdown("")

    # Dividimos el espacio en dos columnas
    col1, col2= st.columns(2)

    # Ruta a la imagen PNG
    eventos_path = "Fotos/Mineria.png"  # Ruta de la imagen

    # Mostrar la imagen en la primera columna
    col1.image(eventos_path, caption="", width=800, use_column_width=True)

    # Conclusiones en la segunda columna
    col2.markdown("### **CONCLUSIONES**:")
    col2.write(
        "CONCLUSION 1."
        "\n\n"
        "CONCLUSION 2."
        "\n\n"
        "CONCLUSION 3."
    )

# Ruta al archivo CSV para almacenar las respuestas
ruta_csv_respuestas = "respuestas_encuesta.csv"

# Nueva Sección 11: Encuesta
with st.expander("Encuesta"):

    # Solicitamos el nombre del usuario
    st.subheader("¿Cómo te llamas?")
    nombre_usuario = st.text_input("Introduce tu nombre y apellidos:", "")

    # Pregunta 1
    st.subheader("Pregunta 1: ¿Crees que realmente existen los OVNIs?")
    respuesta_pregunta_1 = st.radio("Opciones:", ["Sí", "No", "No sé qué es un OVNI"])

    # Pregunta 2
    st.subheader("Pregunta 2: Si fueras un OVNI, ¿de qué tipo serías?")
    respuesta_pregunta_3 = st.radio("Opciones:", ["Bola de Fuego", "Disco", "Triangular", "Cono", "Otro"])

    # Pregunta 3
    st.subheader("Pregunta 3: ¿Crees que hay alienígenas en el Área 51?")
    respuesta_pregunta_2 = st.radio("Opciones:", ["Sí", "No", "No existe ese lugar"])

    # Solicitamos un testimonio de avistamiento
    st.subheader("Pregunta 4: ¿Alguna vez has visto un OVNI? ")
    testimonio = st.text_input("Cuéntanos tu experiencia", "")

    # Pregunta 4
    st.subheader("Pregunta 5: ¿Puntúa del 1 al 10 este proyecto?")
    respuesta_pregunta_5 = st.slider("Selecciona tu puntuación:", min_value=1, max_value=10)

    # Botón para enviar las respuestas de la encuesta
    if st.button("Enviar Respuestas de la Encuesta"):
        # Muestra las respuestas del usuario actual
        st.success(f"Respuestas de {nombre_usuario}:")
        st.success(f"Pregunta 1: {respuesta_pregunta_1}")
        st.success(f"Pregunta 2: {respuesta_pregunta_2}")
        st.success(f"Pregunta 3: {respuesta_pregunta_3}")
        st.success(f"Pregunta 4: {testimonio}")
        st.success(f"Pregunta 5: {respuesta_pregunta_5}")
        
        st.markdown("<h3 style='color: white; font-size: 2em;'>Muchas gracias y hasta la próxima 🖖</h3>", unsafe_allow_html=True)

        # Almacena las respuestas en un archivo CSV
        with open(ruta_csv_respuestas, 'a', encoding='utf-8', newline='') as file:
            file.write(f"{nombre_usuario},{respuesta_pregunta_1},{respuesta_pregunta_2},{respuesta_pregunta_3},{testimonio},{respuesta_pregunta_5}\n")

#----------------------SIDEBAR------------------------------------------
# Título de la barra lateral
st.sidebar.markdown("<h1 style='color: white; text-decoration: underline;'><strong>Explora los Datos</strong></h1>", unsafe_allow_html=True)

# Mensaje en el sidebar
st.sidebar.markdown(
    "<p style='color: white; font-size: 18px;'>¿Sabías que el 88% de los avistamientos registrados son en Estados Unidos? 🛸🌌</p>",
    unsafe_allow_html=True
)

# Ruta a las imágenes PNG
imagen_triangular_path = "Fotos/Ovni triangular.png"
imagen_posibles_conos_path = "Fotos/Posibles conos.jpg"
imagen_disco_path = "Fotos/Ovni disco.jpg"
imagen_oval_path = "Fotos/Oval.png"
imagen_bola_de_fuego_path = "Fotos/Ovni Bola de fuego.png"

# Nueva Sección en la barra lateral: Tipos de ovnis e Imágenes
st.sidebar.markdown("---")
st.sidebar.markdown("## Tipos de OVNIs")

# Botón desplegable para seleccionar el tipo de OVNI
selected_ovni_type = st.sidebar.selectbox("Selecciona un tipo de OVNI", ["Triangular", "Conos","Disco","Ovalo","Bola de Fuego"])

# Creamos un diccionario que asocia el tipo de OVNI con su respectiva imagen
ovni_images = {
    "Triangular": imagen_triangular_path,
    "Conos": imagen_posibles_conos_path,
    "Disco": imagen_disco_path,
    "Ovalo": imagen_oval_path,
    "Bola de Fuego": imagen_bola_de_fuego_path,
}
st.sidebar.image(ovni_images[selected_ovni_type], caption=f"Ovni {selected_ovni_type}", width=300)

# Nueva Sección en la barra lateral: Datos Estadísticos con Filtro de Años
st.sidebar.markdown("---")
st.sidebar.markdown("## Avistamientos por Años")

# Filtro de años
selected_years = st.sidebar.slider("Selecciona un rango de años", min_value=df['Year'].min(), max_value=df['Year'].max(), value=(df['Year'].min(), df['Year'].max()))

# Botón para mostrar datos estadísticos
if st.sidebar.button("Resultados"):
    st.sidebar.markdown(f"({selected_years[0]} - {selected_years[1]})")

    # Frecuencia de avistamientos por año en el rango seleccionado
    df_filtered_by_years = df[(df['Year'] >= selected_years[0]) & (df['Year'] <= selected_years[1])]
    avistamientos_por_año = df_filtered_by_years['Year'].value_counts()

    # Ordenamos los años en el rango seleccionado
    años_ordenados = sorted(avistamientos_por_año.index)
    color_palette = sns.color_palette("Spectral", n_colors=len(años_ordenados))[::-1]
    plt.style.use('dark_background')

    # Creamos la gráfica de barras para el rango seleccionado
    plt.figure(figsize=(12, 8))
    avistamientos_por_año.loc[años_ordenados].plot(kind='bar', color=color_palette)
    plt.title(f'Número de Avistamientos de Ovnis ({selected_years[0]}-{selected_years[1]})', fontsize=20, y=1.1)
    plt.xlabel('Año')
    plt.ylabel('Número de Avistamientos')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    st.sidebar.pyplot(plt)

# Contenido adicional al final del sidebar
st.sidebar.markdown("---")
st.sidebar.markdown("### ¡Gracias por explorar el mundo de los OVNIs con nosotros! 👽")
st.sidebar.markdown("Si te ha gustado nuestro proyecto, ¡compártelo!✨")

# Enlace a LinkedIn - Iraitz Garmendia Alberdi
st.sidebar.markdown(f"[![LinkedIn - Iraitz Garmendia Alberdi](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/iraitz-garmendia-alberdi-5ba782276/)")
st.sidebar.text("Iraitz Garmendia Alberdi")
# Enlace a LinkedIn - Jaime Vecina Montesinos
st.sidebar.markdown(f"[![LinkedIn - Jaime Vecina Montesinos](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jaime-vecina-montesinos-b372802a0/)")
st.sidebar.text("Jaime Vecina Montesinos")
# Enlace a LinkedIn - Javier Muñoz Ballesteros
st.sidebar.markdown(f"[![LinkedIn - Javier Muñoz Ballesteros](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/javier-munoz-ballesteros/)")
st.sidebar.text("Javier Muñoz Ballesteros")


# Fuentes
st.sidebar.markdown("---")
st.sidebar.markdown("### Fuentes")
st.sidebar.markdown(f"https://nuforc.org/")
st.sidebar.markdown(f"https://www.kaggle.com/datasets/NUFORC/ufo-sightings")
st.sidebar.markdown(f"https://creativecommons.org/licenses/by-nc/3.0/")
st.sidebar.markdown(f"https://es.quora.com/Cu%C3%A1l-fue-la-primera-fotograf%C3%ADa-de-un-ovni")
