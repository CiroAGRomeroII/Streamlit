import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Áreas Protegidas: Datos.",
    page_icon="🐍",
    layout="wide"
)

protegida = pd.read_csv("area_protegida.csv")

protegida["tap"] = protegida["tap"].replace({
    0: "Reserva Natural",
    1: "Reserva Protegida",
    2: "Parque Nacional"
})

st.title("Tarea de exposición de los datos de los registros de áreas protegidas.")
st.header("Información del contenido del dataset.")
st.write(
    "Este dataset reúne información de las áreas protegidas que se encuentran en Argentina y permiten conocer mejor nuestros datos sobre la vida silvestre en nuestras zonas naturales, "
    "las categorías encontradas que dan una mejor descripción enumerada de cada zona, los organismos que las administran y su superficie registrada actualmente o en años anteriores."
)
st.write(
    "¿Qué es un dataset? Es un archivo que almacena muchos datos organizados en filas "
    "y columnas. Como contiene tanta información, sería complicado buscar cada dato uno "
    "por uno. Por eso, con esta pequeña web podemos filtrar la información y encontrar los datos "
    "que necesitamos de forma más rápida y sencilla, también podemos hacer gráficos y mapas para visualizar mejor la información recopilada."
    "por eso, acontinuación en esta sección vamos a conocer mejor nuestros datos y sus características."
)

with st.expander("¿Cuántas filas y columnas tiene este archivo?"):
    filas, columnas = protegida.shape
    st.write(f"Este archivo tiene {filas} filas y {columnas} columnas.")

with st.expander("¿Cuáles son la superficie mínima y máxima registradas?"):
    st.write("Área más pequeña (m²):", protegida["area"].min())
    st.write("Área más grande (m²):", protegida["area"].max())

with st.expander("¿Cuántas categorías diferentes (gna) hay?"):
    cant = protegida["gna"].nunique()
    st.write(f"En total hay unas {cant} categorías diferentes en la columna 'gna'.")

with st.expander("¿Cuáles son los nombres de las columnas en este archivo?"):
    columnas2 = protegida.columns
    st.write("Los nombres de las columnas que tenemos son en este archivo son:")
    st.write(columnas2)

with st.expander("¿Cuáles son los valores nulos en este dataset?"):
    valores_nulos = protegida.isnull().sum()
    st.write("Estos son los valores nulos o datos faltantes en cada columna:")
    st.write(valores_nulos)

with st.expander("¿Cuáles son los organismos (sag) con más registros cargados?"):
    organismos = protegida["sag"].value_counts()
    st.write("Estos son los organismos con más registros cargados en el dataset y sus cantidades:")
    st.write(organismos)
