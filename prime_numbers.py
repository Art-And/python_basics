def its_prime(number):
    counter = 0

    for i in range(1, number + 1):
        if i == 1 or i == number:
            continue
        if number % i == 0:
            counter += 1

    if counter == 0:
        return True
    else:
        return False


def run():
    number = int(input("Write a number: "))

    if its_prime(number):
        print("It's prime number")
    else:
        print("It isn't prime number")

# def factorial(n):
#     fact = 1
#     if n < 0:
#         return 0
#     elif n == 0:
#         return 1
#     while (n > 1):
#         fact *= n
#         n -= 1
#     return fact


# def main():
#     numero = int(input("Escoge un numero: "))
#     wilson = factorial(numero - 1) + 1
#     #print(wilson)
#     if wilson % numero == 0:
#         print("El numero es primo")
#     else:
#         print("No es primo")


if __name__ == '__main__':
    run()