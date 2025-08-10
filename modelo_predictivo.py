import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


print("Vas a construir tu primer modelo de preduccion con Python.")
print("Ingresarás horas estudiasdas y la nota obtenida. Escribe 'fin para terminar'.\n")

horas = []
notas = []

while  True:
    entrada_hora = input("Horas de estudio (o 'fin'): ")
    if entrada_hora.lower() == 'fin':
        break
    entrada_nota = input("Nota obtenida: ")
    try:
        horas.append(float(entrada_hora))
        notas.append(float(entrada_nota))
    except ValueError:
        print("Ingresa solo los números válidos")
        continue
    
if len(horas) < 2:
    print("Necesitas al menos dos registros para entrenar el modelo.")
    exit()
    
#Crear y mostrar tabla
df = pd.DataFrame({'Horas': horas, 'Notas': notas})
print("\n Datos cargados: ")
print(df)

# Guardar CSV
df.to_csv("datos_estudio.csv", index=False)
print("\n Archivo guardado como datos_estudio.csv")

# Entrenar modelo
X = df[['Horas']]
y = df[['Notas']]
modelo = LinearRegression()
modelo.fit(X. y)

