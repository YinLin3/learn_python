import os
import time
os.system("cls")

# os.getcwd() | devuelve el directorio de trabajo (desde donde se ejecuta python) | O(1)
lugar=os.getcwd()
print("se esta ejecutando desde",lugar)

# os.chdir(...) | cambia el directorio de trabajo | O(1)
nuevo_lugar="D:/lenguajes_programacion/python/learn_python/4"
os.chdir(nuevo_lugar)
print("\nahora se ejecuta desde",os.getcwd())

# os.listdir(...) | devuelve una lista de archivos dentro de la carpeta, en caso no pongamos nd devuelve el del directorio actual | O(n)
print("\nveamos los archivos de la carpeta actual",os.listdir())

# os.mkdir...() | crea una carpeta en la ruta indicada, en caso no pongamos la ruta lo crea en el directorio actual,en caso ya exista devuelve FileExistsError | O(1)
crear="D:/lenguajes_programacion/python/learn_python/5"
try: os.mkdir(crear)
except FileExistsError: print("\nla carpeta ya existe")

# os.makedirs(...) | crea cada carpeta de la direccion en caso no exista y si todas existen genera error FileExistsError que se puede controlar con "exist_ok=True" | O(n)
crear2="D:/lenguajes_programacion/python/learn_python/5"
os.makedirs(crear2,exist_ok=True)
print("\nVemos que no vota error por mas que todas las carpetas ya esten creadas")

# os.rmdir(...) | elimina una carpeta solo si esta vacia, en caso contrario vota OSError | O(1)
try: os.rmdir(crear2)
except OSError: print("\nLa carpeta tiene elementos, no ha sido eliminada")

# os.remove(...) | elimina el archivo indicado, en caso no exista genera FileNotFoundError | O(1)
eliminar="D:/lenguajes_programacion/python/learn_python/5/hola.txt"
try: os.remove(eliminar)
except FileNotFoundError: print("\nel archivo no existe")

# os.rename(...) | cambia el nombre del carvibo o carpeta por otro, no exista genera FileNotFoundError y en caso el segunda exista genera FileExistsErro | O(1)
cambiar="D:/lenguajes_programacion/python/learn_python/5/texto1.txt"
cambiar_por="D:/lenguajes_programacion/python/learn_python/5/2/texto2.txt"
try: os.rename(cambiar, cambiar_por)
except FileNotFoundError: print("\nel archivo no existe o ya fue cambiado")
except FileExistsError: print("\nel segundo archivo existe")

# os.replace(...) | cambia el nombre del archivo o carpeta por otro, no exista genera FileNotFoundError y en caso el segunda exista lo sobreescribe | O(1)
cambiar="D:/lenguajes_programacion/python/learn_python/5/texto1.txt"
cambiar_por="D:/lenguajes_programacion/python/learn_python/5/2/texto2.txt"
try: os.replace(cambiar, cambiar_por)
except FileNotFoundError: print("\nel archivo no existe o ya fue cambiado")

# os.stat(...) | nos da la informacion sobre un archivo o carpeta | O(1)
ver="D:\lenguajes_programacion\python\learn_python"
estado=os.stat(ver)
print("\nveremos: tamaño,  ultima modificacion,  ultima vez que se accedio,  fecha de creacion")
print("veamos la info de la carpeta learn_python","||",estado.st_size,"||",time.ctime(estado.st_mtime),"||",time.ctime(estado.st_atime),"||",time.ctime(estado.st_ctime),"\n")

# os.scandir(...) | itera sobre todo el contenido de la carpeta | O(n)
carpeta="D:/lenguajes_programacion/python/learn_python/2"
for x in os.scandir(carpeta):
    print(f"mi nombre es\t{x.name}\ty soy un{' archivo' if x.is_file() else 'a carpeta'},\tmi direccion es: {x.path}")

# os.walk(...) | itera sobre todo el contenido de la carpeta y de las subcarpetas | O(n)
print("")
veamos="D:/lenguajes_programacion/python/learn_python/2"
quitar="D:/lenguajes_programacion/python/"
for ruta, subcarpetas, archivos in os.walk(veamos):
    print("esta ruta:",ruta.replace(quitar,"..."),"|| tiene estas subcarpetas:",subcarpetas,"|| y estos archivos:",archivos)

# os.path.exists(...) | verifica si un archivo existe | O(1)
verificar="D:/lenguajes_programacion/python/learn_python/4/hola.txt"
print("\nel archivo hola.txt existe?",os.path.exists(verificar))

# os.path.isfile/.isdir/.getsize (...) | devuelve booleano si es archivo o si es carpeta y devuelve el tamaño en bytes | O(1)
archivo_carpeta="D:/lenguajes_programacion/python/learn_python/4/my_modules.py"
print("\ncarpeta?",os.path.isdir(archivo_carpeta),"\tarchivo?",os.path.isfile(archivo_carpeta),"\tque tamaño?",os.path.getsize(archivo_carpeta),"byte")

# os.path.join(...) | une palabras y lo devuelve en ruta de manera segura | O(n)
print("\nhemos creado la ruta:",os.path.join(os.getcwd(),"archivo_inventado\n"))

# os.environ[...] | funciona como un dict, devuelve ruta(s) de la clave indicada en caso no existe devuelve KeyError | O(1)
os.environ["variable_extra"]="fui creada"
lista_environ=["USERPROFILE", "PATH", "TEMP", "APPDATA", "LOCALAPPDATA", "COMSPEC", "NUMBER_OF_PROCESSORS", "PYTHONPATH","variable_extra"]
for elemento in lista_environ:
    print(f"{elemento}: {os.environ.get(elemento, 'No definida')}")

# os.getenv(...) | devuelve ruta(s) de la clave indicada en caso no exista devuelve por defecto None | O(1)
print("\nveamos que solo accede, no puede crear nuevas variables como un dict",os.getenv("TEMP"),"\n")

# os.system(...) | escribe el comando directamente en el cmd | O(1)
os.system("mkdir carpeta_creada_por_system")

# os.getpid() | escribe el pid del proceso actual | O(1)
pid = os.getpid()
print("\nEl ID del proceso actual es:",pid)

# os.urandom(...) | gener ala cantidad indicada de byte randoms | O(n)
random=os.urandom(8)
print("\nbyte random",random)

# os.kill(...) | termina un proceso al ingresra un pid
import signal
os.kill(pid,signal.SIGTERM)
print("yo nunca aparecere :(")