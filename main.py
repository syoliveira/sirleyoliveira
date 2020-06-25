"""numero = int(input("digite um numero:"))
print(numero)
#numero = str (numero)

print(numero)

boleano = True
if numero % 2 == 0:
    print("numero par")
if numero < 5:
    print("numero menor")
elif numero == 5:
    print("numero igual")
else:
    print("numero maior")"""


"""numeroA = int(input("digite o 1ª numero:"))
numeroB = int(input("digite o 2º numero:"))
soma = numeroA + numeroB
print(soma)
if soma % 2 == 0:
    print("numero par")
else:
    print("numero impar")
if soma > 20:
    print("maior que 20")"""


"""==============================================================="""

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
sexo = input("Digite o sexo: ")

ano = 2020 - idade
ano = str(ano)
print(nome + " você nasceu em " + ano)
if sexo =="masculino":
    mulher = False
else:
    mulher = True

if mulher:
    print("Você é uma bela mulher")
    print(f"Sua idade parece ser {idade-1}")
else:
    print("Você é um cabra")
    print(f"Mas tu é {sexo} mesmo?")
print("fim do codigo")