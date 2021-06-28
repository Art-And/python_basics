import random


def main():
    number_random = random.randint(0, 100)
    number_selected = int(input("Choose a number between 0 and 100: "))

    while number_selected != number_random:
        if number_selected < number_random:
            print("Error, choose a higher number")
        else:
            if number_selected > 100:
                print("Please, write a lower number than 100")
            else:
                print("Error, choise a lower number")
        number_selected = int(input("Choose a new number: "))

    print('You win!')


if __name__ == '__main__':
    main()