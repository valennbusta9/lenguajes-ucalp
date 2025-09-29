import string

def normalizar_palabras(frase):
    frase = frase.lower()  # paso a minúsculas
    frase_sin_puntuacion = ""  

    for c in frase:
        if c not in string.punctuation:  # si no es signo de puntuación
            frase_sin_puntuacion += c

    # divido la frase en palabras y retorno la lista
    return frase_sin_puntuacion.split()

frase = input('Ingrese una frase: \n')
print(normalizar_palabras(frase))

