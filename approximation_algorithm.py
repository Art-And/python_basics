def main():
    objective = int(input("Choose a number: "))
    epsilon = 0.01
    step =  epsilon**2
    result = 0.0

    while abs(result**2 - objective) >= epsilon and result <= objective:
        result += step

    if abs(result**2 - objective) >= epsilon:
        print(f'Square root doesnt find')
    else:
        print(f'{objective} aprox square root is {result}')


if __name__ == '__main__':
    main()