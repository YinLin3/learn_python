import os
import random
from collections import Counter
# funcion para limpiar pantalla
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')
limpiar_pantalla()
# interfaz
print("RPG")
print("1. Load Game")
print("2. exit")
print("3. New Game")
try:
    eleccion=int(input("elije una opcion.. "))
except ValueError:
    print("Ingrese una opcion valida")
    exit()
except Exception as e:
    print(f"Error inesperado: {e}")
    exit()
if eleccion not in range(1,4):
    raise ValueError("Opcion no valida")

# enemigos (fuerza,inteligencia,escudo,vida,arma)
enemigos={}
# Clases
class enemigo:
    def __init__(self,lvl_min,nombre,fuerza,inteligencia,escudo,vida,arma,exp,drops):
        self.lvl_min=lvl_min
        self._nombre=nombre
        self.fuerza=fuerza
        self.inteligencia=inteligencia
        self.escudo=escudo
        self.vida=vida
        self.arma=arma
        self.exp=exp
        self.drops=drops
    def agregar(self):
        enemigos.update({
            self._nombre:[list(range(self.lvl_min,self.lvl_min+10))]})
    def soltar(self):
        bolsa=[f"{self.exp} exp"]
        if self.drops!={}:
            for dropeo in self.drops:
                if (random.randint(1,self.drops[dropeo]))==self.drops[dropeo]:
                    bolsa.append(dropeo)


class jugador:
    def __init__(self,nombre,lvl,fuerza,inteligencia,escudo,vida,arma):
        self.lvl=lvl
        self._nombre=nombre
        self.fuerza=fuerza
        self.inteligencia=inteligencia
        self.escudo=escudo
        self.vida=vida
        self.arma=arma
    def change_weapon(self):
        pass
    def estadisticas(self):
        print(f"Estadisticas del jugador {self._nombre}:")
        print("lvl:",self.lvl)
        print("fuerza:",self.fuerza)
        print("inteligencia:",self.inteligencia)
        print("escudo:",self.escudo)
        print("vida:",self.vida)
        print("arma:",self.arma,"\n")
        print("1. cambiar de arma")
        print("2. regresar al menu")
        try:
            eleccion3=int(input("elije una opcion.. "))
        except ValueError:
            print("Ingrese una opcion valida")
            exit()
        except Exception as e:
            print(f"Error inesperado: {e}")
            exit()
        if eleccion3 not in range(1,3):
            raise ValueError("Opcion no valida")
        if eleccion3==1:
            self.change_weapon()
        if eleccion3==2:
            self.menu()
    
    def lucha(self,combatiente):
        limpiar_pantalla()
        print(combatiente)

    def menu_lucha(self):
        limpiar_pantalla()
        print("Con quien desea pelear?")
        a=0
        for x in enemigos:
            print(f"{a+1}. {x}")
            a+=1
        print(f"{a+1}. regresar")
        print(f"{a+2}. exit")
        try:
            eleccion4=int(input("elije una opcion.. "))
        except ValueError:
            print("Ingrese una opcion valida")
            exit()
        except Exception as e:
            print(f"Error inesperado: {e}")
            exit()
        if eleccion4 not in range(1,a+3):
            raise ValueError("Opcion no valida")
        
        dicc={}
        b=1
        for y in enemigos: 
            dicc.update({b:y})
            b+=1
        if eleccion4 in dicc:
            self.lucha(dicc[eleccion4])
        elif eleccion4==(a+1):
            self.menu()
        elif eleccion4==(a+2):
            exit()

    def menu(self):
        limpiar_pantalla()
        print("Que desea hacer?")
        print("1. ver estadisticas")
        print("2. luchar")
        print("3. exit")
        try:
            eleccion2=int(input("elije una opcion.. "))
        except ValueError:
            print("Ingrese una opcion valida")
            exit()
        except Exception as e:
            print(f"Error inesperado: {e}")
            exit()
        if eleccion2 not in range(1,4):
            raise ValueError("Opcion no valida")
        if eleccion2==1:
            limpiar_pantalla()
            self.estadisticas()
        elif eleccion2==2:
            self.menu_lucha()
        elif eleccion2==3:
            exit()

# Agregando enemigos
rata=enemigo(1,"rata",1.5,0,5,50,None,5,{})
rata.agregar()
araña=enemigo(11,"araña",2,0,5,100,None,15,{})
araña.agregar()
boss_1=enemigo(21,"boss_1",4,1,5,300,None,100,{"Espada":30})
boss_1.agregar()
    
# Juego
if eleccion==1:
    exit()
elif eleccion==2:
    exit()
elif eleccion==3:
    name=input("ingrese su nombre.. ")
    player=jugador(name,1,10,10,10,100,"None")

limpiar_pantalla()
print(f"Bienvenido Jugador {name}\n")
input("presione enter para continuar")
player.menu()