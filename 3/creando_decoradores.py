import os
import time
def a():
    os.system("cls")
a()

class deco:
    # decorador basico
    def confirmacion(func):
        def decorador2():
            print("inicio")
            func()
            print("final\n")
        return decorador2
    
    @confirmacion
    def saludar1():
        print("hola bro1")

    # decorador para funciones con parametros
    def multiplicador(func):
        def decorador3(a,b):
            print("hola "*a)
            func()
            print("adios "*b+"\n")
        return decorador3
    
    @multiplicador
    def saludar2():
        print("hola bro2")

    # decorador con parametro
    def añadir_tiempo(tiempo):
        def decorador1(func):
            def abc():
                time.sleep(tiempo)
                return func()
            return abc
        return decorador1
    @añadir_tiempo(4)
    def saludar3():
        return "hola bro3"
deco.saludar1()
deco.saludar2(3,4)
print(deco.saludar3())