# calculator in Python (v0.3)
from cmath import sqrt

def add(num1, num2):
    return num1+num2
def sub(num1, num2):
    return num1-num2
def mul(num1, num2):
    return num1*num2
def div(num1, num2):
    return num1/num2
def Sqroot(num1):
    return sqrt(num1)

# main

print(add(5, 3))
print(sub(5, 3))
print(mul(5, 3))
print(div(5, 3))
print(Sqroot(5))