precios_usd = [3.5,12,100,4.99,7.25,10.0]

conversion = list((map(lambda x: x * 1450, precios_usd)))

print(sum(conversion))