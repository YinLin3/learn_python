from collections import namedtuple

# opcion 1
namedtuple_1=namedtuple("Campos",["id_","name","edad"])(1,"mario",20)
# opcion 2
namedtuple_2=namedtuple("Estudios",["C1","C2","C3"])
a=namedtuple_2("Aleman","Python","Git")

# trabajaremos con el siguiente namedtuple
namedtuple_3=namedtuple("Practiquemos",["A1","B2","C3"])

# .fields | muestra en una tupla los campos definidos | O(1)
print("los campos definidos son los siguientes",namedtuple_3._fields)

# ._make(...) | util cuando los datos los tenemos en una lista, tuple, etc | O(n)
lista_cursos=["curso1","curso2","curso3"]
estudiar=namedtuple_3._make(lista_cursos)
print("\nnuestro namedtple es",estudiar)

# ._asdict() | convierte el namedtuple en un dict | O(n)
dicc=estudiar._asdict()
print("\nhemos transformado el namedtuple en un dict",dicc)

# ._replace() | crea otro namedtuple modificado independiente del anterior (excepto si el namedtuple contiene un mutable al modificarlo tmbn se vera afectado el creado) | O(n)
estudiar2=estudiar._replace(A1="curso0")
print("\nhemos creado otro namedtuple modifciado",estudiar2,estudiar)

# _field_defaults | crea valores predeterminados | O(1)
namedtuple_4=namedtuple("Persona",["nombre","edad"],defaults=["no se sabe","???"])
persona1=namedtuple_4("mario","20")
print("\nhemos creado un namedtuple predeterminado y lo hemos modificado",persona1)