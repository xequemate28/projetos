class Moto:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    # Método 1
    def ligar(self):
        print(f"A {self.marca} {self.modelo} de João Paulo está ligada.")
    
    # Método 2
    def desligar(self):
        print(f"A {self.marca} {self.modelo} de João Paulo foi desligada.")

# Criando dois objetos da classe Moto)
moto1 = Moto("Yamaha", "Ténéré")
moto2 = Moto("Honda", "XRE 300")

# Chamando métodos
moto1.ligar()
moto1.desligar()

moto2.ligar()
moto2.desligar()
