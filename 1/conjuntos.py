#set: conjunto de elementos desordenados, no existen duplicados
a={1,7,2,4,1,8,5,6,4,3,5,7,2,9,4}
b={10,17,48,67,4,7,4,5,9}
# a y b son sets
print(a)
print("como vemos los elementos multiples solo se muestran como 1 solo")

# añadir elemento
a.add(10)
print("\nhemos añadido el elemento 10:")
print(a)

# eliminar elemento (sabiendo elemento)
a.remove(7)         #genera error si el elemento no esta
a.discard(100)      #este no genera error si no esta
print("\nvemos que hemos eliminado el elemento 7")
print(a)

# operaciones entre sets
print("\nunion:")
print(a|b)

print("\ninterseccion:")
print(a&b)

print("\ndiferencia:")
print(a-b)

print("\ndiferencia simetrica:")
print(a^b)