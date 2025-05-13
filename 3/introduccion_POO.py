class contar:
    def __init__(self, palabra):
        self.palabra = palabra

    def __len__(self):
        longitud = len(self.palabra)
        return longitud

# Ejemplo de uso
objeto = contar("Hola")
print(objeto.palabra)
print(objeto.__len__())