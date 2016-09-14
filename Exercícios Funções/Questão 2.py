'''
calcula as raízes de uma equação do 2o grau:
ax² + bx + c=0
Para ela existir, o coeficiente 'a' deve ser diferente de zero.
No caso de a ser igual a zero, envie uma mensagem de erro ao usuário.
Caso o delta seja maior ou igual a zero, as raízes serão reais.
Caso o delta seja negativo, exiba a mensagem: As raízes são números complexos.
'''
def delta_r(a, b, c):
    delta = (b**2)-(4*a*c)
    return delta

def equacao(a, b, c):
    global delta
    from math import sqrt
   
    if (a != 0):
        if (delta >= 0):
            xI = (-(b) + sqrt(delta))/(2*a)
            xII = (-(b) - sqrt(delta))/(2*a)
            print("Solução:", xI, "e", xII)
        else:
            print("As raízes são números complexos.")
    else:
        print("Coeficiente 'a' inválido!") 
    return
   
a = eval(input("Digite o coeficiente 'a': "))
b = eval(input("Digite o coeficiente 'b': "))
c = eval(input("Digite o coeficiente 'c': "))

delta = delta_r(a,b,c)
equacao(a, b, c)
