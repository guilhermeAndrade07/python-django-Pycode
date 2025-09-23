# Polimorfismo de Interface

class Forma(): # Classe Base

    def area(self):
        pass


class Quadrado(Forma): #Classe especifica que herda de Forma

    def __init__(self, lado): # é obrigatório ao chamar a classe quadrado, informar o valor do lado
        self.lado = lado

    def area(self): # função para calcular a area 
        return f"A área do quadrado é {self.lado ** 2}"
    
class Circulo(Forma):

    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return 3.14 * self.raio ** 2


quadrado = Quadrado(5)
area_quadrado = quadrado.area()
print(area_quadrado)

circulo = Circulo(4)
area_circulo = circulo.area()
print(area_circulo)