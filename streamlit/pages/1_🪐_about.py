
import streamlit as st
import pandas as pd
import altair as alt

# Carga del archivo CSV
@st.cache_data
def load_data():
    df = pd.read_csv('../clean_visuals/hist_est.csv')
    return df

# Configuración de la página
st.set_page_config(page_title="NO2 Data", page_icon="📊")

# Título y descripción
st.markdown("# Análisis de NO2")
st.sidebar.header("Filtros")

# Carga de datos
df = load_data()

# Multiselect para elegir estaciones
selected_stations = st.sidebar.multiselect("Seleccionar estaciones", df['Estacion'].unique())

if not selected_stations:
    st.error("Por favor selecciona al menos una estación.")
else:
    # Filtrar datos según las estaciones seleccionadas
    filtered_data = df[df['Estacion'].isin(selected_stations)]

    # Gráfico de evolución temporal
    st.write("### Evolución temporal del NO2")
    chart = alt.Chart(filtered_data).mark_line().encode(
        x='Año:O',
        y='NO2:Q',
        color='Estacion:N'
    ).properties(width=600, height=400)
    st.altair_chart(chart, use_container_width=True)

    # Información basada en la latitud y longitud
    st.write("### Información de ubicación")
    st.write(filtered_data[['Estacion', 'Longitud', 'Latitud']].drop_duplicates())
