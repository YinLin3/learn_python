#tuplas: son un conjunto de elementos ordenados mediante indices y son inmutables
a=2,1,4,5
b=(4,7,2,9)
c=0,
#a, b y c son tuplas
'''
al ser inmutables
no se pueden modificar los elementos existentes ni su indice, solo añadir nuevos al final
'''
print("\nunir tuplas:")
print(a+c*3+b)

print("\nveamos el error que genera intentar cambiar un elemento:")
a[0]=5