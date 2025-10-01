
def calcularPromedio(lista):
    return sum(lista) / len(lista)

def calcularMaximo(lista):
    return max(lista)
contador = 0
def incrementar():
    global contador
    contador += 1
    return contador
print(incrementar(), incrementar())