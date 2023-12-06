#streamlit run main.py

import streamlit as st
import pandas as pd
import pylab as plt
import folium
import h3

from PIL import Image
from streamlit_folium import folium_static
from branca.colormap import LinearColormap

st.title('AQ-MAD Project')

#muestra imagen

file_path = "../img/wip.gif"
with open(file_path, "rb") as f:
    gif_bytes = f.read()

# Mostrar el GIF en Streamlit
st.image(gif_bytes, caption='GIF local', use_column_width=True)


#Mapa estaciones

prueba_map = pd.read_csv('../clean_visuals/hextaciones.csv')

from branca.colormap import LinearColormap
import folium
import h3
import pandas as pd
import streamlit as st
from streamlit_folium import folium_static

#Folium

nivel_resolucion = 7  # Puedes ajustar este valor según la resolución deseada

def calcular_influencia(distancia):
    influencia = 1 / (distancia + 1)  # Fórmula de influencia (ajustable)
    return influencia

# Lectura de datos simulada (reemplaza esto con tu lectura real desde el archivo CSV)
data = {
    'Latitud': [40.4168, 40.41, 40.42],
    'Longitud': [-3.7038, -3.71, -3.72],
    'Avg': [10, 20, 30],
    'Estacion': ['Estacion 1', 'Estacion 2', 'Estacion 3']
}
prueba_map = pd.DataFrame(data)

# Crear un mapa de Folium en Streamlit
st.title("Mapa de Estaciones y Zona de Influencia")
mapa = folium.Map(location=[prueba_map['Latitud'].mean(), prueba_map['Longitud'].mean()], zoom_start=12)

# Encontrar el rango de valores de Avg para establecer la escala de colores
max_avg = prueba_map['Avg'].max()
min_avg = prueba_map['Avg'].min()

# Crear un colormap lineal entre rojo y verde basado en los valores de Avg, pero invertido
colormap = LinearColormap(colors=['green', 'yellow', 'red'], vmin=min_avg, vmax=max_avg).to_step(10)

# Resto del código para generar hexágonos y marcadores...
for index, row in prueba_map.iterrows():
    latitud = row['Latitud']
    longitud = row['Longitud']
    valor_so2 = row['Avg']
    estacion = row['Estacion']
    
    hexagono_central = h3.geo_to_h3(latitud, longitud, nivel_resolucion)
    nivel_distancia = 10
    hexagonos_vecinos = h3.k_ring(hexagono_central, nivel_distancia)
    
    influencia_total = 0
    for hexagono_vecino in hexagonos_vecinos:
        distancia_central_vecino = h3.h3_distance(hexagono_central, hexagono_vecino)
        influencia = calcular_influencia(distancia_central_vecino)
        influencia_total += influencia * valor_so2
    
    influencia_promedio = influencia_total / len(hexagonos_vecinos)
    
    folium.GeoJson(
        {
            'type': 'Feature',
            'geometry': {
                'type': 'Polygon',
                'coordinates': [h3.h3_to_geo_boundary(hexagono_central, geo_json=True)]
            },
            'properties': {'tooltip': f"Avg SO2: {valor_so2}", 'style': {'fillColor': colormap(valor_so2), 'fillOpacity': 0.6}}
        },
        tooltip=f"Avg SO2: {valor_so2}"
    ).add_to(mapa)
    
    folium.Marker(
        location=[latitud, longitud],
        popup=f'Estación: {estacion}',
        icon=folium.Icon(color='blue', icon='info-sign')
    ).add_to(mapa)

# Mostrar el mapa de Folium en Streamlit
folium_static(mapa)



#Foursquare Studio

st.title("Visualización desde Foursquare Studio")

url_foursquare = "https://studio.foursquare.com/public/8729d261-aaf7-4cf6-ad1d-919a41da54d1"

st.components.v1.iframe(url_foursquare, width=800, height=600)
