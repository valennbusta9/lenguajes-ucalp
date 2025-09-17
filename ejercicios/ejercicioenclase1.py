#🔧 Ejercicios (Strings)
#Pedir una palabra y mostrarla en mayúsculas, minúsculas y title case.
#Pedir una frase y contar cuántas veces aparece cada vocal.
#Dada una frase, mostrar las 3 primeras y las 3 últimas letras usando slicing.
#Verificar si una palabra contiene la letra 'r'. (Tip: in)

palabra = input('Ingrese una palabra \n')
                
print(palabra.upper())
print(palabra.lower())
print(palabra.title())

frase = input('Ingrese una frase \n')

vocales = 'aeiou'

print (frase.count(vocales))

palabra = input('Ingrese una palabra \n')

for vocal in vocales:
    print(vocal +':'+ str(palabra.count(vocal)))

