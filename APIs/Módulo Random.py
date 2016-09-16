print("Módulo Random")

#Serve para que o próprio computador escolha números de forma aleatória

#A primeira função da biblioteca é o randrange que escolhe um número entre
#um intervalo de número apresentado

import random

print("Exemplo1:", random.randrange(5, 8))

#Também dá para definir o passo entre os números, podendo assim, decidir
#se o número escolhido será par ou ímpar

print("Exemplo2:", random.randrange(1,10, 2))

#Outra é o randint
#A diferença entre este e o randrange é  que o primeiro funciona como um range
#Excluindo o último número do intervalo, e este o inclui. E este não admite a
#denominação da passada

print("Exemplo3:", random.randint(1, 10))

#choice
#Escolhe o número a partir de uma sequência não vazia

print("Exemplo4:", random.choice("abcdefghijklmnopqrstwxyz"))

#random.random
#retorna números reais entre 0.0 e 1.0

print("Exemplo5: %.2f"%random.random())

#uniform
#Muito parecido com o random.randon, mas neste não necessariamente o intervalo
#será entre 0.0 e 1.0

print("Exemplo6: %.2f"%random.uniform(1, 20))

"""
Exercício: Criar uma maneira que não permita que um número par seja sorteado
entre 1 e um número escolhido pelo usuário.
"""

print("")
num = int(input("Digite um número: "))
from random import randrange as r
print("Número Sorteado: ",r(1, num+1, 2))
