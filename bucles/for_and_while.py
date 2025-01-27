a=[y for y in range(1,11,2)]
for x in a:
    print(f"{x} its odd")
print("all this numbers are odd")

while a:
    print(f"{a[0]} its odd")
    del a[0]
print("all this numbers are odd")