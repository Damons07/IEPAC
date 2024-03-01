import streamlit as st
import pandas as pd
import random

archivo_excel = "datos/ALEAOTIRO.xlsx"
df = pd.read_excel(archivo_excel)

# Seleccionar las columnas específicas para el segundo DataFrame
columnas_seleccionadas = ['ID', 'MUNICIPIO', '% DE VOTACIÓN MORENA', 'BLOQUE']
df_segundo = df[columnas_seleccionadas]

# Mostrar el segundo DataFrame
st.write(df_segundo)

# Agregar widgets para ingresar valores
muestra = st.number_input("MUESTRA", value=50, min_value=1)
cantidad_municipios = st.number_input("CANTIDAD DE MUNICIPIOS", value=100, min_value=1, max_value=len(df_segundo))

# Generar una lista de municipios aleatorios
municipios_aleatorios = random.sample(range(len(df_segundo)), muestra)

# Crear un nuevo DataFrame con los municipios seleccionados aleatoriamente
df_aleatorio = pd.DataFrame(columns=["Posición", "Número", "Municipio"])

for i, idx in enumerate(municipios_aleatorios):
    municipio = df_segundo.iloc[idx]['MUNICIPIO']
    df_aleatorio.loc[i] = [i+1, idx+1, municipio]

# Mostrar la tabla con los municipios seleccionados aleatoriamente
st.write("Municipios seleccionados aleatoriamente:")
st.write(df_aleatorio)
