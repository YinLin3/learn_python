def area_circulo(radio):
    return f"el area es: {radio*radio*3.14}"
print(area_circulo(1))

def suma(a,b):
    print(a+b)
suma(7,8)
def maximo(lista):
    return max(lista)
print(maximo([1,2,4,87,9,2,74,8,6,5]))
a=5
def multiplo(numero):
    if numero%5==0:
        print("es multiplo")
    else:
        print("no es multiplo")
multiplo(11)

funcion= lambda numero1,numero2: numero1*numero2
print(funcion(4,5))