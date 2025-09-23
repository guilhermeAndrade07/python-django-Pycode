# Polimorfismo de Interface

class Forma(): # Classe Base

    def area(self):
        pass


class Quadrado(Forma): 

    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2
    

quadrado = Quadrado(5)
area_quadrado = quadrado.area()
print(area_quadrado)