'''
- Módulo: validaciones.py
- Funciones sueltas para leer datos del teclado de forma segura. Si el
  usuario se equivoca, se le vuelve a preguntar sin cerrar el programa:
    - Campo vacío
    - Nombre con números o símbolos
    - Texto donde se esperaba número
    - Números negativos, cero, o por encima del máximo permitido
    - Longitud inválida (cédula/teléfono demasiado cortos o largos)
    - Opción de menú no numérica o fuera de rango
    - Fecha con formato inválido o en el pasado
    - Respuesta s/n inválida
'''

from datetime import datetime


def leer_nombre(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor == "":
            print("  ERROR: el nombre no puede quedar vacío. Intente de nuevo.")
            continue
        # isalpha() acepta letras con tilde y ñ, pero no números ni símbolos
        if not valor.replace(" ", "").isalpha():
            print("  ERROR: el nombre solo puede contener letras y espacios (sin números ni símbolos). Intente de nuevo.")
            continue
        return valor


def leer_solo_numeros(mensaje, longitud_min=1, longitud_max=15):
    while True:
        valor = input(mensaje).strip()
        if valor == "":
            print("  ERROR: este campo no puede quedar vacío. Intente de nuevo.")
            continue
        if not valor.isdigit():
            print("  ERROR: solo se permiten números (sin espacios ni letras). Intente de nuevo.")
            continue
        if not (longitud_min <= len(valor) <= longitud_max):
            print(f"  ERROR: debe tener entre {longitud_min} y {longitud_max} dígitos. Intente de nuevo.")
            continue
        return valor


def leer_entero_positivo(mensaje, maximo=1000):
    while True:
        valor = input(mensaje).strip()
        if valor == "":
            print("  ERROR: este campo no puede quedar vacío. Intente de nuevo.")
            continue
        try:
            valor_int = int(valor)
        except ValueError:
            print("  ERROR: debe ingresar un número entero válido. Intente de nuevo.")
            continue
        if valor_int <= 0:
            print("  ERROR: la cantidad debe ser mayor que cero. Intente de nuevo.")
            continue
        if valor_int > maximo:
            print(f"  ERROR: la cantidad no puede ser mayor que {maximo}. Intente de nuevo.")
            continue
        return valor_int


def leer_opcion_menu(titulo, opciones):
    while True:
        print(f"\n{titulo}")
        for i, op in enumerate(opciones, start=1):
            print(f"  {i}. {op}")
        seleccion = input("Seleccione una opción: ").strip()
        if seleccion == "":
            print("  ERROR: debe seleccionar una opción. Intente de nuevo.")
            continue
        if not seleccion.isdigit():
            print("  ERROR: ingrese el número de la opción. Intente de nuevo.")
            continue
        indice = int(seleccion)
        if indice < 1 or indice > len(opciones):
            print("  ERROR: opción fuera de rango. Intente de nuevo.")
            continue
        return opciones[indice - 1]


def leer_fecha(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor == "":
            print("  ERROR: la fecha no puede quedar vacía. Intente de nuevo.")
            continue
        try:
            fecha_ingresada = datetime.strptime(valor, "%d/%m/%Y")
        except ValueError:
            print("  ERROR: formato de fecha inválido. Use dd/mm/aaaa. Intente de nuevo.")
            continue
        if fecha_ingresada.date() < datetime.now().date():
            print("  ERROR: la fecha de la cita no puede ser una fecha pasada. Intente de nuevo.")
            continue
        return valor


def leer_respuesta_sn(mensaje):
    while True:
        valor = input(mensaje).strip().lower()
        if valor in ("s", "n"):
            return valor
        print("  ERROR: responda solamente 's' para sí o 'n' para no. Intente de nuevo.")
