import pandas as pd

def NO2_clean(df):
    
    '''
    Esta funcion limpia el formato de los df procedentes del la base de datos de Madrid con mediciones diarias,
    ordenando el dato y realizando la media mensual de NO2 de todas las estaciones.

    '''
    
    # Filtrar por la magnitud correspondiente (en este caso, MAGNITUD == 8)
    df = df[df["MAGNITUD"] == 8]

    # Eliminar columnas que contienen 'V'
    df = df.drop(columns=[e for e in df.columns if 'V' in e])

    # Eliminar columnas innecesarias
    df.drop(['MUNICIPIO', 'MAGNITUD', 'PUNTO_MUESTREO'], axis=1, inplace=True)

    # Convertir a formato largo (melt)
    df = pd.melt(df, id_vars=['ESTACION', 'ANO', 'MES'], var_name='DIA', value_name='NO2')

    # Convertir la columna 'DIA' a tipo int
    df['DIA'] = df['DIA'].str[1:].astype(int)

    # Calcular el promedio mensual por estación, año y mes
    df = df.groupby(['ESTACION', 'ANO', 'MES'])['NO2'].agg(lambda x: x.mean())
    df = df.reset_index()

    return df


def estacion_timeseries(df):
    
    '''
    Esta funcion prepara los df de cada estación para introducirlos en un modelo SARIMA.

    '''
 
    df.drop('ESTACION', axis=1, inplace=True)
    
    df['month'] = df['ANO'].astype(str) + '-' + df['MES'].astype(str).str.zfill(2)
    
    df.drop(['ANO', 'MES'], axis=1, inplace=True)
    
    df.index = pd.to_datetime(df["month"])
    
    df.index.freq = pd.infer_freq(df.index)
    
    df.drop("month",  inplace = True, axis = 1)
    
    return df

    