#Tuples are "Read-Only" -> after creation can not add,remove,change elements

num = (1,2,3,4,5)
for i in range(len(num)):
    print(num[i],end=" ")
print()
try:
    num[i] =10
except TypeError:
    print("Item Change is not Possible")

# () is optinal but "," is 

num = 10,20,30
print(type(num))
num = (10) # count  as int
print(type(num))
#adding Two Tuples
even = 2,4,6,8
odd = 3,5,7,9
num = even+odd
print(num)
#Concatenation
t1 = 10,20,30,40
t2 = 11,22,33,44
t1 = t1+t2
print(t1)
t1 = (t1,t2)
print(t1)
n =5
t1 = "GFG"
for i in range(n):
    t1 = (t1,)
    print(t1)