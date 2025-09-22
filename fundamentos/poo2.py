# Polimorfismo
# Polimorfismo → “uma mesma ação, mas cada um faz do seu jeito” 
# (todos se movem, mas de formas diferentes).

class Transporte:
    def mover(self):
        pass

class Carro(Transporte):
    def mover(self):
        return "Dirigindo pelas ruas 🚗"

class Bicicleta(Transporte):
    def mover(self):
        return "Pedalando pela ciclovia 🚴"

class Aviao(Transporte):
    def mover(self):
        return "Voando pelos céus ✈️"

transportes = [Carro(), Bicicleta(), Aviao()]

for t in transportes:
    print(t.mover())
