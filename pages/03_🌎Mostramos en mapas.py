import folium
import streamlit as st
import pandas as pd
from streamlit_folium import st_folium

st.set_page_config(
    page_title="Áreas Protegidas: Mapas.",
    page_icon="🐍",
    layout="wide"
)

def generar_mapa():
    attr = (
        '&copy; <a href="https://openstreetmap.org">OpenStreetMap</a> '
        'contributors, &copy; <a href="https://cartodb.com">CartoDB</a>'
    )
    tiles = 'https://wms.ign.gob.ar/geoserver/gwc/service/tms/1.0.0/capabaseargenmap@EPSG%3A3857@png/{z}/{x}/{-y}.png'
    m = folium.Map(
        location=(-33.457606, -65.346857),
        control_scale=True,
        zoom_start=5,
        name='es',
        tiles=tiles,
        attr=attr
    )
    return m

protegida = pd.read_csv("area_protegida.csv")

st.title("Mapa de áreas protegidas de Argentina")
st.header("Este es un mapa interactivo de las áreas protegidas de Argentina.")
st.write(
    "En este mapa se pueden visualizar las ubicaciones de las áreas protegidas de Argentina. "
    "En el apartado de filtros se puede seleccionar una categoría específica para visualizar sus ubicaciones."
)

protegida = protegida.dropna(subset=["lat", "lng"]).copy()

categorias = sorted(protegida["gna"].dropna().unique())

opciones = ["Todas las categorías"] + categorias

categoria_seleccionada = st.selectbox(
    "Toca aqui para seleccionar una zona protegida para ubicar en el mapa:",
    opciones
)

if categoria_seleccionada == "Todas las categorías":
    areas_mostrar = protegida
else:
    areas_mostrar = protegida[protegida["gna"] == categoria_seleccionada]

mapa_reservas = generar_mapa()

for _, row in areas_mostrar.iterrows():
    folium.Marker(
        location=[row["lat"], row["lng"]],
        popup=f"Nombre: {row['nam']}<br>Ubicación: {row['fna']}<br>Área: {row['area']}",
        tooltip=row["nam"],
        icon=folium.Icon(
            color="green",
            icon="tree",
            prefix="fa"
        )
    ).add_to(mapa_reservas)

st.write("Estas son las áreas protegidas que coinciden con el filtro seleccionado:", len(areas_mostrar))

st_folium(
    mapa_reservas,
    width=900,
    height=600,
    key="mapa_areas_protegidas"
)

st.write("Frecuencia de áreas encontradas por categoría:")
st.write(protegida["gna"].value_counts())
