import streamlit as st

def app():

    st.title("Conclusiones")

    #Tabla predicts 2023
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
