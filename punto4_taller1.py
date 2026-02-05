def cifrar(texto, llave):
    resultado = ""

    for letra in texto:
        if letra.isalpha():
            codigo = ord(letra) + llave

            
            if letra.islower():
                if codigo > ord('z'): #si me paso de la z 
                    codigo -= 26
                if codigo < ord('a'): #si me paso antes de la a
                    codigo += 26

            # para mayúsculas
            if letra.isupper():
                if codigo > ord('Z'): #si me paso de la Z
                    codigo -= 26
                if codigo < ord('A'): #si me paso antes de la A
                    codigo += 26

            resultado += chr(codigo)
        else:
            resultado += letra

    return resultado


def descifrar(texto, llave):
    return cifrar(texto, -llave) #es - la llave por que me debo devolver


def menu():
    print("=== CIFRADO CESAR ===")
    print("1. Cifrar")
    print("2. Descifrar")
    opcion = input("Seleccione una opción (1/2): ")

    texto = input("Ingrese el texto: ")
    llave = int(input("Ingrese la llave numérica: "))

    if opcion == "1":
        print("Texto cifrado:", cifrar(texto, llave))
    elif opcion == "2":
        print("Texto descifrado:", descifrar(texto, llave))
    else:
        print("Opción inválida")


if __name__ == "__main__":
    menu()
