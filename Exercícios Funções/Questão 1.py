'''
Crie uma função que receba três valores,
'a', 'b' e 'c', que são os coeficientes de uma equação do segundo grau e
retorne o valor do delta, que é dado por 'b² - 4ac'. Faça um pequeno programa
para testar sua função.
'''

def delta(a, b, c):
    delta = (b**2)-(4*a*c)

    return delta

print(delta(1 , -3 , -4))
