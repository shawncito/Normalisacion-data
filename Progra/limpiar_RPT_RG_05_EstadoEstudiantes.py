import pandas as pd 

# Leer el archivo Excel

df = pd.read_excel("./data/RPT_RG_05_EstadoEstudiantes.xlsx")

def eliminar_columna(df):
    return df.drop(columns=['TRASH1', 'TRASH2'], axis=1)

def renombrar_columna(df):
    return df.rename(columns={'ID_STUDENT':'ID_ESTUDIANTE',
                              'NAME_STUDENT':'NOMBRE_ESTUDIANTE',
                              'PHONE1':'NUMERO_TELEFONO_1',
                              'PHONE2':'NUMERO_TELEFONO_2',
                              'GENERO':'GENERO',
                              'CIUDAD':'CIUDAD',
                              'DATE_NAC':'FECHA_NACIMIENTO',
                              'DATE_ING':'FECHA_INGRESO',
                              'E-MAIL':'CORREO_ELECTRONICO',
                              })

de = eliminar_columna(df)
df = renombrar_columna(de)

a = input("Ingrese el nombre del nuevo reporte(O el nommbre que desea): ")

ruta = 'DATA_NORMALIZADA/' + a + '.xlsx'
# Crear un nuevo DataFrame
df_nueva = pd.DataFrame(df)

# Guardar el nuevo DataFrame en un nuevo archivo de Excel
df_nueva.to_excel(ruta, index=False)

print("El archivo se guardo en la ruta: ", ruta)