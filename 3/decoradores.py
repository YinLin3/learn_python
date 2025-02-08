import os
import functools
from typing import overload
def a():
    os.system("cls")
a()

'''
self es el nombre con que llamaremos a la instancia se usa por convencion
al usar @classmethod el primer parametro es para llamar a la clase se usa cls por convencion
'''


class nose:
    invitados=10
    def __init__(self,nombre,apellido,edad):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad

    # @staticmethod indica que el metodo no necesita de self ni clase, por ende no puede acceder a los atributos
    @staticmethod
    def suma(a,b):
        return a+b
    
    # @classmethod puede llamar a las variables de la clase y a la misma clase
    @classmethod
    def agregar_cliente(cls,cadena):
        nombre,apellido,edad=cadena.split(",")
        return cls(nombre,apellido,int(edad))
    
    @classmethod
    def aumentar(cls):
        cls.invitados+=1

    def get_valores(self):
        return self.nombre,self.apellido,self.edad
    
    # @property convierte un metodo en atributo | @.setter le da la capacidad de ser modificado
    @property
    def bocaditos(self):
        return nose.invitados * 5
    
    @bocaditos.setter
    def bocaditos(self,total):
        if total<0 or (total%5)!=0:
            raise ValueError("Error")
        nose.invitados=int(total/5)

    # @functools.lru_cache guarda los valores y en la proxima ya no los calcula, si se llena borra el mas antiguo
    @functools.lru_cache(maxsize=1)
    def multiplicar(numero:int,multiplicador:int):
        return numero*multiplicador

    # @overload
    @overload
    def cumpleaños(self,dia:int,mes:str,año:int) -> str: pass
    
    def cumpleaños(self,dia,mes,año):
        return f"tu cumpleaños es el {dia} de {mes} del {año}"




print(nose.suma(1,2))
a:nose=nose.agregar_cliente("jose,ruiz,17")
print(a.get_valores())
a.aumentar()
print(nose.invitados)
print(a.bocaditos)
a.bocaditos=500
print(a.bocaditos)
print(nose.multiplicar(3,6))
print(a.cumpleaños(3,"marzo",2008))