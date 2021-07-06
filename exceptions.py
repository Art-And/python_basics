def divide_elementos_de_lista(lista, divisor):
    try:
      return [i / divisor for i in lista]
    except ZeroDivisionError as e:
        print(e)
        return lista

def main():
    lista = list(range(100))
    divisor = 0

    print(divide_elementos_de_lista(lista, divisor))


if __name__ == '__main__':
    main()