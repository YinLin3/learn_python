import os
from math import *
def clean():
    os.system("cls")

def primo(num:int)->bool:
    if num%2==0 or num==1:
        return False
    for x in range(3,ceil(sqrt(num))+1,2):
        if num%x==0:
            return False
    return True