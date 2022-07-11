import matplotlib.pyplot as plt
import random
import pandas as pd

ps = pd.read_csv("boyacaCO.csv")
ps2 = ps
ps3 = ps
ps4 = ps
ps5 = ps
ps6 = ps
ps7 = ps
ps8 = ps

print("-----------------------ALL-------------------------")
print(ps)
print("-----------------------HEAD------------------------")
print(ps2.head())
print("----------Percentiles-Datos estadisticos-----------")
print(ps3.describe().head())
print("-----------------Limpieza datos--------------------")
print(ps4.dropna())
print("--------------Remplazar NaN con Cero---------------")
print(ps5.fillna(0))
print("--------------Remplazar x Column con x value-------")
print(ps6.fillna({"Fecha final":1,"Estacion":2}))
print("----------Filtrado por columna o columnas----------")
print(ps7["Estacion"])
print("----------Filtrado por fila o filas----------------")
print(ps7.iloc[0:1])
print("----------Filtrado por fila y columna--------------")
print(ps7.loc[[ 3 , 4 ] , ["Estacion"]])
print("----------Filtrado por condicion Numerica----------")
print(ps7[ps7["CO"]>900])
print("----------Filtrado por condicion String------------")
print(ps7[ps7["Estacion"].str.contains("SOGAMOSO")])
print("-------------Transformacion de datos---------------")

def sumCO(cO):
	gain = cO * random.randint(2,3) 
	return gain
ps7["gain"]=ps7["CO"].apply(sumCO)
print(ps7)
print("-----------Transformacion por fila-----------------")

def porFila(fila):
	res = fila["CO"]+5
	return res

ps7["test"]=ps7.apply(porFila,axis=1)
print(ps7)
 
print("-----------------Agrupar datos por promedio--------------------")
print(ps8.groupby("Estacion").mean())

print("---------------Agrupar datos por x func de agregacion----------")
print(ps8.groupby("Estacion").agg({"CO":'sum'}))

print("------------------Imprimir datos graficas----------------------")
group = ps8.groupby("Estacion").mean()
group = group.fillna(0)
group["CO"].plot( kind = "bar" )
plt.savefig('graph.png')
print("El grafico se ha guardado correctamente")

print("-------------------Guardar archivos CSV------------------------")
group.to_csv("output.csv")
print("El archivo se ha guardado correctamente")
