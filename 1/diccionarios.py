#dict: diccionario es un conjunto de elementos asociados a una clave que especificamos
a={"nombre":"Mario",
   "edad":54,
   "altura":1.82,
   "sexo":"Masculino"
   }
#a es un dict
print(a)
# añadir elementos a un dict
a["peso"]="70 kg"
print("\nVemos que hemos añadido peso:70kg a nuestro dict:")
print(a)

# eliminar elementos de un dict (sabiendo clave)
valor_eliminado=a.pop("edad")
print("\nhemos eliminado el elemento de clave edad")
print(valor_eliminado)

# modificar elementos
a["nombre"]="Mario2"
print("\nVemos que hemos modificado nombre a nuestro dict:")
print(a)

# eliminar elemento
del a["altura"]
print("\nVemos que hemos eliminado altura de nuestro dict:")
print(a)

# unir diccionarios
b={"color_favorito":"azul",
   "fecha_cumpleaños":"12-09-1941"
}
a.update(b)
print("\nhemos añadiendo un dict a otro:")
print(a)

# copiar dict
c=a.copy()
print("\nhemos copaido un dict")
print(c)

#clave, elementos y pares de un dict
print("\nvemos las claves, los elementos y el par de ellos:")
print(a.keys())
print(a.values())
print(a.items())