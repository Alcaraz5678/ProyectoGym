import datetime

class Usuario:
    def __init__(self, nombre, documento):
        self.nombre = nombre
        self.documento = documento
        self.historial_reservas = []
        self.retos_cumplidos = []
        self.intervalos_seleccionados = set()

    def hacer_reserva(self, reserva):
        self.historial_reservas.append(reserva)
        self.intervalos_seleccionados.add(reserva.hora)
        print(f"Reserva confirmada para {self.nombre} el {reserva.fecha} a las {reserva.hora}.")

    def cancelar_reserva(self, reserva):
        if reserva in self.historial_reservas:
            reserva.estado = "Cancelada"
            self.intervalos_seleccionados.remove(reserva.hora)
            print(f"Reserva cancelada para {self.nombre} el {reserva.fecha} a las {reserva.hora}.")
        else:
            print("La reserva no se encuentra en el historial.")

    def ver_historial_reservas(self):
        print(f"Historial de reservas de {self.nombre}:")
        for reserva in self.historial_reservas:
            print(f"Fecha: {reserva.fecha}, Hora: {reserva.hora}, Estado: {reserva.estado}")

    def elegir_reto(self, reto):
        if reto not in self.retos_cumplidos:
            self.retos_cumplidos.append(reto)
            print(f"¡Felicitaciones! Te has registrado en el reto: {reto.descripcion}, ¡¡¡TU PUEDESSS¡¡¡")
        else:
            print("Ya has completado este reto anteriormente.")

class Reserva:
    def __init__(self, hora, estado="Confirmada"):
        self.fecha = datetime.datetime.now().strftime("%d/%m/%Y")
        self.hora = hora
        self.estado = estado

class Reto:
    def __init__(self, descripcion, objetivo, requisitos):
        self.descripcion = descripcion
        self.objetivo = objetivo
        self.requisitos = requisitos

    def ver_info_reto(self):
        print(f"Descripción: {self.descripcion}")
        print(f"Objetivo: {self.objetivo}")
        print(f"Requisitos: {self.requisitos}")

class Calendario:
    def __init__(self):
        self.reservas = {}

    def agregar_reserva(self, usuario, reserva):
        if usuario not in self.reservas:
            self.reservas[usuario] = []
        self.reservas[usuario].append(reserva)

    def mostrar_calendario(self):
        print("Calendario de Reservas:")
        for usuario, reservas in self.reservas.items():
            print(f"\nReservas de {usuario.nombre}:")
            for reserva in reservas:
                print(f"Fecha: {reserva.fecha}, Hora: {reserva.hora}, Estado: {reserva.estado}")

class Horario:
    def __init__(self, hora_inicio, hora_fin, capacidad_maxima):
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.capacidad_maxima = capacidad_maxima
        self.registros_actuales = 0

    def incrementar_registros(self):
        self.registros_actuales += 1

    def decrementar_registros(self):
        self.registros_actuales -= 1

    def hay_disponibilidad(self):
        return self.registros_actuales < self.capacidad_maxima

class Gimnasio:
    def __init__(self):
        self.horarios = {
            "8am-10am": Horario("8:00", "10:00", 20),
            "10am-12pm": Horario("10:00", "12:00", 20),
            "12pm-2pm": Horario("12:00", "14:00", 20),
            "2pm-4pm": Horario("14:00", "16:00", 20),
            "4pm-6pm": Horario("16:00", "18:00", 20),
            "6pm-8pm": Horario("18:00", "20:00", 20)
        }
        self.calendario = Calendario()

def inicio_sesion():
    usuarios_registrados = [
        {"nombre": "Juan", "documento": 12345},
        {"nombre": "María", "documento": 67890}
    ]
    nombre = input("Ingrese su nombre: ")
    documento = int(input("Ingrese su documento de identidad: "))
    for usuario in usuarios_registrados:
        if usuario["nombre"] == nombre and usuario["documento"] == documento:
            print("Inicio de sesión exitoso.\n")
            return Usuario(usuario["nombre"], usuario["documento"])
    print("No se encontró el usuario. Por favor, verifique sus datos.")
    return None

def menu_usuario(usuario, gimnasio):
    retos_disponibles = [
        Reto("Correr 5 kilómetros", "Correr 5 kilómetros seguidos", "Tener un buen estado físico"),
        Reto("Realizar 50 abdominales", "Realizar 50 abdominales seguidos", "Buena resistencia abdominal"),
        Reto("Hacer 20 flexiones de brazos", "Hacer 20 flexiones de brazos seguidas", "Buena fuerza en brazos")
    ]

    while True:
        print("\nMenú de Usuario")
        print("1. Ver Historial de Reservas")
        print("2. Hacer una Nueva Reserva")
        print("3. Cancelar una Reserva")
        print("4. Ver Retos Disponibles")
        print("5. Elegir un Reto")
        print("6. Mostrar Calendario")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            usuario.ver_historial_reservas()
        elif opcion == "2":
            print("Horarios disponibles:")
            for i, (horario, datos) in enumerate(gimnasio.horarios.items(), 1):
                print(f"{i}. {horario}: {datos.registros_actuales}/{datos.capacidad_maxima}")
            opcion_horario = input("Seleccione el número correspondiente al horario deseado: ")
            try:
                opcion_horario = int(opcion_horario)
                if 1 <= opcion_horario <= len(gimnasio.horarios):
                    horario_elegido = list(gimnasio.horarios.keys())[opcion_horario - 1]
                    horario = gimnasio.horarios[horario_elegido]
                    if horario.hay_disponibilidad() and horario_elegido not in usuario.intervalos_seleccionados:
                        reserva = Reserva(horario_elegido)
                        usuario.hacer_reserva(reserva)
                        gimnasio.calendario.agregar_reserva(usuario, reserva)
                        horario.incrementar_registros()
                    else:
                        print("¡Lo sentimos! El horario seleccionado está lleno o ya ha sido seleccionado.")
                else:
                    print("Opción de horario no válida.")
            except ValueError:
                print("Por favor, ingrese un número válido.")
        elif opcion == "3":
            if usuario.historial_reservas:
                print("Seleccione la reserva que desea cancelar:")
                for i, reserva in enumerate(usuario.historial_reservas):
                    print(f"{i + 1}. Fecha: {reserva.fecha}, Hora: {reserva.hora}, Estado: {reserva.estado}")
                indice = int(input("Ingrese el número de la reserva a cancelar: ")) - 1
                if 0 <= indice < len(usuario.historial_reservas):
                    reserva_cancelar = usuario.historial_reservas[indice]
                    horario_cancelar = gimnasio.horarios.get(reserva_cancelar.hora)
                    usuario.cancelar_reserva(reserva_cancelar)
                    horario_cancelar.decrementar_registros()  # Resta la cuenta de reservas
                    gimnasio.calendario.mostrar_calendario()
                else:
                    print("Opción no válida.")
            else:
                print("No tienes reservas para cancelar.")
        elif opcion == "4":
            print("Retos Disponibles:")
            for i, reto in enumerate(retos_disponibles, 1):
                print(f"{i}. {reto.descripcion}")
        elif opcion == "5":
            print("Seleccione un reto:")
            for i, reto in enumerate(retos_disponibles, 1):
                print(f"{i}. {reto.descripcion}")
            num_reto = int(input("Ingrese el número del reto que desea elegir: "))
            if 1 <= num_reto <= len(retos_disponibles):
                usuario.elegir_reto(retos_disponibles[num_reto - 1])
            else:
                print("Opción no válida.")
        elif opcion == "6":
            gimnasio.calendario.mostrar_calendario()
        elif opcion == "7":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    gimnasio = Gimnasio()
    usuario = inicio_sesion()
    if usuario:
        menu_usuario(usuario, gimnasio)


