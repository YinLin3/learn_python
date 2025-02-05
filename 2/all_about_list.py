lista=["c","a","g","d","b"]

# METODOS DE LISTAS
# .append(...) | agrega un elemento al final de la lista
lista.append("e")
print("\nse agrego nuevo elemento",lista)

# .insert(...) | agrega un elemento en el indice indicado en la lista
lista.insert(1,"f")
print("\nse agrego nuevo elemento en el indice 1",lista)

# .remove(...) | elimina un elemento indicado en la lista, en caso no exista indica ValueError
lista.remove("b")
print("\nse elimino el elemento \"b\"",lista)

# .pop(...) | extrae el elemento del indice indicado en la lista, en caso no exista el indice indica IndexError
eliminado=lista.pop()
print("\nse extrajo el siguiente elemento", eliminado,lista)

# .reverse() | invierte el orden de la lista
lista.reverse()
print("\nse invirtio el orden",lista)

# .sort() | ordena la lista alfabeticamente o numericamente, (reverse=True) para orden inverso
lista.sort()
print("\nlista ordenada",lista)
lista.sort(reverse=True)
print("\nlista con orden invertido",lista)

# .extend(...) | itera los elementos y los añade a la lista
lista.extend({"a","e","h","b"})
print("\nse agregaron nuevos elementos a la lista",lista)

# .count(...) | cuenta cuantos de un elemento hay en la lista
cuenta=lista.count("a")
print("\nse conto los \"a\" y hay",cuenta,lista)

# .index() | se busca el indice de un elemento, se pueden poner intervalo de busqueda, en caso no encuentre el elemento genera ValueError
indice1=lista.index("a")
print("\n\"a\" se encuentra en el indice",indice1,lista)
indice2=lista.index("a",-4,)
print("\n\"a\" tambien se encuentra en el indice",indice2,lista)

# .copy() | copia la lista que es independiente (excepto si la lista contiene un mutable al modificarlo tmbn se vera afectado el copiado)
lista_copy=lista.copy()
print("\nse copio la lista",lista_copy)


# .clear() | elimina todos el contenido de la lista
lista.clear()
print("\naqui terminan los metodos de listas",lista)

#LIST COMPREHENSION
# lista=[salida for elemento in rango | condiciones]
lista=[str(x)+"0" for x in range(1,10) if bin(x)[-1]=="1"]
print("\n\nlista creada",lista)
lista2=[int(x+"5") for x in lista if (int(x)+5)<40 or (int(x)+5)>80]
print("\nlista2 creada",lista2)