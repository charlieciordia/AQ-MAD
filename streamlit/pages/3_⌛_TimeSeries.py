import streamlit as st

# Encabezado común
st.title("Modelo Predictivo SARIMA")
st.write("#### *Objetivo: evaluar la tendencia de emisiones de NO2 en Madrid*")
st.write("""
* Comprobar si las medidas planteadas resultan efectivas.
* Intentar predecir el comportamiento, y comprobar si la tendencia es acorde a los objetivos marcados.
""")

# Paso 1
st.header("Paso 1: Procesamiento y exploración de datos")
st.write("""
Se aplica la limpieza, transformación y preparación de los datos para el modelo. 
""")
st.write("""
* Evaluación de estacionaridad y estacionalidad.
* Test de Fuller
""")
# Carga de la imagen Estacionaridad
st.image("../img/11.png", caption="Estacionaridad", use_column_width=True)
# Estacionaridad vs Estacionalidad
st.image("../img/12.png", caption="Estacionaridad vs Estacionalidad", use_column_width=True)


# Paso 2
st.header("Paso 2: Parámetros del modelo, ajuste y métricas de rendimiento")
st.write("""
* Concepto autocorrelación.
* Elección parámetros p, d, q y s.
* Evaluación Error Medio Absoluto (MAE).
""")
# Carga de la imagen Autocorrelación
st.image("../img/13.png", caption="Autocorrelación", use_column_width=True)

# Paso 3
st.header("Paso 3: Evaluación y Ajuste")
st.write("""
Aquí se evalúa el rendimiento del modelo entrenado. Se realiza la validación final y se ajustan los parámetros si es necesario.
""")
# Carga de la imagen Ajuste modelo
st.image("../img/14.png", caption="Ajuste modelo", use_column_width=True)

# Paso 4
st.header("Resultados: Predicción y comparativa con datos reales de 2023")
st.write("""
Las siguientes gráficas muestran los resultados tras aplicar el modelo predictivo, y la comparativa entre los datos reales y los predichos para 2023:
""")

# Carga de la imagen correspondiente al Paso 3
st.image("../img/15.png", caption="Predicción", use_column_width=True)
# Carga de la imagen correspondiente al Paso 3
st.image("../img/16.png", caption="Datos reales vs predicciones", use_column_width=True)
