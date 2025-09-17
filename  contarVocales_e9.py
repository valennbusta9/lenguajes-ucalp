

def contarVocales(cadena):

    vocales = {"a": 0, "e": 0, "i": 0, "o":0, "u":0} #inicializo en 0 cada vocal

    for i in cadena:
        if i[0] in vocales:
            vocales[i] =+ 1
    return vocales


cadena=input("Ingresa una cadena ")
print (contarVocales(cadena))

