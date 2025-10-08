#Crear una función con una variable local llamada x, y fuera de ella definir también x.
#Mostrar cómo Python resuelve qué valor usar.

x = 12

def crear_sumador(incr):
    x = 0
    def sumar():
        nonlocal x
        x += incr
        return x
    return sumar
s = crear_sumador(3)
print(s(), s(), s())

#me devuelve 3 6 9 el valor de fuera de la funcion no lo mira, ya que x esta declarado como una variable local