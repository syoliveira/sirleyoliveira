def funcao(aniversario):
    aniversario = aniversario + 258
    primos = [2]
    for numerador in range(3, aniversario + 1):
        for denominador in range(2, numerador):
            if numerador % denominador == 0:
                break
        else: primos.append(numerador)
    return primos