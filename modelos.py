TIPOS_CLIENTE = ["Particular", "EPS", "Prepagada"]
TIPOS_ATENCION = ["Limpieza", "Calzas", "Extracción", "Diagnóstico"]
PRIORIDADES = ["Normal", "Urgente"]

# Limpieza y Diagnóstico siempre son cantidad 1
CANTIDAD_FIJA = {"Limpieza": 1, "Diagnóstico": 1}

# Nadie tiene más de 32 dientes: límite para Calzas y Extracción
MAX_DIENTES = 32


class Cliente:
    def __init__(self, cedula, nombre, telefono, tipo_cliente, tipo_atencion,
                 cantidad, prioridad, fecha_cita):
        self.cedula = cedula
        self.nombre = nombre
        self.telefono = telefono
        self.tipo_cliente = tipo_cliente
        self.tipo_atencion = tipo_atencion
        self.cantidad = cantidad
        self.prioridad = prioridad
        self.fecha_cita = fecha_cita

    def __repr__(self):
        return (
            f"Cliente(cedula={self.cedula}, nombre={self.nombre}, "
            f"tipo_atencion={self.tipo_atencion}, cantidad={self.cantidad}, "
            f"prioridad={self.prioridad}, fecha_cita={self.fecha_cita})"
        )
