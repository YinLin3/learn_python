from os import system
from random import randint
from time import sleep
def clean():
    system("cls")

def inicio():
    print(a:="RPG\n1. Load Game\n2. New Game\n3. Exit")

    while True:
        try:
            inicio_num=int(input("\nelije una opcion.. "))
        except Exception as e:
            clean()
            print(e)
            print(a)
            continue
        if inicio_num in (1,2,3):
            break
        clean()
        print("invalid number, is not 1, 2 or 3")
        print(a)
        continue

    if inicio_num==1:
        with open("D:/lenguajes_programacion/python/learn_python/3/jugador.txt",mode="r",encoding="utf-8") as archivo:
            b=archivo.readlines()
            jugador1=player(b[0][:-1],float(b[1][:-1]),float(b[2][:-1]),float(b[3][:-1]),float(b[4][:-1]),float(b[5][:-1]),float(b[6][:-1]),float(b[7]))
        clean()
        print(f"Bienvenido de nuevo Jugador {jugador1.name}\n")
        input("Presione enter para continuar")
        clean()
        jugador1.menu()
    elif inicio_num==2:
        clean()
        name=input("ingrese su nombre.. ")
        jugador1=player(name,3,20,0.7,0.2)
        clean()
        print(f"Bienvenido Jugador {name}\n")
        input("Presione enter para continuar")
        clean()
        jugador1.menu()
    elif inicio_num==3:
        exit()

class unidad:
    def __init__(self,name:str,fuerza:float,vida:float,velocidad:float,escudo:float):
        self.name=name
        self.fuerza=fuerza
        self.vida=vida
        self.velocidad=velocidad
        self.escudo=escudo
    
    def atacar(self,atacante,atacado):
        atacado.vida-=atacante.fuerza-atacado.escudo
    
    def vivo(self,n1,n2):
        if n1.vida<=0:
            n1.vida=0
            return False
        if n2.vida<=0:
            n2.vida=0
            return False
        return True
        
    def luchar(self,p1,p2):
        vida_inicial=p1.vida
        if p1.velocidad>p2.velocidad: tv=(p1,p2)
        else: tv=(p2,p1)

        print("\t\t",p2.vida)
        print("\t\t",p2.name)
        print("\n\n",p1.vida)
        print(p1.name)
        print("empieza la batalla")
        sleep(0.5)

        while self.vivo(p1,p2):
            sleep(1)
            clean()
            self.atacar(tv[0],tv[1])
            self.vivo(p1,p2)
            print("\t\t",p2.vida)
            print("\t\t",p2.name)
            print("\n\n",p1.vida)
            print(p1.name)
            if self.vivo(p1,p2):
                self.atacar(tv[1],tv[0])
                self.vivo(p1,p2)
                print("\t\t",p2.vida)
                print("\t\t",p2.name)
                print("\n\n",p1.vida)
                print(p1.name)
                continue
            break
        if p1.vida==0:
            self.vida=vida_inicial
            print("PERDISTE")
        else:
            self.vida=vida_inicial
            p1.exp_actual+=p2.experiencia
            print("GANASTE!!!!!!")
            p1.level()
        input("enter para continuar")
        clean()
        self.menu_mundo1()


class enemigo(unidad):
    def __init__(self,name:str,fuerza:float,vida:float,velocidad:float,escudo:float,experiencia:float):
        self.name=name
        self.fuerza=fuerza
        self.vida=vida
        self.velocidad=velocidad
        self.escudo=escudo
        self.experiencia=experiencia

class player(unidad):
    def __init__(self,name:str,fuerza:float,vida:float,velocidad:float,escudo:float,exp_actual=0,exp_total=5,lvl=1):
        self.name=name
        self.fuerza=fuerza
        self.vida=vida
        self.velocidad=velocidad
        self.escudo=escudo
        self.exp_actual=exp_actual
        self.exp_total=exp_total
        self.lvl=lvl
    
    def level(self):
        while self.exp_actual>=self.exp_total:
            self.lvl+=1
            self.exp_actual%=self.exp_total
            self.exp_total*=1.3
            self.fuerza*=1.1
            self.vida*=1.1
            self.velocidad*=1.1
            self.escudo*=1.1
            print(f"subio a nivel {self.lvl}")

    def menu_mundo1(self):
        print(d:="Con quien desea luchar\n\n1. Enemigo1\n2. Enemigo2\n3. Enemigo3\n4. Boss1\n5. Regresar")
        while True:
            try:
                mundo1_num=int(input("\nelije una opcion.. "))
            except Exception as e:
                clean()
                print(e)
                print(d)
                continue
            if mundo1_num in (1,2,3,4,5):
                break
            clean()
            print("invalid number, is not 1, 2, 3, 4 or 5")
            print(d)
            continue
        if mundo1_num==1:
            rdm=randint(0,2)
            enemigo_creado=enemigo("enemigo1",2.7+(0.3*rdm),7.3+(0.7*rdm),0.4+(0.2*rdm),0.5+(0.25*rdm),1+(1*rdm))
            clean()
            self.luchar(self,enemigo_creado)
        elif mundo1_num==2:
            pass
        elif mundo1_num==3:
            pass
        elif mundo1_num==4:
            pass
        elif mundo1_num==5:
            clean()
            self.menu_mundos()

    def menu_mundos(self):
        print(c:="A que mundo quiere ir?\n\n1. Mundo1\n2. Mundo2\n3. Mundo3\n4. Mundo4\n5. Regresar")
        while True:
            try:
                mundo_num=int(input("\nelije una opcion.. "))
            except Exception as e:
                clean()
                print(e)
                print(c)
                continue
            if mundo_num in (1,2,3,4,5):
                break
            clean()
            print("invalid number, is not 1, 2, 3, 4 or 5")
            print(c)
            continue
        if mundo_num==1:
            clean()
            self.menu_mundo1()
        elif mundo_num==2:
            clean()
            self.menu_mundo1()
        elif mundo_num==3:
            clean()
            self.menu_mundo1()
        elif mundo_num==4:
            clean()
            self.menu_mundo1()
        elif mundo_num==5:
            clean()
            self.menu()
    
    def estadisticas(self):
        print(f"Estadisticas del Jugador: {self.name}\n\nnivel:       {self.lvl}\nfuerza:      {self.fuerza}\nvida:        {self.vida}\nvelocidad:   {self.velocidad}\nescudo:      {self.escudo}\nexperiencia: {self.exp_actual}/{self.exp_total}")
        input("\nPresione enter para continuar")
        clean()
        self.menu()
    
    def menu(self):
        print(b:="Que desea hacer?\n\n1. luchar\n2. estadisticas\n3. guardar")
        while True:
            try:
                menu_num=int(input("\nelije una opcion.. "))
            except Exception as e:
                clean()
                print(e)
                print(b)
                continue
            if menu_num in (1,2,3):
                break
            clean()
            print("invalid number, is not 1, 2 or 3")
            print(b)
            continue
        if menu_num==1:
            clean()
            self.menu_mundos()
        elif menu_num==2:
            clean()
            self.estadisticas()
        elif menu_num==3:
            clean()
            with open("D:/lenguajes_programacion/python/learn_python/3/jugador.txt",mode="w",encoding="utf-8") as archivo:
                a="\n"
                archivo.writelines([self.name,a+str(self.fuerza),a+str(self.vida),a+str(self.velocidad),a+str(self.escudo),a+str(self.exp_actual),a+str(self.exp_total),a+str(self.lvl)])
            inicio()

clean()
inicio()