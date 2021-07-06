def factorial(n):
    """
    Calcula el factorial de n.

    n int > 0
    returns n!
    """
    print(n)
    if n == 1:
        return 1

    return n * factorial(n-1)


def main():
    n = int(input('Selecciona un numero para obtener su factorial: '))
    print(factorial(n))


if __name__ == '__main__':
    main()