# Ejercicios (Listas)
# Ingresar notas hasta -1, calcular el promedio y cuántos están por debajo.
# Dada una lista de palabras, construir otra con las que tengan más de 5 letras.
notas = []

nota = int(input("Ingresa una nota: "))
promedio = 0
totalNotas = 0

while nota != -1:
    notas.append(nota)
    promedio += nota
    totalNotas += 1
    nota = int(input("Ingresa una nota: "))

print(notas)
resultadoPromedio = promedio / totalNotas
print("Total promedio: ", resultadoPromedio)

debajo = 0
for n in notas:
    print(n)
    if n < resultadoPromedio:
        debajo += 1

print(f"Hay un total de {debajo} notas debajo del promedio")


print ("/n-------------------------------")


palabras = ["mates","botella","termo","llave","casa"]
palabras5 = []

for p in palabras:
    if len(p) > 5:
        palabras5.append(p)

print(f"La lista de palabras original es: {palabras}")
print(f"La lista de palabras con mas de 5 leras es: {palabras5} ")