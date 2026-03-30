class Casa:
    propietario = "Juan Pérez"
    m2 = 500
    ubicacion = "Zona residencial norte"
    precio = 250000
    coordenada = "-12.0464, -77.0428"
    partida = "0501-001-000123"
    departamento = "Lima"
    provincia = "Lima"
    distrito = "San Isidro"

    def setpropietario(self, propietario):
        self.propietario = propietario

    def getpropietario(self):
        return self.propietario

    def setm2(self, m2):
        self.m2 = m2

    def getm2(self):
        return self.m2

    def setubicacion(self, ubicacion):
        self.ubicacion = ubicacion

    def getubicacion(self):
        return self.ubicacion

    def setprecio(self, precio):
        self.precio = precio

    def getprecio(self):
        return self.precio

    def setcoordenada(self, coordenada):
        self.coordenada = coordenada

    def getcoordenada(self):
        return self.coordenada

    def setpartida(self, partida):
        self.partida = partida

    def getpartida(self):
        return self.partida

    def setdepartamento(self, departamento):
        self.departamento = departamento

    def getdepartamento(self):
        return self.departamento

    def setprovincia(self, provincia):
        self.provincia = provincia

    def getprovincia(self):
        return self.provincia

    def setdistrito(self, distrito):
        self.distrito = distrito

    def getdistrito(self):
        return self.distrito

    def info_completa(self):
        return f"""
        Propietario: {self.propietario}
        Superficie: {self.m2} m²
        Ubicación: {self.ubicacion}
        Precio: S/. {self.precio:,}
        Coordenadas: {self.coordenada}
        Partida: {self.partida}
        Ubicación administrativa: {self.distrito}, {self.provincia}, {self.departamento}
        """

casa = Casa()

print("=== DATOS ORIGINALES ===")
print(casa.info_completa())

# Cambio de propietario
casa.setpropietario("María González")
casa.setm2(350)
casa.setprecio(180000)
casa.setubicacion("Zona residencial centro")
casa.setcoordenada("-12.0671, -77.0282")
casa.setpartida("0501-001-000456")
casa.setdistrito("San Isidro")

print("\n=== NUEVOS DATOS ===")
print(casa.info_completa())