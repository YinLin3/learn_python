from math import *
import my_modules as mm
mm.clean()
# 1
# sqrt(...) | devuelve un float de la raiz cuadrada de un numero | O(1)
print("la raiz cuadrada de 170 es", sqrt(170))

# exp(...) | devuelve float de la potencia del numero euler | O(1)
print(f"\nel numero euler al cuadrado es {exp(2):.4f}")

# log(...) | devuelve float del logaritmo en base indicada, por defecto e | O(1)
print(f"\nlogaritmo en base 5 de 9 es {log(9,5):.4f}")

# log2(...) y log10(...) | devuelve float del logaritmo en base 2 o 10 (mejor optimizado que log(...)) | O(1)
print(f"\nlogaritmo en base 2 de 60 es {log2(60):.4f}")

# factorial(...) | devuelve int del factorial del numero indicado | O(n)
print("\nel factorial de 11 es",factorial(29))


#2
# round(...) | devuelve int del redondeo, en caso ser .5 utiliza redondeo hacia la par | O(1)
print("\n\nredondiemos 8.5 y 7.3\t",round(8.5),"y",round(7.3))

# ceil(...) | devuelve int del redondeo por exceso (hacia el mayor) | O(1)
print("\nceil round de 5.2 es",ceil(5.2))

# floor(...) | devuelve int del redondeo por defecto (hacia el menor) | O(1)
print("\nfloor round de -3.2 es",floor(-3.2))

# trunc(...) | devuelve int del float o visto de otra forma (redondea a cero) | O(1)
print("\ntruncamiento hacia 0 de 14.9 es",trunc(14.9))

# fmod(...) | devuelve el residuo de la divison con mayor presicion | O(1)
print("\nel resto de la division -978/45 es",fmod(-978,45))

# isclose(...) | devuelve bool si los numero son cercanos (rel_tol=, maxima diferencia es el porcentaje del numero y abs_tol=, maxima diferencia la que indiquemos) | O(1)
print("\n800 y 880 son cercanos con respecto al 10% de 800?",isclose(800,880,rel_tol=10))