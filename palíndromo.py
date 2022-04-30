def palíndromo(palabra):
    palabra = palabra.replace(" ", "")
    palabra = palabra.lower()
    palabra_inv = palabra[::-1]
    if palabra == palabra_inv:
        return True
    else:
        return False


def run():
    palabra = input("🥶 Escribe una palabra:")
    es_palindromo = palíndromo(palabra)
    if es_palindromo == True:
        print("Es polindromo")
    else:
        print("No es un polindromo hdtpm")


if __name__ == "__main__":
    run()