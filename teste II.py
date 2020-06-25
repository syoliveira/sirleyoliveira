import string
paragrafo = input("Escreva um parágrafo: ")
for letra in string.ascii_lowercase:
    if paragrafo.find(letra) == paragrafo.find(letra.upper()) == -1:
        print(False)
        break
else:print(True)
    print("fim do exercicio")