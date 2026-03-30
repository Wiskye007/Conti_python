class Coche:
    def __init__(self):
        self.color = "rojo"
        self.marca = "Nissan"
        self.modelo = "AD"
        self.velocidad = 300
        self.caballaje = 500
        self.plazas = 2

    def setcolor(self, color):
        self.color = color

    def getcolor(self):
        return self.color

    def setmarca(self, marca):
        self.marca = marca

    def getmarca(self):
        return self.marca

    def setmodelo(self, modelo):
        self.modelo = modelo

    def getmodelo(self):
        return self.modelo

    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def getvelocidad(self):
        return self.velocidad


# Crear instancia fuera de la clase
Coche = Coche()

Coche.setcolor("rojo")
Coche.setmarca("Nissan")
Coche.setmodelo("AD")

print(Coche.marca, Coche.getmodelo(), Coche.getcolor())
print("Velocidad actual: ", Coche.getvelocidad())

Coche.acelerar()
Coche.acelerar()
Coche.acelerar()

Coche.frenar()
Coche.frenar()

print("Velocidad nueva: ", Coche.getvelocidad())


