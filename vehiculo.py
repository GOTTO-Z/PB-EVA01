class Vehiculo:

    def __int__(self, patente, marca, modelo, ano, capacidad, estado):
        self.patente = patente
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.capacidad = capacidad
        self.estado = estado

    def obtener_informacion(self):
        print(f"Numero de matricula: {self.patente}")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.ano}")
        print(f"capacidad maxima: {self.capacidad}")
        print(f"Estado: {self.estado}")

    def cambiar_estado(self, nuevo_estado):
        if self.estado == nuevo_estado:
            self.estado.capitalize() = "FINALIZADO"
            print("Ha finalizado su viaje")
        else:
            self.estado.capitalize() = "EN_CURSO"
            print("Ha iniziado un nuevo viaje")