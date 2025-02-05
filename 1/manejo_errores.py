dia_año={**dict.fromkeys([1,3,5,7,9,11],31), **dict.fromkeys([4,6,8,10,12],30)}
año_actual,mes_actual,dia_actual=2025,1,31
print("dinos su fecha de nacimiento:")

try:
    año=int(input("escriba su año de nacimiento.. "))
    mes=int(input("escriba su mes de nacimiento.. "))
    dia=int(input("escriba su dia de nacimiento.. "))
except ValueError:
    print("bro la fecha en numero, porque escribiste otra cosa .-.")
    exit()
except Exception as e:
    print(e)

if año>año_actual or año<=(año_actual-120):
    raise ValueError(f"El año está fuera del rango permitido. Debe estar entre {año_actual-120} y {año_actual}.")

if mes not in range(1,13):
    raise ValueError(f"El mes está fuera del rango permitido. Debe estar entre 1 y 12.")

año_bisiesto = lambda x: ((x % 4 == 0 and x % 100 != 0) or x % 400 == 0)
if año_bisiesto(año):
    dia_año[2:29]
else:
    dia_año[2:28]

if dia<1 or dia>dia_año[mes]:
    raise ValueError(f"El dia está fuera del rango permitido. Debe estar entre 1 y {dia_año[mes]}.")

if año==año_actual and mes==mes_actual and dia==dia_actual:
    print("wow bro, eres nuevesito tienes 0km")
elif mes==mes_actual and dia==dia_actual:
    print("feliz cumple bro")
elif año==año_actual and (mes>=mes_actual or dia>dia_actual):
    raise ValueError("La fecha introducida es del futuro")
else:
    print(f"asi que naciste el {dia}-{mes}-{año}")