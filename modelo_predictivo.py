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