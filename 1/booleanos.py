#bool: significa booleanos (True or False)
a=int(input("ingresen numero...  "))

b=bin(a)

c=b[-1]=="1"

#c es booleano, True si a es impar o False si a es par
if c:
    print("el numero introducido es impar")
else:
    print("el numero introducido es par")