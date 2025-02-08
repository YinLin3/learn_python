import os
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')
limpiar_pantalla()

class abuelo1:
    def __init__(self,nombre):
        self.nombre=nombre
    def name(self):
        print("class abuelo1")
    def hablar(self):
        print(f"hola soy la class abuelo1 pero mi nombre es {self.nombre}\n")
class abuelo2:
    def __init__(self,nombre):
        self.nombre=nombre
    def name(self):
        print("class abuelo2")
    def hablar(self):
        print(f"hola soy la class abuelo2 pero mi nombre es {self.nombre}\n")

class hijo1(abuelo1,abuelo2):
    def __init__(self,nombre):
        self.nombre=nombre
    def hablar(self):
        self.name()
        print(f"hola soy la class hijo1 pero mi nombre es {self.nombre}\n")

class hijo2(abuelo2):
    def __init__(self,nombre):
        self.nombre=nombre
    def hablar(self):
        self.name()
        print(f"hola soy la class hijo2 pero mi nombre es {self.nombre}\n")
class nieto(hijo1):
    def __init__(self,nombre):
        self.nombre=nombre
    def hablar(self):
        self.name()
        print(f"hola soy la class nieto pero mi nombre es {self.nombre}")
        print("llamare a mi padre para que salude")
        super().hablar()
# entender que cada variable es un mundo distinto de abuelo,hijo,nieto
a=abuelo1("juan")
b=abuelo2("mario")
c=hijo1("luis")
d=hijo2("uwu")
e=nieto("owo")
lista=[a,b,c,d,e]
for x in lista:
    x.hablar()