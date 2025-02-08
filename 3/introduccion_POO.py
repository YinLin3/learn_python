class contar:
    def __init__(self, palabra):
        self.palabra = palabra

    def __str__(self):
        longitud = len(self.palabra)
        return "string bby"

# Ejemplo de uso
objeto = contar("Hola")
print(objeto.palabra)
print(objeto.__str__())