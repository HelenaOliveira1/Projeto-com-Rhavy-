"""
Criar um programa que busque a ocorrência de uma letra numa frase.
Caso a letra seja encontrada imprimir a mensagem: Letra Encontrada.
Neste foi utilizada a API lowercase que transforma todas as letras
da frase em minúsculas, possibilitando melhor avaliação desta.
*Há também a variação uppercase, que transforma as letras em maiúsculas.
"""
frase = str(input("Digite a frase: "))
l = str(input("Digite a letra para ser encontrada: "))
sim = 0
frase = frase.lower()

for aux in frase:
    if (l == aux):
        sim += 1

print("Letra encontrada %i vez(es)" %sim )

