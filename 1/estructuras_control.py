# tenemos los condicionales if elif else
numero=int(input("ingrese numero..  "))
# si resulta True se ejecuatara el if y pasara a la siguiente parte del codigo
if numero<10:
    print("tiene 1 cifra")

# si resulta False pasa al siguiente que es elif
elif numero<100:
    print("tiene 2 cifras")

# si resulta False pasa al siguiente que es otro elif
elif numero<1000:
    print("tiene 3 cifras")

# si todo lo anterior resulta False se ejecutara el else
else:
    print("wow! tiene varias cifras")

# lo siguiente se ejecutara cuando el codigo haya ejecutado 1 de los 4 anteriores
print("---------------\n")

# tenemos los bucles for and while

# for realiza una accion un numero determinado de veces
lista=[7,6,4,3,1,9,8,2,5]
b=[]

# se ejecutara con todos los elementos de la lista (tmbn llamado iteracion)
for elemento in lista:
    b.insert(0,elemento)
print(f"{b}\n")

# while realiza una accion mientras se cumplan las condiciones
lista2=['h', 'o', 'l', 'a']
c=""
# se ejecutara mientras lista2 tenga elementos
while lista2:
    c+=lista2[0]
    del lista2[0]
print(c)
print("---------------\n")

# tenemos los controles de flujo break, continue, pass
'''
break: rompe el bucle y pasa a la siguiente parte del codigo
continue: para el bucle con el elemento actual y pasa a ejecutar el bucle con el siguiente elemento
pass: se usa como marcador de posicion, una parte donde no quieres que sucede algo o simplemento aun no sabes que poner y deseas evitar el error
'''

# break
lista3=[1,2,3,4,5,6,7,8,9,0]
numero2=int(input("ingrese un numero 0-9.. "))
for elemento in lista3:
    if elemento!=numero2:
        print("no es ", end="")
    else:
        print(f"\nyeah! encontramos tu numero")
        break

# continue
numero3=int(input("ingrese un numero 2-9.. "))
while numero3<100:
    if bin(numero3)[-1]=="1":
        numero3*=numero3
        continue
    else:
        print("ganaste!")
        break
print(numero3)