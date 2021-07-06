def approximation_algorithm(number):
    objective = number
    epsilon = 0.01
    step =  epsilon**2
    result = 0.0

    while abs(result**2 - objective) >= epsilon and result <= objective:
        result += step

    if abs(result**2 - objective) >= epsilon:
        print(f'Square root doesnt find')
    else:
        print(f'{objective} aprox square root is {result}')


def binary_search(number):
    objective = number
    epsilon = 0.01
    down = 0.0
    up = max(1.0, objective)
    result = (up + down) / 2

    while abs(result**2 - objective) >= epsilon:
        if result**2 < objective:
            down = result
        else:
            up = result

        result = (up + down) / 2

    print(f'{objective} square root is {result}')


def enumeration(number):
    objective = number
    response = 0

    while response**2 < objective:
        #print(response)
        response += 1

    if response**2 == objective:
        print(f'{objective} square root is {response}')
    else:
        print(f'{objective} doesnt have square root')


def main():
    number = int(input('Please choose a number that you need to square root: '))
    option_selected =  int(input("""
    Select a option that you want, please:
    1- binary
    2- approximation
    3- enumeration

    option: """
    ))

    if option_selected == 1:
        binary_search(number)
    elif option_selected == 2:
        approximation_algorithm(number)
    elif option_selected == 3:
        enumeration(number)
    else:
        print("Please choose a correct option")


if __name__ == '__main__':
    main()