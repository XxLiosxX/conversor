def run():
    menu = """"
    Bienvenido a la tabla de multiplicar

    1.- Tabla del 1
    2.- Tabla del 2
    3.- Tabla del 3
    4.- Tabla del 4
    5.- Tabla del 5
    6.- Tabla del 6
    7.- Tabla del 7
    8.- Tabla del 8
    9.- Tabla del 9

    Elije una opción del (1 al 9): """
    opcion = int(input(menu))
    if opcion == 1:
        for tabla1 in range(11):
            print(1 * tabla1)
    elif opcion == 2:
        for tabla2 in range(11):
            print(2 * tabla2)
    elif opcion == 3:
        for tabla3 in range(11):
            print(3 * tabla3)
    elif opcion == 4:
        for tabla4 in range(11):
            print(4 * tabla4)
    elif opcion == 5:
        for tabla5 in range(11):
            print(5 * tabla5)
    elif opcion == 6:
        for tabla6 in range(11):
            print(6 * tabla6)
    elif opcion == 7:
        for tabla7 in range(11):
            print(7 * tabla7)
    elif opcion == 8:
        for tabla8 in range(11):
            print(8 * tabla8)
    elif opcion == 9:
        for tabla9 in range(11):
            print(9 * tabla9)
    else:
        print("             Esa no es una opción")


if __name__ == "__main__":
    run()



