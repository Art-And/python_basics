import random


def generator_pass():
    mayus = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    minus = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    simbol = ['!', '#', '$', '&', '/', '(', ')']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    characters = mayus +minus + simbol + numbers

    password = []

    for i in range(15):
        random_character = random.choice(characters)
        password.append(random_character)

    password = "".join(password)
    return password

def main():
    password = generator_pass()
    print("Your new password is: " + password)


if __name__ == '__main__':
    main()