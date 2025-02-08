import os
import random
import time
from itertools import islice
from collections import Counter
# funcion para limpiar pantalla
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')
limpiar_pantalla()
# inicio
def inicio():
    print("RPG")
    print("1. Load Game")
    print("2. Exit")
    print("3. New Game")
    try:
        inicio_num=int(input("elije una opcion.. "))
    except ValueError:
        print("Ingrese una opcion valida")
        exit()
    except Exception as e:
        print(f"Error inesperado: {e}")
        exit()
    if inicio_num==1:
        exit()
    elif inicio_num==2:
        exit()
    elif inicio_num==3:
        name=input("ingrese su nombre.. ")
        player=Juego_Jugador(name,10,2,10)
        limpiar_pantalla()
        print(f"Bienvenido Jugador {name}\n")
        input("Presione enter para continuar")
        player.menu()
    else:
        raise ValueError("Opcion no valida")

# Juego

class Juego_Jugador:
    def __init__(self,nombre,lvl,fuerza,vida):
        self.nombre=nombre
        self.lvl=lvl
        self.fuerza=fuerza
        self.vida=vida

    def ver_estadisticas(self):
        limpiar_pantalla()
        print(f"Estadisticas del Jugador: {self.nombre}\n")
        print(f"lvl:",self.lvl)
        print(f"fuerza:",self.fuerza)
        print(f"vida:",self.vida)
        input("Presione enter para regresar..")
        self.menu()
    def menu_lucha(self):
        limpiar_pantalla()
        for a,b in enumerate(lista_enemigo.values(),start=1):
            print(f"{a}. {b}")
        print(f"{a+1}. Regresar")

        try:
            menu_lucha_num=int(input("elije una opcion.. "))
        except ValueError:
            print("Ingrese una opcion valida")
            exit()
        except Exception as e:
            print(f"Error inesperado: {e}")
            exit()
        if menu_lucha_num in range(1,a+1):
            self.lucha(lista2[menu_lucha_num-1])
        elif menu_lucha_num==(a+1):
            self.menu()
        else:
            raise ValueError("Opcion no valida")
        
    def vivo(self):
        if self.vida>0:
            return True
        else:
            return False
    
    def verificar(self):
        if self.vida<0:
            self.vida=0
    
    def lucha(self,combatiente):
        combatiente.change()
        limpiar_pantalla()
        print(f"{self.nombre} vs {combatiente.nombre}\n")
        while self.vivo() and combatiente.vivo():
            print(f"{self.nombre} inflinge {self.fuerza:.2f} puntos de daño a {combatiente.nombre}")
            combatiente.vida-=self.fuerza
            print(f"{combatiente.nombre} inflinge {combatiente.fuerza:.2f} puntos de daño a {self.nombre}")
            self.vida-=combatiente.fuerza
            self.verificar()
            combatiente.verificar()
            print(f"vida de {self.nombre}:",self.vida,"y",f"vida de {combatiente.nombre}:",combatiente.vida,"\n")
        if self.vivo():
            print("Ganaste")
            input("presione enter para continuar.. ")
            self.menu_lucha()
        elif combatiente.vivo():
            print("Has muerto")
            exit()
        else:
            print("Empate, ambos luchadores estan muertos")
            exit()
    

    def menu(self):
        limpiar_pantalla()
        print("Que desea hacer?")
        print("1. ver estadisticas")
        print("2. luchar")
        print("3. guardar")
        print("4. exit")
        try:
            menu_num=int(input("elije una opcion.. "))
        except ValueError:
            print("Ingrese una opcion valida")
            exit()
        except Exception as e:
            print(f"Error inesperado: {e}")
            exit()
        if menu_num==1:
            limpiar_pantalla()
            self.ver_estadisticas()
        elif menu_num==2:
            self.menu_lucha()
        elif menu_num==3:
            exit()
        elif menu_num==4:
            exit()
        else:
            raise ValueError("Opcion no valida")
lista_enemigo={}
class enemigo(Juego_Jugador):
    def __init__(self,nombre,lvl,fuerza,vida):
        self.nombre=nombre
        self.lvl=lvl
        self.fuerza=fuerza
        self.vida=vida
    
    def change(self):
        enemigo_lvl=random.randint(self.lvl,self.lvl+4)
        self.fuerza=enemigo_lvl*self.fuerza
        self.vida=enemigo_lvl*self.vida

    def agregar_enemigo(self):
        global lista_enemigo
        lista_enemigo.update({self:self.nombre})

 # agregando enemigos
lista2=[]
rat=enemigo("rata",1,1.2,5)
rat.agregar_enemigo()
lista2.append(rat)

spider=enemigo("araña",6,1.5,10)
spider.agregar_enemigo()
lista2.append(spider)
# inicar juego
inicio()