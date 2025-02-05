# dit: un diccionario guarda pares clave:valor
dicc={
    "a":1,
    2:"b",
    3:"c",
    "d":4
}

# METODOS DE DICCIONARIOS
# .keys() | muestra las claves del dict
claves=dicc.keys()
print("estas son las claves", claves)

# .values() | muestra los valores del dict
valores=dicc.values()
print("\nestas son los valores", valores)

# .items() | muestra los pares clave:valor del dict
pares=dicc.items()
print("\nestas son las claves", pares)

# .setdefault(...) | muestra el valor de la clave indicada, en caso no exista crea una con el valor indicado
dicc.setdefault("a",8)
print("\nel valor de \"a\" es",dicc["a"])

dicc.setdefault("e",5)
print("\nel valor de \"e\" es",dicc["e"])

# .update(...) | itera lo introducido en pares clave:valor y los agrega
agregar=[[6,"f"],(7,"g")]
dicc.update(agregar)
print("\nel dict actualizado es",dicc)

# .pop(...) y .popitem(...) | elimina el par clave:valor que decidas y devuelve el valor // elimina el ultimo par clave:valor y lo devuelve en forma de tupla
eliminado1=dicc.pop("a")
eliminado_clave,eliminado_valor=dicc.popitem()
print("\nhemos eliminado",eliminado1,"y",eliminado_clave,eliminado_valor)

# .get(...) | busca la clave indicada y devuelve su valor, en caso no este devuelve lo indicado
buscar=dicc.get("a","Oh no!, no esta la letra \"a\"")
print("\nesta \"a\"?",buscar)

# dict.fromkeys() | 
nuevo_dicc=dict.fromkeys(["Nota1","Nota2","Nota3"],10)
print("\nel nuevo dict creado es", nuevo_dicc)

# .copy() | copia el dict que es independiente (excepto si el dict contiene un mutable al modificarlo tmbn se vera afectado el copiado)
dicc_copiado=dicc.copy()
print("\nel dict copiado es",dicc_copiado)

# .clear() | elimina todo el contenido del dict
dicc.clear()
print("\naqui terminan los metodos de dict",dicc)

# DICCIONARIOS DENTRO DE DICCIONARIOS
alumnos={
    "mario":{"_id":"m5ri","edad":24,"aula":104},
    "luis":{"_id":"l4is","edad":27,"aula":108},
    "juan":{"_id":"j3an","edad":23,"aula":106}
}
print("\nel id de cada alumno es")
for x in alumnos:
    print(x,"\t",alumnos[x]["_id"])