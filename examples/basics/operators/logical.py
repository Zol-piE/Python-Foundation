# and or not
x = 10 
y =20
#any number expect zero is assume as true
print(x or y)  # works as circuit -- find x true prints x
print(x and y) # both x and y are checked ..last y is checked thats why y is printed
x = int(input())
y = int(input())
if(x>0 and y>0):
    print("both are positive")
elif(x>0):
    print("x is positive")
else:
    print("both Negative")

if not (x%2):
    print(x," is even")
elif x%2:
    print(x," is Odd")

y = False
if(y or "tomal"):
    print("is Awsome")