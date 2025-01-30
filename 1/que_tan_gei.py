letras={
    "a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"ñ":15,"o":16,"p":17,"q":18,"r":19,"s":20,"t":21,"u":22,"v":23,"w":24,"x":25,"y":26,"z":27,
    }

def gei(nombre,mas_gei="adrian",maximo=971):
    numero1=[letras[numeroa] for numeroa in list(nombre.strip().lower())]
    numero2=[letras[numerob] for numerob in list(mas_gei.strip().lower())]

    a=min(numero1,numero2,key=len)
    b=max(numero1,numero2,key=len)
    b=b[len(a):]

    diferencia=0

    for valor in range(0,len(a)):
        diferencia+=abs(numero1[valor]-numero2[valor])

    diferencia+=sum(b)
    porcentaje=100*(1-diferencia/maximo)

    return f"eres {porcentaje:.3f}% gei"
print(gei("luis"))