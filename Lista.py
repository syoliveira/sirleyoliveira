"""==============Exercício 01 ================================"""
"""tentei fazer de uma outra forma mais não consegui entender
como poderia inverter o triangulo"""

for i in range(10):
    print((i - 1) * "*")

print()
"""========================================================="""
print("*")
print("**")
print("***")
print("****")
print("***")
print("**")
print("*")
print('fim do exercício - não consegui fazer com loop')

"""==============Exercício 02 ================================"""


def triagulo(n):
    return "\n".join([" " * (n - i) + "*" * (i + i - 1) for i in range(1, n + 1)])


numero = int(input("quantas quantos asteriscos vc quer?: "))
print(triagulo(numero))

print('fim do exercício')

"""============== Exercício 03 ================================"""
x = 23
while x <= 83:
    if x % 3 == 0 and x % 5 == 0:
        print("PumBla")
    elif x % 3 == 0:
        print("Pum")
    elif x % 5 == 0:
        print("Bla")
    else:
        print(x)
    x = x + 1
print('fim do exercício')

"""============== Exercício 04 ================================"""
ano_mae = 1954
    nasc = ano_mae
    while nasc <= 2727:
    if nasc % 13 == 0 and nasc % 19 == 0:
        print(nasc)
        nasc = {nasc} + 1

"""============== Exercício 05 ================================"""
l = input("coloque uma letra aqui :")
v = ["a", "e", "i","o", "u"]
if not (l in v):
    print("maravilha: colocou uma consoante!")
else:
    print("A letra colocada não é consoante")

"""============== Exercício 06 ================================"""
def funcao(texto):
    return len(texto)*10
print(funcao("vida"))

"""============== Exercício 07 ================================"""
print("não consegui fazer")

"""============== Exercício 08 ================================"""
print("não consegui fazer")

"""============== Exercício 09 ================================"""
print("não consegui fazer")

"""============== Exercício 10 ================================"""
print("não consegui fazer")

"""============== Exercício 11 ================================"""
print("não consegui fazer")

"""============== Exercício 12 ================================"""
print("não consegui fazer")

"""============== Exercício 13 ================================"""

string = "1,000,568.987.765"
nstring = ""
for i in range(0,len(string)):
    if string[i] == ',': nstring = nstring + "."
    elif string[i] == '.': nstring = nstring + ","
    else: nstring = nstring + string[i]
print(nstring)
print("fim do exercicio")

"""============== Exercício 14 ================================"""
import string
paragrafo = input("Escreva um parágrafo: ")
for letra in string.ascii_lowercase:
    if paragrafo.find(letra) == paragrafo.find(letra.upper()) == -1:
        print(False)
        break
else:print(True)
    print("fim do exercicio")