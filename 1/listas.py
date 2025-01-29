#lista: conjunto de datos ordenados mediante indices y es mutable
print("lista:")
a=[4,7,0,4,9,3,5,7,8,8,1,3,4,7,6,8,3,9,7]
print(a)
#a es una lista

# acceder a elementos de una lista
print("\nvalores de indice 2 y -2:")
print(f"{a[2]} y {a[-2]}")

# modificar elementos de una lista
print("\nmodificamos el elemento de indice 9:")
a[9]=0
print(a)

# añadir elementos al final de la lista
print("\nañadimos el valor 10 al final:")
a.append(10)
print(a)

# añadir elementos en un indice establecido
print("\nañadimos el valor 3 en el indice 2:")
a.insert(2,3)
print(a)


# eliminar elemento (sabiendo el elemento)
print("\nremovimos el valor 4 de la lista:")
a.remove(4)
print(a)

# eliminar elemento (sabiendo su indice)
print("\nremovimos el elemento de indice 0 de la lista:")
a.pop(0)
print(a)

# creamos nueva lista
b=[0.1,0.9,0.4,0.1]

# añadimos la lista "b" a la lista "a"
print("\nañadimos valores a la lista:")
a.extend(b)
print(a)

# buscar un elemento
buscar=a.index(0.9)
print(f"\nel elemento {a[buscar]} esta en el indice {buscar}")

# contar elemento
contar=a.count(7)
print(f"\nel elemento 7 aparece {contar} veces")

#invertir orden de la lista actual
a.reverse()
print("\nla lista ahora esta al revez:")
print(a)

#ordenar lista
a.sort()
print("\nhemos ordenado la lista de menor a mayor:")
print(a)

#ordenar lista al revez
a.sort(reverse=True)
print("\nhemos ordenado la lista de mayor a menor:")
print(a)

#final
print("\npara finalizar sacaremos un promedio de toda la lista:")
promedio=sum(a)/len(a)
print(promedio)