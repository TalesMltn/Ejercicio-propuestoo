def obtener_divisores(numero):
    divisores = [i for i in range(1, numero + 1) if numero % i == 0]
    return divisores


def solicitar_numero_natural():
    while True:
        try:
            # Solicitar un número al usuario
            entrada = input("Introduce un número natural: ")
            numero = int(entrada)

            # Validar que sea un número natural positivo
            if numero <= 0:
                raise ValueError("El número debe ser un natural positivo.")

            return numero
        except ValueError as e:
            # Si el ingreso no es un número válido o es negativo, se muestra el error
            print(f"Entrada inválida: {e}. Por favor, inténtalo de nuevo.")


def main():
    numero = solicitar_numero_natural()
    divisores = obtener_divisores(numero)
    print(f"Los divisores de {numero} son: {divisores}")


if __name__ == "__main__":
    main()
