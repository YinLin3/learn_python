import my_modules
import sys
my_modules.clean()

# sys.path | es un list, muestra donde python busca los modulos | O(1)
print(sys.path)

# sys.modules | es un dict, muestara todos los modulos importados | O(1)
print("esta el modulo sys importado?", "sys" in sys.modules,"\n")

# sys.version | muestra la version de python y otras cosas | O(1)
print(sys.version,"||",sys.version_info)

# sys.platform | muestra el sistema operativo actual | O(1)
print("\nel sistema opetarivo actual es:",sys.platform)

# sys.getsizeog(...) | muestra los bytes de una variable, funciones, etc. | O(1)
x = "hola mundo"
print("\nla variable consume",sys.getsizeof(x),"bytes")

# sys.getrecursionlimit() | muestra el limite de recursion actual | O(1)
print("\nel maximo de recursion es",sys.getrecursionlimit())

# sys.setrecursionlimit(...) | modifica el limite de recursiones | O(1)
modificar=300
sys.setrecursionlimit(modificar)
print("\nel limite de recursiones fue modificado a",modificar)

# sys.getrefcount(...) | devuelve el numero de referencias, algunos estan cacheados y vota un numero grande | O(1)
print("\nde 'hola :D' es",sys.getrefcount("hola :3"),"y de 100 es",sys.getrefcount(100),"\n")

# sys._getframe(...) | devuelve el frame 0 por defecto | O(1)
print(sys._getframe(0))

# sys.exc_info() | devuelve una tupla con 3 elementos sobre la ifnroamcion de la ultima excepcion capturada | O(1)
try:
    sys._getframe(1)
except:
    tipo, valor, traza=sys.exc_info()
finally:
    print("\ntipo:",tipo,"||\tvalor:", valor,"||\ttraza:", traza)

# sys.byteorder | devuelve si el sistema usa LSB o MSB | O(1)
print("\norden de bytes del sistema",sys.byteorder)

# sys.maxsize | representa el índice máximo en estructuras de datos | O(1)
print("\nel maximo es",sys.maxsize)

# sys.implementation | nos dice la implementacion que estamos usando | O(1)
print("\nimplementacion de python:",sys.implementation)

# sys.exit(...) | sale del programa y al escribir un string lo imrpime y sale | O(1)
sys.exit("\nhemos terminado :D")