import pandas as pd
import os 

# Leer el archivo Excel
df = pd.read_excel("./data/RPT_RG_04_EstudiantesInstitucion.xlsx")

def eliminar_columna(df):
    return df.drop(columns=['ORACUN'], axis=1)

#renombrar columnas
def renombrar_columnas(df):
    return df.rename(columns={'ID_STUDENT':'ID_ESTUDIANTE',
                              'NAME_STUDENT':'NOMBRE_ESTUDIANTE',
                              'INST_PROCE': 'INSTITUCION_PROCEDENCIA',
                              'INST_NAME':'CLASE_INSTITUCION', 
                              'INST_NIVEL':'NIVEL_INSTITUCION',
                              'INST_MODALIDAD':'MODALIDAD_INSTITUCION'})

de = eliminar_columna(df)
df = renombrar_columnas(de)

a = input("Ingrese el nombre del nuevo reporte(O el nommbre que desea): ")

ruta = 'DATA_NORMALIZADA/' + a + '.xlsx'
# Crear un nuevo DataFrame con solo la columna 'Nota'
df_nueva = pd.DataFrame(df)

# Guardar el nuevo DataFrame en un nuevo archivo de Excel
df_nueva.to_excel(ruta, index=False)

print("El archivo se guardo en la ruta: ", ruta)
