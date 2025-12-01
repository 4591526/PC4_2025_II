# Importar librerías 
import pandas as pd
import openpyxl
import folium
import streamlit as st
from folium.map import Icon
from streamlit.components.v1 import html
import matplotlib.pyplot as plt

# Cargar la base de datos
df = pd.read_excel("autores.xlsx")

#st.write(df)

st.title(":red[Autores]")
st.title("Autores de :blue[libros]")

st.markdown("**Este es un texto en negrita** y *este en cursiva*.")
st.markdown("<h1 style='text-align: center; color: #0BF48F'>Título</h1>", unsafe_allow_html=True)


# Crear el mapa centrado en la media de coordenadas
m = folium.Map(location=[df["Latitud"].mean(), df["Longitud"].mean()],
                zoom_start=3)

  # Añadir marcadores con popup e imagen + enlace a YouTube
for i, row in df.iterrows():

    popup_html = f"""
    <div style="width:240px;">
        <h4><b>{row['Autor']}</b></h4>
        <p><b>Fecha:</b> {row['Fecha de nacimiento']}</p>
        <p><b>Nacionalidad:</b> {row['Nacionalidad']}</p>
        <p><b>Lugar:</b> {row['Lugar de nacimiento']}</p>

        <img src="{row['Imagen']}" width="150px"><br><br>

        <a href="{row['Entrevista']}" target="_blank">
            🎬 Ver entrevista en YouTube
        </a>
    </div>
    """

    popup = folium.Popup(popup_html, max_width=300)

    folium.Marker(
        location=[row["Latitud"], row["Longitud"]],
        popup=popup,
        icon=Icon(icon="home", color="green", icon_color="red")
    ).add_to(m)

# Mostrar mapa 
map_html = m._repr_html_()

# Mostrar en Streamlit
html(map_html, height=500)

st.image("tlou.jpg", caption= "Ellie en el auto con Joe")

# Crear tres columnas y poner la imagen en la columna central
col1, col2, col3 = st.columns(3)
with col2:
    st.image("tlou.jpg", caption="Ellie en el auto con Joe", width=280)


fig = plt.figure(figsize=(4,4))

x = ["A", "B", "C", "D"]
y = [3, 8, 1, 10]

plt.bar(x, y, color = ["red", "blue", "#079C5C", "#6283CB" ]) 
st.pyplot(fig) # instead of plt.show()