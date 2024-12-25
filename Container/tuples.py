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