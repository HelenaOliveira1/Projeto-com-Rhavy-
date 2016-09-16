print("Módulo Math")
print("")
"""
O módulo math, como o próprio nome sugere, importa cálculos matemáticos para o
programa, sem a necessidade de realmente cálcula-los. Para usá-lo é necessário
importar ele, pois ele não está presente no código.
"""

import math

#Quando já importado o módulo math, podemos utilizar suas funções
#Exemplo:

print("Exemplo1: seno de 12 = %.2f"%math.cos(12))
print("Exemplo2: raiz quadrada de 81 = ",math.sqrt(81))
print("Exemplo3: potência de 5 elevado a 3 = ",math.pow(5, 3))
print("Exemplo4: fatorial do número 5 = ", math.factorial(5))

# Também é possível invocar uma única função da biblioteca.
#Exemplo:

from math import pi

print("Exemplo5: constante pi = %.5f"%pi)
print("")

"""
Exercício: Calcular a área de um círculo, usando a constante pi, e recebendo
o valor do raio do círculo pelo usuário.
"""
from math import pi as p

raio = eval(input("Digite o valor do raio: "))
area = p*(raio**2)

print("Area = %.3f"%area)
