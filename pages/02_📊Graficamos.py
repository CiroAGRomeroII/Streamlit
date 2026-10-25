import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Áreas Protegidas: Gráficos.",
    page_icon="🐍",
    layout="wide"
)

protegida = pd.read_csv("area_protegida.csv")

protegida["tap"] = protegida["tap"].replace({
    0: "Reserva Natural",
    1: "Reserva Protegida",
    2: "Parque Nacional"
})

st.title("Gráficos de áreas protegidas")

areas_grandes = protegida[protegida["area"] > 500000]
top_grandes = areas_grandes.sort_values(by="area", ascending=False).head(10)

fig = px.bar(
    top_grandes,
    x="nam",
    y="area",
    title="Estas son las 10 áreas con mayor superficie registrada",
    labels={"nam": "Nombre del Área", "area": "Superficie (m²)"},
    color="area"
)

organismos = protegida["sag"].value_counts()

fig2 = px.bar(
    x=organismos.index,
    y=organismos.values,
    title="Estas son las cantidades de los registros según el Organismo Administrador (sag)",
    labels={"x": "Organismo", "y": "Cantidad de registros"},
    color=organismos.index
)

tipos_reserva = protegida["tap"].value_counts()

fig3 = px.pie(
    values=tipos_reserva.values,
    names=tipos_reserva.index,
    title="Grafico de torta de los tipos de reservas que hay según la columna 'tap' del dataset"
)

st.plotly_chart(fig, use_container_width=True)
st.caption("En este gráfico de barras se muestran las 10 áreas protegidas con mayor extensión en metros cuadrados dentro del dataset.")

st.plotly_chart(fig2, use_container_width=True)
st.caption("En este gráfico se puede comparar cuántos registros fueron aportados o son gestionados por cada organismo institucional.")

st.plotly_chart(fig3, use_container_width=True)
st.caption("Por ultimo en este gráfico de torta se puede observar las proporciones de los tipos de reservas mapeados a partir de la columna 'tap'.")
