from modelos import (
    Cliente, TIPOS_CLIENTE, TIPOS_ATENCION, PRIORIDADES, CANTIDAD_FIJA, MAX_DIENTES
)
from validaciones import (
    leer_nombre, leer_solo_numeros, leer_entero_positivo,
    leer_opcion_menu, leer_fecha, leer_respuesta_sn
)
from procesos import (
    obtener_lista_urgentes, mostrar_informe_urgentes,
    construir_agenda, mostrar_agenda, atender_siguiente_cola
)

OPCIONES_MENU = [
    "Ver informe de extracciones urgentes",
    "Ver la agenda (Cola de atención)",
    "Atender al siguiente cliente de la Cola",
    "Salir"
]


def capturar_cliente():
    """Pide y valida por teclado todos los datos de un cliente y arma un objeto Cliente."""
    print("\n--- Datos del cliente ---")
    cedula = leer_solo_numeros("Cédula: ", longitud_min=6, longitud_max=12)
    nombre = leer_nombre("Nombre: ")
    telefono = leer_solo_numeros("Teléfono: ", longitud_min=7, longitud_max=10)

    tipo_cliente = leer_opcion_menu("Tipo de Cliente:", TIPOS_CLIENTE)
    tipo_atencion = leer_opcion_menu("Tipo de Atención:", TIPOS_ATENCION)

    cantidad_fija = CANTIDAD_FIJA.get(tipo_atencion)
    if cantidad_fija is not None:
        cantidad = cantidad_fija
        print(f"(La cantidad para {tipo_atencion} se fija automáticamente en {cantidad})")
    else:
        # Calzas y Extracción: la cantidad no puede superar 32 (total de dientes)
        cantidad = leer_entero_positivo(f"Cantidad de {tipo_atencion}: ", maximo=MAX_DIENTES)

    prioridad = leer_opcion_menu("Prioridad de Atención:", PRIORIDADES)
    fecha_cita = leer_fecha("Fecha de la cita (dd/mm/aaaa): ")

    return Cliente(
        cedula=cedula,
        nombre=nombre,
        telefono=telefono,
        tipo_cliente=tipo_cliente,
        tipo_atencion=tipo_atencion,
        cantidad=cantidad,
        prioridad=prioridad,
        fecha_cita=fecha_cita
    )


def main():
    arreglo_clientes = []  # Lista con todos los clientes registrados

    print("--- Consultorio Odontológico - Dr. XXX ---")

    try:
        seguir_registrando = True
        while seguir_registrando:
            cliente = capturar_cliente()
            arreglo_clientes.append(cliente)
            print(f"\nCliente {cliente.nombre} registrado correctamente.")

            respuesta = leer_respuesta_sn("¿Desea registrar otro cliente? (s/n): ")
            if respuesta == "n":
                seguir_registrando = False

        # Plan de contingencia: lista de extracciones urgentes
        lista_urgentes = obtener_lista_urgentes(arreglo_clientes)
        mostrar_informe_urgentes(lista_urgentes)

        # Agenda del día: Cola de atención
        cola_agenda = construir_agenda(arreglo_clientes)
        mostrar_agenda(cola_agenda)

        # Menú para consultar informes y atender clientes
        seguir_en_menu = True
        while seguir_en_menu:
            opcion = leer_opcion_menu("Menú principal:", OPCIONES_MENU)

            if opcion == OPCIONES_MENU[0]:
                mostrar_informe_urgentes(lista_urgentes)
            elif opcion == OPCIONES_MENU[1]:
                mostrar_agenda(cola_agenda)
            elif opcion == OPCIONES_MENU[2]:
                atender_siguiente_cola(cola_agenda)
            else:
                seguir_en_menu = False

        print("\nPrograma finalizado.")

    except Exception as error:
        # Red de seguridad final: ningún error no previsto debe cerrar el programa de golpe con una traza de error para el usuario final.
        print(f"\nOcurrió un error inesperado: {error}")
        print("El programa se cerrará de forma segura.")


if __name__ == "__main__":
    main()
