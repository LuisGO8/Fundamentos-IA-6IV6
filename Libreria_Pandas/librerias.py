import pandas as pd


pd.__version__


df_profesores1=pd.DataFrame({

        "nombre":["Jaime","Alma","Armando","Sergio"],

        "apellido_paterno":["Minor","Vazquez","Alvarez","Moreno"],

         "apellido_materno":["Gomez","Sanchez","Galvan","Soto"]

        })


print(df_profesores1)

print(type(df_profesores1))


df_archivo_1=pd.read_csv("Sacramentorealestatetransactions.csv")

print(df_archivo_1)

# primeros 5 elementos
print("PRIMEROS 5 ELEMENTOS")
print(df_archivo_1.head())

# 20 elementos de la lista
print("20 ELEMENTOS DE LA LISTA")
print(df_archivo_1.head(20))

#Los últimos t elementos
print("ULTIMOS ELEMENTOS")
print(df_archivo_1.tail())


#Ver los tiposy de datos

print("TIPOS DE DATOS")
print(df_archivo_1.dtypes)

#estadísticas básicas

print(df_archivo_1.describe())


print(df_archivo_1.loc[100])


print (df_archivo_1["city"])


print(df_archivo_1["city"]=="SACRAMENTO")


city="SACRAMENTO"

print(df_archivo_1.query("city==@city"))


print(df_archivo_1.sort_values(by="city",ascending=True))