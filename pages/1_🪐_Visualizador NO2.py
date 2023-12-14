import streamlit as st
import pandas as pd
import altair as alt

# Carga del archivo CSV
@st.cache_data
def load_data():
    df = pd.read_csv('clean_visuals/hist_est.csv', parse_dates=['Fecha'])
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

# Filtro por rango de años
year_range = st.sidebar.slider("Seleccionar rango de años", min_value=int(df['Fecha'].dt.year.min()), 
                               max_value=int(df['Fecha'].dt.year.max()), value=(int(df['Fecha'].dt.year.min()), 
                               int(df['Fecha'].dt.year.max())))

# Filtro por rango de meses
month_range = st.sidebar.slider("Seleccionar rango de meses", min_value=int(df['Fecha'].dt.month.min()), 
                                max_value=int(df['Fecha'].dt.month.max()), value=(int(df['Fecha'].dt.month.min()), 
                                int(df['Fecha'].dt.month.max())))

if not selected_stations:
    st.error("Selecciona al menos una estación.")
else:
    # Filtrar datos por estaciones seleccionadas, rango de años y rango de meses
    filtered_data = df[df['Estacion'].isin(selected_stations) & 
                       df['Fecha'].dt.year.between(year_range[0], year_range[1]) & 
                       df['Fecha'].dt.month.between(month_range[0], month_range[1])]

    # Mostrar los datos filtrados (excluyendo las columnas Longitud, Latitud, y Fecha)
    columns_to_show = ['Codigo', 'Año', 'Mes', 'NO2', 'Estacion']
    st.write("### Datos de las estaciones seleccionadas")
    st.write(filtered_data[columns_to_show])

    # Gráfico de evolución temporal con la columna 'Fecha' y estaciones filtradas
    st.write("### Evolución temporal del NO2")
    chart = alt.Chart(filtered_data).mark_line().encode(
        x=alt.X('Fecha:T', axis=alt.Axis(title='Fecha')),
        y=alt.Y('NO2:Q', axis=alt.Axis(title='NO2 (µg/m3)')),
        color='Estacion:N'
    ).properties(width=800, height=400)
    st.altair_chart(chart, use_container_width=True)

    # Mapa de estaciones con las estaciones seleccionadas
    st.write("### Mapa de estaciones seleccionadas")
    # Renombrar las columnas de latitud y longitud
    filtered_data = filtered_data.rename(columns={'Latitud': 'lat', 'Longitud': 'lon'})
    st.map(filtered_data, use_container_width=True)