import utilidades
import importlib

lista = [12,45,60,70,30,12]

print(utilidades.calcularPromedio(lista))

importlib.reload(utilidades)

print(utilidades.calcularMaximo(lista))