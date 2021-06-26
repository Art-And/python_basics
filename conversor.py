pesos = input('Pesos Mexicanos: ')
pesos =  float(pesos)
valor_dolar = 20
dolar = pesos / valor_dolar
dolar = round(dolar, 2)
dolar = str(dolar)
print('Tienes $' + dolar + ' dolares')