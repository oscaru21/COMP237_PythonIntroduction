#Loops
#for loops in python need to have an iterable data structure like a list or an array

from ast import If
from asyncio import _enter_task
from tkinter.tix import InputOnly


def my_loop():
    a = list(range(5))
    for num in a:
        print(num)
    
my_loop()

def factorial(num):
    result = 1
    for el in range(num, 0, -1):
        result = result * el
    print(result)

factorial(4)


