def es_palindromo ():
    frase = input('Ingrese una frase \n')
    i = 0
    j = len(frase) - 1 #me quedo con la ultima letra

    while (frase[i] == frase[j] and i < j ):
        print(frase[i])
        print(frase[j])
        i += 1
        j -= 1
    print(i,j)
    return i >= j
        
        
print (es_palindromo())