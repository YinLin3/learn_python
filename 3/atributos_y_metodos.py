# atributos de clase | al modificarlo se modifican todas las instancias
class clase:
    atributo_clase="Esto es un atributo de clase"
ejemplo=clase()
ejemplo2=clase()
print(ejemplo.atributo_clase,ejemplo2.atributo_clase,"\n")

clase.atributo_clase="Cambie para todos"
print(ejemplo.atributo_clase,ejemplo2.atributo_clase,"\n")

# atributos de instancia | al modificalo se modifica solo el de esa instancia
class clase2:
    def __init__(self,valor):
        self.atributo_instancia=valor
ejemplo3=clase2("esto es un atributo instancia")
ejemplo4=clase2("esto es otro atributo instancia")

ejemplo4.atributo_instancia="sigo siendo un atributo instancia solo cambie de valor"
print(ejemplo3.atributo_instancia,ejemplo4.atributo_instancia)

class clase3:
    def __init__(self,valor1,valor2):
        self.valor1=valor1
        self.valor2=valor2
    def sumar(self):
        return self.valor1+self.valor2
ejemplo5=clase3(10,20)
print(ejemplo5.sumar())