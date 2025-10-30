class Persona:
    def __init__(self, nombre, nif, fecha_nac):
        self.nombre = nombre
        self.nif = nif
        self.fecha_nac = fecha_nac

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"NIF: {self.nif}")
        print(f"Fecha de nacimiento: {self.fecha_nac}")   

class Jugador(Persona):
    def __init__(self, nombre, nif, fecha_nac, numFed):
        super().__init__(nombre, nif, fecha_nac)
        self.numFed = numFed
    
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Numero de Federacion: {self.numFed}")


if __name__ == "__main__":
        jugador1 = Jugador("Juan", "7777", "04/10/2007", 1000)

        print("Informacion del jugador: ")
        jugador1.mostrar_informacion()