for x in range(1,21,2):
    if x%3!=0:
        print(x)
    else:
        print(f"{x} es multiplo de 3\nfinish")
        break

for x in range(1,21,2):
    if x<=15:
        print(f"{x} cumple")
        continue
    if x<18:
        print(f"{x} is my first number >15\nwe finish")
        break