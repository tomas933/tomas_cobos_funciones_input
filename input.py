import validate

def get_int(mensaje: str, mensaje_error: str, minimo: int, maximo:int, reintentos: int) -> int|None:
    """
    Solicita al usuario el ingreso de un número entero validado con cantidad de intentos.

    Parámetros:
    mensaje (str): Texto que se muestra para solicitar el dato.
    mensaje_error (str): Mensaje que se muestra en caso de error.
    minimo (int): Valor mínimo permitido.
    maximo (int): Valor máximo permitido.
    reintentos (int): Cantidad de intentos permitidos.

    Retorna:
    int | None: Número entero válido o None si se agotan los intentos.
    """

    for entero in range(reintentos):
        dato = input(mensaje)

        if validate.validate_number(dato, minimo, maximo):
            return int(float(dato))

        print(mensaje_error)

    return None

###############################################

def get_float(mensaje: str, mensaje_error: str, minimo: int, maximo:int, reintentos: int) -> float|None:
    """
    Solicita al usuario el ingreso de un número decimal (float) validado con intentos.

    Parámetros:
    mensaje (str): Texto que se muestra para solicitar el dato.
    mensaje_error (str): Mensaje que se muestra en caso de error.
    minimo (int): Valor mínimo permitido.
    maximo (int): Valor máximo permitido.
    reintentos (int): Cantidad de intentos permitidos.

    Retorna:
    float | None: Número decimal válido o None si se agotan los intentos.
    """
    for flotante in range(reintentos):
        dato = input(mensaje)

        if validate.validate_number(dato, minimo, maximo):
            return float(dato)

        print(mensaje_error)

    return None

###############################################

def get_string(mensaje: str, mensaje_error: str, minimo: int , maximo: int, reintentos: int) -> str|None:
    """
    Solicita al usuario el ingreso de una cadena de texto validada con intentos.

    Parámetros:
    mensaje (str): Texto que se muestra para solicitar el dato.
    mensaje_error (str): Mensaje que se muestra en caso de error.
    minimo (int): Cantidad mínima de caracteres permitidos.
    maximo (int): Cantidad máxima de caracteres permitidos.
    reintentos (int): Cantidad de intentos permitidos.

    Retorna:
    str | None: Cadena válida o None si se agotan los intentos.
    """
    for string in range(reintentos):
        dato = input(mensaje)

        if validate.validate_length(dato, minimo, maximo):
            return dato

        print(mensaje_error)

    return None

# PRUEBA INT
entero = get_int("Ingrese un entero: ", "Error, entero inválido", 0, 120, 3)
print(f"Resultado entero: {entero}")


# PRUEBA FLOAT
flotante = get_float("Ingrese un float: ", "Error, float inválido", 0.5, 2.5, 3)
print(f"Resultado flotante: {flotante}")


# PRUEBA STRING
string = get_string("Ingrese un string: ", "Error string inválido", 2, 10, 3)
print(f"Resultado string: {string}")