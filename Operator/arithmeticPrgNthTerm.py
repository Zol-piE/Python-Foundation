""" 
given first term a,difference d,calculate nth term

"""
def nth(a,d,n):
    return a +(n-1)*d

a = int(input("Enter 1st term :"))
d = int(input("Common Difference :"))
n = int(input("Nth term :"))
print("the nth term - ",nth(a,d,n))
