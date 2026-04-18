def validate_number(numero, minimo, maximo):

    if len(numero) == 0:
        return False

    punto = False
    tiene_digito = False

    num = 0

    for num in range(len(numero)):
        num_2 = numero[num] 

        if num_2 == "-" and num == 0:
            continue

        elif num_2 == ".":
            if punto:
                return False
            punto = True

        elif num_2 >= "0" and num_2 <= "9":
            tiene_digito = True

        else:
            return False

    if not tiene_digito:
        return False

    valor = float(numero)

    if valor >= minimo and valor <= maximo:
        return True

    return False


def validate_length(texto, minimo, maximo):

    if len(texto) < minimo or len(texto) > maximo:
        return False

    for letra in range(len(texto)):
        nombre = texto[letra]

        if not (nombre >= 'A' and nombre <= 'Z') and not (nombre >= 'a' and nombre <= 'z'):
            return False

    return True
