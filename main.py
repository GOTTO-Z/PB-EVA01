from pasajero import Pasajero
from conductor import Conductor
from vehiculo import Vehiculo
from pago import Pago
from persona import Persona



def main():
    pass
    # Crear pasajeros#
    pasajero_1 = Pasajero(1, "Gotoh", "ggotho72@hunxhunmail.cl", "666-908", "Transferencia", 3.4)
    pasajero_2 = Pasajero(2, "Leon", "lleonn@gmail.com", "453-893", "efectivo", 4.5)

    # Crear vehículos#
    vehiculo_1 = Vehiculo("4H12", "Toyota", "desonocido", 2012, 50, "EN_CURSO")
    vehiculo_2 = Vehiculo("CC13", "Lenovo", "thinpad", 2010, 60, "FINALIZADO")


    # Crear conductores#
    conductor_1 = Conductor(1, "Juan", "juanperz@papu.cl", "323-123", True, vehiculo_1)
    conductor_2 = Conductor(2, "Benjamin", "benja777qgmail.com", "254-375", False, vehiculo_2)


    # Actualizar teléfono

    print(pasajero_1)
    pasajero_1 = Persona.actualizarTelefono("234-123")
    print(pasajero_1)


    # Solicitar viaje
    viaje1 = pasajero_1.solicitarViaje(
        "Plaza de Armas",
        "Universidad"
    )

    # Conductor acepta
    conductor_1.aceptarViaje(viaje1)
    
    

    # Definir distancia
    viaje1.distancia = 5.0

    # Calcular tarifa
    viaje1.calcularTarifa()

    # Iniciar viaje

    
    

    # Finalizar viaje




    # Mostrar información
    # print("Estado:", viaje1.estado)
    # print("Tarifa:", viaje1.tarifa)

    # Generar pago
    # pago1 = Pago(
    #     1,
    #     viaje1.tarifa,
    #     pasajero1.metodoPago,
    #     "PAGADO"
    # )

    # print("Monto del pago:", pago1.obtenerMonto())

    # pago1.generarComprobante()



    # Calificar viaje



if __name__ == "__main__":
    main()

#Link hacia el Fork relizado por mi
#https://github.com/GOTTO-Z/PB-EVA01.git