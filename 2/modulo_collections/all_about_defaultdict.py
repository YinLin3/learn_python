from collections import defaultdict

# defauldict(...) | se puede poner funciones callables que asignaran un valor predeterminado y otras en las que podremos asignarle | O(1)
defaultdict_1=defaultdict(lambda: "hola " )
defaultdict_1["juan"]+="juan"
print("\nveamos el defaultdict",defaultdict_1)

# .defaultfactory | cambia la funcion callable del defaultdict
defaultdict_1.default_factory=list
defaultdict_1["numeros"]+=1,2,3
print("\nveamos como se modifico",defaultdict_1)

# Defaultdict al funcionar como un dict hereda algunas de sus funciones:
'''
clear()
copy()
fromkeys(...)
get(...)
items()
keys()
values()
pop(...)
popitem()
setdefault(...)
update(...)
'''