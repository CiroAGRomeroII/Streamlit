import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Áreas Protegidas: Juego.",
    page_icon="🐍",
    layout="wide"
)

st.title("Reto mental - Juego de preguntas")
st.write("¡Bienvenido al reto mental! Pon a prueba tus conocimientos sobre las áreas protegidas de Argentina.")
st.write("¿Podrás responder correctamente a todas las preguntas y demostrar tu conocimiento sobre la conservación natural? ¡Vamos a descubrirlo!")

try:
    protegida = pd.read_csv("area_protegida.csv")
except FileNotFoundError:
    pass

preguntas = [
    {
        "pregunta": "¿Qué organismo estatal concentra la mayor cantidad de registros dentro del dataset con un total de 342 áreas?",
        "opciones": ["MAyDS", "IGN", "APN"],
        "correcta": 1
    },
    {
        "pregunta": "¿Cuál es el área protegida que registra la mayor superficie total acumulada en todo el archivo (58.234.860)?",
        "opciones": ["Yaganes", "Patagonia Azul", "Namuncura - Banco Burdwood"],
        "correcta": 0
    },
    {
        "pregunta": "¿Cuántos registros del dataset no tienen cargado su correspondiente documento legal en la columna fdc?",
        "opciones": ["27 registros", "1 registro", "59 registros"],
        "correcta": 2
    },
    {
        "pregunta": "¿Cuál es la categoría de conservación que más superficie acumula en el gráfico de barras del dataset (114.830.836)?",
        "opciones": ["Reserva de Biósfera", "Sitio Ramsar", "Área Marina Protegida"],
        "correcta": 2
    },
    {
        "pregunta": "¿Cuál es el valor exacto de superficie que figura para la reserva más pequeña del archivo (Vicente López)?",
        "opciones": ["59", "27", "342"],
        "correcta": 1
    },
    {
        "pregunta": "¿Cuántos puntos o parques nacionales quedaron marcados en el mapa según sus coordenadas específicas de latitud y longitud?",
        "opciones": ["15 puntos", "37 puntos", "395 puntos"],
        "correcta": 1
    },
    {
        "pregunta": "¿Qué valor aproximado arroja el promedio de superficie por registro al analizar el tamaño general del dataset?",
        "opciones": ["1.245.242,33", "491.870.721", "31.702.666"],
        "correcta": 0
    },
    {
        "pregunta": "¿Cuántas áreas protegidas en total sumaron una superficie menor al promedio real calculado en el archivo?",
        "opciones": ["197 áreas", "52 áreas", "331 áreas"],
        "correcta": 2
    },
    {
        "pregunta": "¿Qué porcentaje aproximado sobre el total representan los 59 registros que no tienen el documento legal cargado?",
        "opciones": ["14.94%", "21.52%", "6.34%"],
        "correcta": 0
    },
    {
        "pregunta": "Además de Yaganes y Namuncurá, ¿cuál es la tercera área con mayor superficie citada en el informe de nuestro tablero (30.553.073)?",
        "opciones": ["Patagonia Azul", "Parque Nacional Perito Moreno", "Área Natural Protegida Sierras de Belén"],
        "correcta": 0
    },
]

for i, p in enumerate(preguntas):
    st.subheader(f"Pregunta {i + 1}")
    st.write(p["pregunta"])

    eleccion = st.radio(
        "Elegí una opción:",
        p["opciones"],
        key=f"pregunta_{i}",
        index=None,
    )

    if st.button("Verificar", key=f"btn_{i}"):
        if eleccion is None:
            st.warning("⚠️ Elegí una opción antes de verificar.")
        elif eleccion == p["opciones"][p["correcta"]]:
            st.balloons()
            st.success("¡Ganaste! Felicidades, tu respuesta es correcta. 🎉")
        else:
            correcta = p["opciones"][p["correcta"]]
            st.error(f"❌ Perdiste. ¡La respuesta correcta es: {correcta}! Sigue intentando, ¡no te desanimes! 💪")

    st.divider()
