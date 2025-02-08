class nuevo:
    def __init__(self,objeto,numero):
        # usar _ significa por convencion que es preferible no modificar esa variable
        # pero en terminos de codigo es totalemte accesible
        self._objeto=objeto

        # usar __ bloquea el uso de esa variable mas no significa que sea imposible acceder a ella
        self.__numero=numero
    
class usemos(nuevo):
    # getters
    def get_numero(self):
        return self.__numero
    
    # setters
    def set_numero(self,cambio):
        self.__numero=cambio


a=usemos(10,20)
# print(a._nuevo__numero) | se puede usar pero no es la mejor opcion
a.set_numero(100)
print(a.get_numero())