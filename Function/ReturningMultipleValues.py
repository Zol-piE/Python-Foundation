"""
by default return multiple elements return as tuple
can return as list , dic, other class
"""
def fun(x,y):
    sum = x+y
    mul = x*y
    min = x-y
    return sum,mul,min
#returrn list

def number(x,y):
    sum = x+y
    mul = x*y
    min = x-y
    return [sum,mul,min]
    

x = int(input())
y = int(input())
print(fun(x,y))
num = number(x,y)
print(num)