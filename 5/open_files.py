import os
os.system("cls")
name_archivo="D:/lenguajes_programacion/python/learn_python/5/Lineas.txt"
'''
r : lee
w : sobreescribe o crea
a : append
x : crea
b : binario
t : texto
+ : lectura y escritura
-----------
with open(file, 'modo') as archivo:
    ...

-----------
** r **
# archivo es un iterable de todas de las lineas del file
.read(x) x opcional siendo x cantidad de texto leido, al ser usado
         de nuevo este lee desde donde se quedo.

.seek(x) x es la nueva posicion desde donde comenzara a leer

.readlines() es una lista con todas las lineas
-----------
** w **
.write(x) borra todo y escribe x o crea un archivo que contiene x

.writelines(x) x es un iterable y escribe todo lo que hay ahi
-----------
** a **
.write(x) añade x al final del archivo

.writelines(x) x es un iterable y escribe todo lo que hay ahi
'''
with open(name_archivo,"r", encoding="utf-8") as archivo:
    contenido=archivo.readlines()
    print(contenido)

with open(name_archivo,"w+", buffering=8192) as archivo:
    archivo.write("hola 1")
    lista=[f"\nhola {x}" for x in range(2,4)]
    archivo.writelines(lista)

    archivo.seek(0)
    contenido=archivo.readlines()
    print(contenido)

with open(name_archivo,"a+", encoding="utf-8") as archivo:
    lista2=[f"\nadios {x}" for x in range(1,4)]
    archivo.writelines(lista2)

    archivo.seek(0)
    contenido=archivo.readlines()
    print(contenido)



with open(name_archivo,"w") as archivo:
    archivo.writelines(("linea1","\nlinea2","\nlinea3"))