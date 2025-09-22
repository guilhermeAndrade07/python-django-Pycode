# Herança


class Carro:
    numero_rodas = 4
    quant_passageiros = 5

    def acelerar(self):
        print("Acelerando...")
    
    def freiar(self):
        print("Freiando...")
    
    def buzinar(self):
        print("BIIIIIIIII, BIIIIII...")

class Uno(Carro):
    modelo = "Uno"
    marca = "Fiat"
    ano = 1992

uno = Uno()
uno.acelerar()
print(uno.marca)
