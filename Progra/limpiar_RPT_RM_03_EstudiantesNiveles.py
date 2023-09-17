import pandas as pd 
import os

# Leer el archivo Excel
df = pd.read_excel("./data/RPT_RM_03_EstudiantesNiveles.xlsx")

def eliminar_columna(df):
    return df.drop(columns=[ 'Textbox74', ], axis=1)#NO TENGO NI IDEA DE QUE HACE ESA COLUMNA

def renombrar_columna(df):
    return df.rename(columns ={'Textbox73':'Num',
                               'CLINAM2':'NOMBRE_ESTUDIANTE',
                               'GRPCUN2':'ID_ESTUDIANTE',
                               'Textbox75':'???',
                               'Textbox76':'CREDITOS_MATRICULADOS',
                               'ESCUELA2': 'ESCUELA',
                               'ENFASIS2' : 'ENFASIS',
                               'Textbox77':'CANTIDAD_CUATRIMESTRES',
                               'CLIPAI2'  : 'PAIS',
                               'Textbox78': 'RELIGION',
                               'Textbox79': 'TIPO_ESTUDIANTE',
                               'CARCOD2': 'GENERO',
                               'CARCOD3' :'EDAD',
                               'CLIEM2' : 'EMAIL',
                               'CLITCE2' : 'TELEFONO',})

de = eliminar_columna(df)
df = renombrar_columna(de)

a = input("Ingrese el nombre del nuevo reporte(O el nommbre que desea): ")

ruta = 'DATA_NORMALIZADA/' + a + '.xlsx'
# Crear un nuevo DataFrame
df_nueva = pd.DataFrame(df)

# Guardar el nuevo DataFrame en un nuevo archivo de Excel
df_nueva.to_excel(ruta, index=False)
print("El archivo se guardo en la ruta: ", ruta)
