# Ejercicios (Tuplas)
# Guardar coordenadas (x, y) en una tupla e imprimir la distancia al origen.
# Dada una lista de tuplas (nombre, edad), imprimir solo los mayores de 18.

import math

x = int(input("Ingresá la coordenada 'X': "))
y = int(input("\nIngresá la coordenada 'Y': "))
coordenadas = (x, y)


def potencia(base, exp=2):
    return base**exp


def origen(x, y):
    suma = potencia(x) + potencia(y)
    raiz = math.sqrt(suma)
    return raiz


print(f"\nLa distancia al origen de las coordenadas X = {x} e Y = {y} es: {origen(x,y)} ")

print ("\n-------------------------------")


personas = [('juan',25), ('pedro',8),('juana',18),('luis', 49)]

for p in personas:
    if p[1] > 18:
        print(p)
