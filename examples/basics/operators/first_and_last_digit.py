import math
def first(num):
    dig = int(math.log10(num))
    print(dig)
    return int(num / pow(10,dig))
def last(num):
    return abs(num%10)

x = -49
print(x%10) # (1-(5*10)) % 10
print(x%-10) #(4*(-10)-9) %10
#Python: Remainder takes the sign of the divisor.
#C++: Remainder takes the sign of the dividend.
x = int(input("enter a Number :"))
print("First digit of",x,"is",first(x))
print("Last Digit of",x,"is",last(x))
