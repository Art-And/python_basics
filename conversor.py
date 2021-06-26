menu = """
Bienvenido al conversor de monedas 😀

1 - Pesos Mexicanos
2 - Pesos argentinos
3 - Pesos Colombianos

Elige una opción: """

opcion = input(menu)

if opcion == '1':
    pesos = input('Pesos Mexicanos: ')
    pesos =  float(pesos)
    valor_dolar = 20
    dolar = pesos / valor_dolar
    dolar = round(dolar, 2)
    dolar = str(dolar)
    print('Tienes $' + dolar + ' dolares')
elif opcion == '2':
    pesos = input('Pesos Argentinos: ')
    pesos =  float(pesos)
    valor_dolar = 95
    dolar = pesos / valor_dolar
    dolar = round(dolar, 2)
    dolar = str(dolar)
    print('Tienes $' + dolar + ' dolares')
elif opcion == '3':
    pesos = input('Pesos Colombianos: ')
    pesos =  float(pesos)
    valor_dolar = 3746
    dolar = pesos / valor_dolar
    dolar = round(dolar, 2)
    dolar = str(dolar)
    print('Tienes $' + dolar + ' dolares')
else:
    print('Elige una opcion correcta')