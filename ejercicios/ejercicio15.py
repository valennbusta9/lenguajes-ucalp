# Ejercicios (Diccionarios)
# Leer nombres y notas hasta FIN y guardar en un diccionario. Luego mostrar:
# Promedio general, mejor estudiante, y los/as que están por debajo del promedio.
# Construir un diccionario {palabra: longitud} a partir de una frase.

diccionario = {} 
notasTot = 0
AlumnosTot = 0
Promedio = 0
max = -1

mejorAlumno = ""
nombre = input("Ingrese un nombre completo: ")

while nombre.upper() != "FIN":
    diccionario[nombre] = int(input("Ingrese su nota: "))
    notasTot += diccionario[nombre]
    AlumnosTot += 1
    if diccionario[nombre] > max:
        max = diccionario[nombre]
        mejorAlumno = nombre
    nombre = input("Ingrese un nombre completo: ")

Promedio = notasTot / AlumnosTot
print(f"\nEl promedio general de las notas es de: {Promedio}\n")
print(f"El mejor estudiante de la clase es: {mejorAlumno}\n")
print(diccionario)

debajoPromedio = []
for i in diccionario:
    if diccionario[i] < Promedio:
        debajoPromedio.append(i)

print(f"Los alumnos que están debajo del promedio son: {debajoPromedio}")
