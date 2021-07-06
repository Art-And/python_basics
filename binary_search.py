def main():
    objective = int(input("Choose a number: "))
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

if __name__ == '__main__':
    main()