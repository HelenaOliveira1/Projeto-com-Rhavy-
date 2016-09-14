'''
Crie um aplicativo de conversão entre as temperaturas Celsius e Farenheit.
Primeiro o usuário deve escolher se vai entrar com a temperatura em Célsius ou
Farenheit, depois a conversão escolhida é realizada através de um comando
SWITCH (if).
Se C é a temperatura em Célsius e F em farenheit, as fórmulas de conversão são:
C= 5.(F-32)/9
F= (9.C/5) + 32
    Use funções para modularizar seu programa. 
'''

def geral(entrada, temp):
    
    def faren(temp):
        conver = (9*(temp/5)) + 32

        return print("A temperatura em Graus Farenheit é", conver)

    def celsius(temp):
        conver = (5*(temp-32))/9

        return print("A temperatura em Graus Celsius é", conver)


    if (entrada == 1):
        faren(temp)

    else:
        celsius(temp)
        
    return 

entrada = int(input("Digite qual temperatura será usada Celsius(1) ou Farenheit(2): "))
temp = int(input("Digite a temperatura: "))

geral(entrada, temp)
