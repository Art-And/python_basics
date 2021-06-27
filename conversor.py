menu = """
Bienvenido al conversor de monedas 😀

1 - Pesos Mexicanos
2 - Pesos argentinos
3 - Pesos Colombianos

Elige una opción: """

opcion = input(menu)

def conversor(string_tipo_pesos, valor_dolar):
    pesos = input('Convertir pesos ' + string_tipo_pesos + ': ')
    pesos =  float(pesos)
    dolar = pesos / valor_dolar
    dolar = round(dolar, 2)
    dolar = str(dolar)
    print('Tienes $' + dolar + ' dolares')

if opcion == '1':
    conversor('mexicanos', 20)
elif opcion == '2':
    conversor('argentinos', 95)
elif opcion == '3':
    conversor('colombianos', 3795)
else:
    print('Elige una opcion correcta')