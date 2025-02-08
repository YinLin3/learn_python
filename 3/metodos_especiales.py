import os
def a():
    os.system("cls")
a()
class nuevo:
    # __init__ se usa para inicializar los atributos de un objeto
    def __init__(self,nombre):
        self.nombre=nombre

    # __str__ define lo que sera devuelto al usar print()
    def __str__(self):
        return f"hola, me llamo {self.nombre}"
    
    # __repr__ define lo que sera devuelto al usar print(repr())
    def __repr__(self):
        return f"hola por segunda vez"
    
    # __len__ define lo que sera devuelto al usar print(len())
    def __len__(self):
        return len(self.nombre)

class listas:
    def __init__(self,lis):
        self.lis=lis

    # __getitem__ define lo que sera devuelto al usar print(variable[...])
    def __getitem__(self,num):
        return f"el elemento de indice {num} es {self.lis[num]}"
    
    # __setitem__ define lo que sera devuelto al usar variable[...]=
    def __setitem__(self,indice,valor):
        self.lis[indice]=valor
    
    # __del__ define lo que sera devuelto al usar del ...
    def __del__(self):
        print("objeto destruido con exito")

probar1=nuevo("mario")
print(probar1)
print(repr(probar1))
print(len(probar1))

probar2=listas([40,80,100])
print(probar2[1])
probar2[0]=30
del probar2
