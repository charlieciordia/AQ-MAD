import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from streamlit_folium import folium_static
import folium

st.markdown("# Conclusiones")

st.write("💀 La siguiente gráfica muestra la predicción para este 2023 de media anual de concentración de NO2 para cada estación:")

# Tabla predicts 2023
df_predicts23 = pd.read_csv('../clean_visuals/df_predicts23.csv', index_col=0)

# Paleta de color
palette = sns.color_palette("pastel", len(df_predicts23.columns))

# Transponer el DataFrame para tener las columnas como filas y viceversa
df_transpuesto = df_predicts23.T

# Crear el gráfico de barras verticales con la paleta de colores suaves
plt.figure(figsize=(40, 10))  # Tamaño del gráfico (mayor)
ax = df_transpuesto.plot(kind='bar', color=palette)
plt.title('NO2 Media anual 2023 por estación Ayto de Madrid')  # Título del gráfico
plt.xlabel('Estaciones')  # Etiqueta del eje X
plt.ylabel('Valor de NO2 (µg/m³)')  # Etiqueta del eje Y
plt.xticks(range(len(df_transpuesto.index)), df_transpuesto.index, rotation=45, ha='right')  # Alinear y rotar etiquetas del eje X

# Dibujar líneas horizontales con sus textos anotados
ax.axhline(y=20, color='red', linestyle='--')  # Línea horizontal en el valor 20
ax.text(len(df_transpuesto) - 0.5, 22, 'Valor límite anual (propuesta Directiva): 20 (µg/m³)', ha='right', va='bottom')
ax.axhline(y=10, color='green', linestyle='--')  # Línea horizontal en el valor 10
ax.text(len(df_transpuesto) - 0.5, 12, 'Valor guía anual (OMS 2021): 10 (µg/m³)', ha='right', va='bottom')

plt.tight_layout()  # Ajustar el diseño
plt.legend().remove()  # Eliminar la leyenda

# Mostrar el gráfico en Streamlit
st.pyplot(plt)

# Cargar los datos de las coordenadas
df_coords = pd.read_csv('../clean_visuals/hextaciones.csv')

# Crear un mapa con streamlit-leaflet
st.markdown("## Mapa de Estaciones")

st.write("""
💀 El siguiente mapa muestra la situación de cada estación, 
<span style='color: green;'>verde</span> por debajo de los valores propuestos a alcanzar, 
<span style='color: orange;'>naranja</span> en aquellas zonas donde el nivel de emisiones está regulinchi y 
<span style='color: red;'>rojo</span> las que superan ampliamente los objetivos planteados:
""", unsafe_allow_html=True)


# Crear un mapa centrado en las coordenadas promedio
mapa = folium.Map(location=[df_coords['Latitud'].mean(), df_coords['Longitud'].mean()], zoom_start=12)

# Definir los colores de los marcadores según el código de Estacion
color_dict = {
    24: 'green',
    58: 'green',
    49: 'orange',
    59: 'orange',
    60: 'orange'
}

# Función para asignar colores a los marcadores según el código de Estacion
def asignar_color(row):
    if row['Estacion'] in color_dict:
        return color_dict[row['Estacion']]
    else:
        return 'red'

# Añadir marcadores al mapa
for index, row in df_coords.iterrows():
    color = asignar_color(row)
    folium.Marker(
        location=[row['Latitud'], row['Longitud']],
        popup=row['Estacion'],
        icon=folium.Icon(color=color)
    ).add_to(mapa)

# Mostrar el mapa en Streamlit
folium_static(mapa)
