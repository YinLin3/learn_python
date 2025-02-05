tupla=(1,2,3)
try:
    tupla[0]=2
except:
    print("Las tuplas son inmutables, no pueden ser modificadas")

pueblo={
(1,1):"Plaza Central          ",
(1,2):"Centro de Innovacion   ",
(1,3):"Biblioteca Nacional    ",
(2,1):"Parque de la Ciencia   ",
(2,2):"Distrito Financiero    ",
(2,3):"Estadio Olimpico       ",
(3,1):"Zona Verde EcoParque   ",
(3,2):"Plaza de los Sabios    ",
(3,3):"Distrito de Arte Urbano",
(4,1):"Centro de Transporte   ",
(4,2):"Hospital Central       ",
(4,3):"Puerto de Comercio     ",
}
lista_coord="(1, 1)                     (1, 2)                     (1, 3)\n(2, 1)                     (2, 2)                     (2, 3)\n(3, 1)                     (3, 2)                     (3, 3)\n(4, 1)                     (4, 2)                     (4, 3)"
print(lista_coord)
a=input("Escriba la coordenada que quiere que sea revelada.. ")
a=eval(a)
if a not in pueblo:
    print("esta escribiendo una coordenada inexistente, pruebe con una de las anteriores mencionadas")
    exit()
ubicacion=lista_coord.index(str(a))
b=lista_coord.replace(str(a)+" "*17,pueblo[a])
print(b)