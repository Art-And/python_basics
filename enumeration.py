def main():
    objective = int(input('Please, choose a integer: '))
    response = 0

    while response**2 < objective:
        #print(response)
        response += 1

    if response**2 == objective:
        print(f'{objective} square root is {response}')
    else:
        print(f'{objective} doesnt have square root')

if __name__ == '__main__':
    main()