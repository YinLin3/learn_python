a={1,2,3,4,5,6,7,8,9}
b={3,7,8,15,18,20}
c={2,4,6,8}
# Unión: A | B o A.union(B)
union=a|b
print("lo unimos",union)

# Intersección: A & B o A.intersection(B)
intersectar=a&b
print("\nlo intersectamos",intersectar)

# Diferencia: A - B o A.difference(B)
diferencia=a-b
print("\nla diferencia",diferencia)

# Diferencia simétrica: A ^ B o A.symmetric_difference(B)
diferencia_simetrica=a^b
print("\nla diferencia simetrica",diferencia_simetrica)

# Subconjunto: A <= B o A.issubset(B)
subconjunto=c<=a
print("\nc esta incliudo en a?",subconjunto)

# Superconjunto: A >= B o A.issuperset(B)
superconjunto=b>=c
print("\nb incluye a c?",superconjunto)

# Disjuntos: A.isdisjoint(B)
disjuntos=a.isdisjoint(b)
print("\na y b tienen 0 elementos en comun?",disjuntos)

# Eliminar elemento: A.remove(x) o A.discard(x)
a.remove(1)      # genera error si el elemento no existe
a.discard(100)   # No genera error si el elemento no existe
print("\nveamos como se ve \"a\" luego de la eliminacion",a)

# Agregar elemento: A.add(x)
a.add(10)
print("\nveamos como se ve luego de agregar 10",a)

# Longitud del conjunto: len(A)
lenght=len(a)
print("\nla cantidad de elementos de \"a\" es", lenght)

# Eliminar y devolver un elemento aleatorio: A.pop()
eliminado=a.pop()
print("\nse elimino el siguiente dijito",eliminado,a)