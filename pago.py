class Pago:
    def __init__(self, id, monto, metodo, estado):
        self.id = id
        self.monto = monto
        self.metodo = metodo
        self.estado = estado

    def obtener_monto(self):
        return self.monto
    

    def generar_comprobante(self):
        print("\n ---COMPROBANTE--- ")
        print(f"N° de voleta: {self.id}")
        print(f"Monto toatl: {self.monto}")
        print(f"Metodo de pago: {self.metodo}")
        print(f"Estado de el pago: {self.estado}")