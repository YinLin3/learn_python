from collections import deque
deque_1=deque([3,4])

# .append(...) | agrega un elemento al final | O(1)
deque_1.append(5)
print("hemos añadido el numero 5",deque_1)

# .appendleft(...) | agrega un elemento al inicio | O(1)
deque_1.appendleft(2)
print("\nhemos añadido el numero 2", deque_1)

# .pop() | elimina el ultimo elemento | O(1)
eliminado=deque_1.pop()
print("\nhemos eleminado el numero",eliminado,deque_1)

# .popleft() | elimina el primer elemento | O(1)
eliminado2=deque_1.popleft()
print("\nhemos eleminado el numero",eliminado2,deque_1)

# .extend(...) | agrega los elementos del iterable al final | O(k)
deque_1.extend([5,6,7])
print("\nhemos añadido varios elementos",deque_1)

# .extendleft(...) | agrega los elementos del iterable al inicio | O(k)
deque_1.extendleft([2,1,0])
print("\nhemos añadido varios elementos",deque_1)

# .insert(...) | inserta un elemento el indice indicado | O(n)
deque_1.insert(3,7)
print("\nhemos añadido el elemento 7 en el indice 3",deque_1)

# .remove(...) | remueve la primera aparicion de un elemento | O(n)
deque_1.remove(7)
print("\nhemos eliminado la primera aparicion del 7",deque_1)

# .rotate(...) | mueve los elementos x pasos a la derecha (+) o a la izquierda (-) | O(k)
deque_1.rotate(-2)
print("\nwow los elementos han cambiado de posicion",deque_1)

# .count(...) | cuenta la cantidad de veces que aparece un elemento | O(n)
contar=deque_1.count(0)
print("\nlas veces que aparece el 0 es/son",contar)

# .index(...) | busca en elemento dentro de un rango indicado en caso no poder se busca en todo el deque, en caso no exiate el valor devuelve ValueError | O(n)
buscar=deque_1.index(6,2,-1)
print("\nel numero 7 se encuentra en el indice",buscar)

# .__getitem__(...) | devuelve el elemento que este en el indice indicado | O(n)
print("\nel elemento que estan en el indice 3 es el",deque_1[3])

# .__setitem(...) | cambia el elemento actual por otro | O(n)
deque_1[1]=8
print("\n el elemento en el indice 1 ahora es el",deque_1[1])

# .__delitem__(...) | elimina el elemento que este en el indice indicado | O(n)
del deque_1[3]
print("\nluego de eliminar un elemento la lista es",deque_1)

# maxlen | le pone un limite de elementos a la lista, en caso agregres de mas se eliminaran otros | O(1)
deque_max= deque(deque_1,maxlen=4)
print("\nmi deque con max es",deque_max)

# .reverse() | invierte el orden del deque | O(n)
deque_1.reverse()
print("\nmi deque invertido es",deque_1)

# .__contains__(...) | busca si un elemento esta en el deque | O(n)
print("\nesta el numero 10 en mi deque?",deque_1.__contains__(10))

# .copy() | copia el deque que es independiente (excepto si el deque contiene un mutable al modificarlo tmbn se vera afectado el copiado) | O(n)
deque_copiado=deque_1.copy()
print("\nel deque copiado es",deque_copiado)

# .clear() | elimina todo el contenido del deque | O(1)
deque_1.clear()
print("\naqui terminan los metodos de deque",deque_1)