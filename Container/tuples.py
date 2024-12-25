#Tuples are "Read-Only" -> after creation can not add,remove,change elements
num = (1,2,3,4,5)
for i in range(len(num)):
    print(num[i],end=" ")
print()
try:
    num[i] =10
except TypeError:
    print("Item Change is not Possible")