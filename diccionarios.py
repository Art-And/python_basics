def main():
    my_dictionary = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    }

    # print(my_dictionary['llave1'])

    countries = {
        'Argentina': 44_938_954,
        'Brasil': 210_147_125,
        'Colombia': 50_372_424,
    }

    # for country in countries.keys():
    #     print(country)

    # for country in countries.values():
    #     print(country)

    for country, people in countries.items():
        print(country + " has " + str(people) + ' people')

if __name__ == '__main__':
    main()