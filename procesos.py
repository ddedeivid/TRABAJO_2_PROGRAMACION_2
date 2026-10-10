#    - Ordenan clientes por fecha de cita, arma la lista de extracciones urgentes y su informe, construye la cola de la agenda del día y atienden clientes

from datetime import datetime
from estructuras import Cola


def convertir_fecha(texto_fecha):
    return datetime.strptime(texto_fecha, "%d/%m/%Y")


def ordenar_por_fecha(arreglo_clientes):
    """Ordenamiento burbuja sobre una copia: fecha más cercana primero.
    Si dos fechas son iguales se respeta el orden en que se registraron."""
    arreglo = arreglo_clientes.copy()
    n = len(arreglo)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if convertir_fecha(arreglo[j].fecha_cita) > convertir_fecha(arreglo[j + 1].fecha_cita):
                arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]
    return arreglo


# Extracciones urgentes (plan de contingencia)

def filtrar_urgentes_extraccion(arreglo_clientes):
    """Solo clientes que vienen para extracción Y tienen prioridad Urgente."""
    urgentes = []
    for cliente in arreglo_clientes:
        if cliente.tipo_atencion == "Extracción" and cliente.prioridad == "Urgente":
            urgentes.append(cliente)
    return urgentes


def obtener_lista_urgentes(arreglo_clientes):
    """Lista de extracciones urgentes, de la fecha más cercana a la más lejana."""
    urgentes = filtrar_urgentes_extraccion(arreglo_clientes)
    return ordenar_por_fecha(urgentes)


def mostrar_informe_urgentes(lista_urgentes):
    print("\n--- Informe de extracciones urgentes ---")
    if len(lista_urgentes) == 0:
        print("No hay clientes con extracción urgente pendiente.")
        return

    print(f"Clientes para llamar: {len(lista_urgentes)} (de la fecha más cercana a la más lejana)")
    turno = 1
    for cliente in lista_urgentes:
        print(f"{turno}. Fecha: {cliente.fecha_cita} | Cédula: {cliente.cedula} | {cliente.nombre} | "
              f"Teléfono: {cliente.telefono} | Piezas a extraer: {cliente.cantidad}")
        turno += 1


# Cagenda del día

def construir_agenda(arreglo_clientes):
    ordenados = ordenar_por_fecha(arreglo_clientes)
    cola = Cola()
    for cliente in ordenados:
        cola.encolar(cliente)
    return cola


def mostrar_agenda(cola):
    print("\n--- Agenda (Cola de atención) ---")
    if cola.esta_vacia():
        print("La agenda está vacía: no hay clientes pendientes por atender.")
        return

    print(f"Clientes en la Cola: {cola.tamano()} (se atienden en este orden, del frente hacia atrás)")

    # Para recorrer la cola sin perder su contenido: se pasan los clientes a una cola auxiliar mientras se imprimen, y luego se devuelven a la original.
    cola_auxiliar = Cola()
    turno = 1
    while not cola.esta_vacia():
        cliente = cola.desencolar()
        print(f"{turno}. Fecha: {cliente.fecha_cita} | Cédula: {cliente.cedula} | {cliente.nombre} | "
              f"{cliente.tipo_atencion} x{cliente.cantidad} | Prioridad: {cliente.prioridad}")
        cola_auxiliar.encolar(cliente)
        turno += 1

    while not cola_auxiliar.esta_vacia():
        cola.encolar(cola_auxiliar.desencolar())


def atender_siguiente_cola(cola):
    cliente = cola.desencolar()
    if cliente is None:
        print("\nLa Cola está vacía: no quedan clientes por atender.")
        return

    print(f"\nAtendiendo a: {cliente.nombre} | Cédula: {cliente.cedula} | "
          f"{cliente.tipo_atencion} x{cliente.cantidad} | Prioridad: {cliente.prioridad} | "
          f"Fecha de la cita: {cliente.fecha_cita}")
    print(f"Clientes que quedan en la Cola: {cola.tamano()}")
