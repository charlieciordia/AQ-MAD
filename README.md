# AQ-MAD
Proyecto final IRONHACK Data Analytics

![homer](https://github.com/charlieciordia/AQ-MAD/blob/main/img/homer.gif)


## Objetivo 🚀

Este proyecto desarrolla un estudio acerca de la calidad del aire en la ciudad de Madrid. Para ello, se utilizan métodos y herramientas de recopilación, limpieza y análisis de datos. Este estudio se centra particularmente en las emisiones de NO2, dada su relevancia para la salud y su presencia en entornos urbanos. Se trata de un contaminante presente debido al tráfico vehicular y la actividad industrial, con gran impacto en el medio ambiente.

Se estudian zonas de afección, y del mismo modo patrones y tendencias a fin de comprender si las medidas aplicadas consiguen reducir el impacto negativo de este contaminante, y tratar de predecir su evolución en años venideros.

Los información ha sido obtenida en la plataforma de [datos abiertos del Ayuntamiento de Madrid](https://datos.madrid.es/portal/site/egob)


## Estructura de carpetas 📂

Este repositorio se divide según la siguiente estructura:

- **Carpeta clean_visuals:**

   - **predicts**: carpeta contenedora de los resultados de las series temporales por estaciones.
   - **df_predicts_23.csv**: archivo con las predicciones de 2023.
   - **H3_NO2_2023.csv**: dataset preparado para visualizar con H3.
   - **hist_est.csv**: histórico de todas las emisiones recogidas de NO2.
   
- **Carpeta data:**

   - **aemet**: carpeta contenedora de datos históricos del clima.
   - **AytoMad**: carpeta contenedora de datos recogidos por las estaciones.   
   - **df_XX.csv**: datos limpios a introducir en los modelos de machine learning.
   
- **Carpeta img:**

   - Carpeta para guardar gráficas, imágenes y memes.

- **Carpeta notebook:**

   - **TimeSeries_Forecasting**: esta carpeta tiene los modelos SARIMA por cada estación de captación de datos.
   - **AQ_Cleansing_Monthly_Rituals .ipynb**: Limpieza de datos de las estaciones.
   - **AQ_Map_Crafting_hub .ipynb**: este archivo crea las visualizaciones con geolocalización.
   - **AQ_Temporal_Insights_Lab.ipynb**: este archivo crea las visualizaciones temporales.  
   - **Predict_viewer .ipynb**: contiene las predicciones de emisiones de NO2 para el cierre del año 2023.
   - **Temperaturas .ipynb**: contiene datos de temperaturas en Madrid.    

- **Carpeta src:**

   - **clean_support .ipynb**: este archivo contiene funciones de apoyo para la limpieza de datos.
   
- **Carpeta streamlit:**

   - **main .py**: este archivo contiene la visualización en streamlit.  
   

## Tu forecaster de confianza🤓

**1. Exploración y limpieza de datos**

Empleo de técnicas habituales de limpieza, incluyendo la creación de funciones de apoyo.

[Visualización en FSQ con H3](https://studio.foursquare.com/public/8729d261-aaf7-4cf6-ad1d-919a41da54d1)

![FSQ](https://github.com/charlieciordia/AQ-MAD/blob/main/img/FSQ.png)

**2. Elección de modelo predictivo**

Se ha realizado el estudio de las estaciones con un modelo SARIMA.

Datos no estacionarios. Además, se aprecia una bajada en registros de NO2 durante la pandemia.

![Img 1](https://github.com/charlieciordia/AQ-MAD/blob/main/img/01.png)

Estacionaridad y estacionalidad. Se opta por establecer una estacionalidad anual.

![Img 2](https://github.com/charlieciordia/AQ-MAD/blob/main/img/02.png)

Se estudia la autocorrelación, es decir, en cuántos registros anteriores para predecir los siguientes.
 
![Img 3](https://github.com/charlieciordia/AQ-MAD/blob/main/img/03.png)

Entrenamiento SARIMA. En negro los datos reales, en rojo la predicción.

![Img 4](https://github.com/charlieciordia/AQ-MAD/blob/main/img/04.png)

Predicción.

![Img 5](https://github.com/charlieciordia/AQ-MAD/blob/main/img/05.png)

Comparativa con datos de 2023 reales desde enero a octubre (datos hasta la fecha obtenidos) y los resultados de la serie temporal.

![Img 6](https://github.com/charlieciordia/AQ-MAD/blob/main/img/06.png)


**3. Visualización de datos y conclusiones**

Se justifica seguir aplicando nuevas medidas de restricción para reducir las emisiones, puesto que las predicciones no son optimistas.
 
![Img 7](https://github.com/charlieciordia/AQ-MAD/blob/main/img/07.png)


## Próximos pasos 🦏

-Mejorar el modelo SARIMA con variables exógenas, particularmente datos climatológicos como la lluvia.

-Aplicar otros modelos predictivos como Prophet.


## Bibliotecas y recursos 📚
 
[Pandas](https://pandas.pydata.org/docs/)🐼

[Matplotlib](https://matplotlib.org/)📈

[Seaborn](https://seaborn.pydata.org/)📊

[h3](https://h3geo.org/)⛋

[Foursquare studio](https://studio.foursquare.com/)🗺️

[Streamlit](https://streamlit.io/)🔥

[Aquí](https://github.com/charlieciordia/AQ-MAD/raw/main/AQ_MAD.mp4) puedes descargar un vídeo de la presentación.