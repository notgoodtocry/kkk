import math

n1=int(input("enter first number"))
n2=int(input("enter seconde number"))

op=input()

if op=="+":
    result=n1 + n2

if op=="-":
    result=n1 - n2

if op=="*":
    result=n1 * n2

if op=="/":
    if n2 !=0:
        result=n1 / n2
    else:
        result="cannot device by zero"


if op=="%":
    result=n1 % n2

if op=="^":
    result== n1 ^ n2


print(result)


