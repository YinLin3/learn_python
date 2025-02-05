from collections import Counter
counter_1=Counter(["id_0","id_1","id_1"])

# .update(...) | agrega los elementos de un iterable al counter | O(n) o O(k)
dicc={"id_0":2,"id_3":4}
counter_1.update(["id_2","id_0","id_3"])
counter_1.update(dicc)
print("Agregamos elementos ahora el counter se ve asi",counter_1)

# .elements() | devuelve una lista extendida de los elementos | O(n)
print("\nveamos la lista de todos los elementos",list(counter_1.elements()))

# .mostcommon(...) | devuelve la cantidad de elementos que indiques en orden, en caso no indiques devuelve todos | O(k log k)
print("\nveamos los 3 elementos que mas aparecen",counter_1.most_common(3))

# .substract(...) | resta a los elementos que tengamos, en caso no este lo pone en nagativo | O(n) o O(k)
dicc2={"id_0":4,"id_4":2,"id_2":2}
counter_1.subtract(["id_1","id_3"])
counter_1.subtract(dicc2)
print("\nveamos como queda el counter luego de la modificacion",counter_1)

# .total() | devuelve la suma de la frecuencia de los elementos | O(k)
print("\nla suma de todas las frecuencias es",counter_1.total())

# .copy() | copia el counter que es independiente (excepto si el counter contiene un mutable al modificarlo tmbn se vera afectado el copiado) | O(k)
counter_copiado=counter_1.copy()
print("\nel counter copiado es",counter_copiado)

# .clear() | elimina todo el contenido del counter | O(1)
counter_1.clear()
print("\naqui terminan los metodos de counter",counter_1)

# Counter al funcionar como un dict hereda algunas de sus funciones:
'''
keys()
values()
items()
get(...)
update(...)
pop(...)
popitem()
setdefault(...)
copy()
clear()
'''