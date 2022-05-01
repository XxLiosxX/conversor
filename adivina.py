import random


def run():
    number_ramdon = random.randint(1, 100)
    number = int(input("Elige un número del 1 al 100: "))
    while number != number_ramdon:
        if number < number_ramdon:
            print("Busca un número más grande")
        else:
            print("Busca un número menor")
        number = int(input("Elige otro número: "))
        pass
    print("¡Ganaste!")


if __name__ == "__main__":
    run()