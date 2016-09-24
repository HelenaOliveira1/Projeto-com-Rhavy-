
class Quadrado():
    def __init__(self):
        self.lado = int(input("Digite lado: "))
        print("Tamanho de lado definido com Sucesso")
"""
Criar classe que modele quadrado

Atributos: Lado do Quadrado
Métodos: Mudar Valor do lado, Retornar Valor do Lado, Calcular Area do Quadrado

"""
    def muda_lado(self):
        self.lado = int(input("Digite lado: "))
        print("Tamanho de lado mudado com Sucesso")
   
    def Retorno(self):
        print("Tamanho de lado igual a: ", self.lado)
   
    def Area(self):
        area = self.lado*self.lado
        print("Area do quadrado igual a: ", area)

quadrado = Quadrado()
print("")
def menu():
    func = int(input("Mudar tamanho do lado(1), Retornar valor do lado(2), Calcular area do quadrado(3)? "))
    if (func == 1):
        quadrado.muda_lado()
    elif (func == 2):
        quadrado.Retorno()
    elif (func == 3):
        quadrado.Area()
    else:
        print("Função não Suportada")

menu()

print("")
op = int(input("Deseja fazer mais algo? sim(1) , não(2) "))

while (op == 1):
    menu()
    print("")
    op = int(input("Deseja fazer mais algo? sim(1) , não(2) "))

print("Até a próxima!")




        
