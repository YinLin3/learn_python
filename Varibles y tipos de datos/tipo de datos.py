enteros="int"
decimales="float"
complejos="complex"
texto="str"
booleanos="bool"
secuencia=["list","tuple","range"]
conjunto=["set","frozenset"]
mapeo="dict"
print(f"{enteros} = 1")
print(f"{decimales} = 1.4")
print(f"{complejos} = 1+4j")
print(f"{texto} = texto1")
print(f"{booleanos} = True or False")

print(f"{secuencia[0]} = [1,\"texto\",2]")
print(f"{secuencia[1]} = (1,7,\"texto2\")")
print(f"{secuencia[2]} = range(1,101,2)")

a={1,7,5,"texto"}
print(f"{conjunto[0]} = {a}")
a=frozenset({1,7,5,"texto"})
print(f"{conjunto[1]} = {a}")
a={"a":1,"b":2,3:"c"}
print(f"{mapeo} = {a}")