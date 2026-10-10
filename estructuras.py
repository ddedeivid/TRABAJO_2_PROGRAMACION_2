#  Guarda sus elementos en una lista interna y solo se usa a través de  sus propios métodos 


class Cola:
    def __init__(self):
        self.elementos = []

    def encolar(self, elemento):
        # Agrega al final de la cola
        self.elementos.append(elemento)

    def desencolar(self):
        # Saca y devuelve el elemento del frente (None si la cola está vacía)
        if self.esta_vacia():
            return None
        return self.elementos.pop(0)

    def ver_frente(self):
        if self.esta_vacia():
            return None
        return self.elementos[0]

    def esta_vacia(self):
        return len(self.elementos) == 0

    def tamano(self):
        return len(self.elementos)
