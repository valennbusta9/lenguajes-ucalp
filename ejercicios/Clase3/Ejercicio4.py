contador = 0

def incrementar():
    global contador
    contador += 1
    return contador
print(incrementar(), incrementar(),incrementar())

#No funciona sin global porque no tendria sentido llamar una a una funcion incrementar, 
# donde cada vez que se llama se inicializa la variable contador en 0, 
# por lo tanto en cada llamada devolveria 1, 
# en cambio si la declaramos con una variable global va a contar de manera correcta
