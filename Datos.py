import streamlit as st
st.image('images/banner.png')

st.set_page_config(
    page_title="Áreas Protegidas: Datos.",
    page_icon="🐍",
    layout="wide"
)

st.title("🌿 Análisis de Datos de Áreas Protegidas en nuestro Dataset")
st.markdown("""
En este pequeño proyecto web, exploraremos y analizaremos un conjunto de datos previamente seleccionados que contienen información sobre las áreas protegidas en Argentina.
A través de las diferentes secciones, podrás conocer mejor nuestros datos, visualizar gráficos interactivos, explorar mapas geográficos y participar en encuestas y juegos relacionados con la conservación natural.
Por ahora, te invitamos a navegar por las siguientes secciones para descubrir más sobre nuestro dataset y la importancia de la preservación de nuestras áreas naturales.
Temas a explorar:
* **Explorando nuestros datos:** Inspección y métricas del dataset.
* **Graficamos:** Visualizaciones dinámicas implementadas con Plotly que nos permiten analizar la distribución y características de las áreas protegidas.
* **Mostramos en mapas:** Geolocalización de reservas, parques nacionales y otras áreas protegidas.
* **Reto mental(Juego):** ¡Poné a prueba tus conocimientos sobre la conservación natural argentina con los temas que hemos visto al finalizar!
""")

st.sidebar.success("Para poder empezar, seleccioná una de las páginas de arriba. .")
