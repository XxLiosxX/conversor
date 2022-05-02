def run():
    menu = """
    Bienvenido al conversor de moneda 🐧

    1 - Pesos colombiano
    2 - Bolivares
    3 - Euros

    Elije una opcion (1, 2, 3): """

    #Este es el conversador de peso
    opcion = int(input(menu))
    if opcion == 1:
        pesos = input("Cuanto pesos tienes: ")
        pesos = float(pesos)
        valor_dolar = 0.00026
        dolares = pesos / valor_dolar
        dolares = round(dolares, 2)
        dolares = str(dolares)
        print("Tienes: " + dolares + "$")

    #Este es el conversor de bolivares
    elif opcion == 2:
        bolivar = input("Cuanto bolivares tienes: ")
        bolivar = float(bolivar)
        valor_dolar = 4.43
        dolares = bolivar / valor_dolar
        dolares = round(dolares, 2)
        dolares = str(dolares)
        print("Tienes: " + dolares + "$")
        
    #Este es el conversor
    elif opcion == 3:
        euro = input("Cuanto euro tienes: ")
        euro = float(euro)
        valor_dolar = 1.08
        dolares = euro / valor_dolar
        dolares = round(dolares, 2)
        dolares = str(dolares)
        print("Tienes: " + dolares + "$")
    else:
        print("La opcion ingresada es incorrecta") 


if __name__ == "__main__":
    run()