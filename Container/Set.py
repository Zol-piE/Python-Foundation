#Set - {} - unordered - no duplicate values - unchanable - only add or remove items
number = {2,"tomal",4,"5"}
print(number)
#Adding 
even = {2,4,6,8}
odd = {1,3,5,7}
num = set()
print(num)
num.update(even)
print(num)
num.update(odd)
print(num)
#dictonary VS set
my_item = {} #create dic
print(type(my_item)) 
my_item = set() #create set
print(type(my_item))
#Adding/Union of two sets
even = {2,4,6,8}
odd = {1,3,5,7,9}
number = even | odd
print(number)
#adding and intersection
num = set()
for i in range (5):
    num.add(i)
print(num)
num2 = set()
for i in range(3,7):
    num2.add(i)
print(num2)
print(num & num2)
print(num-num2) 
print(num2-num)
#iterate through set
for elem in num:
    print(elem,end=" ")
print()

#pop() - remove() - discard()
num = {2,5,7,8,1}
l = len(num)
for i in range(l):
    print(num.pop(),end=" ") #removes an arbitary numbers

Name = {"tomal","tonu","ratul"}
print(Name)
Name.remove("tomal") #raise if elem not present
print(Name)
try:
    Name.remove("tomal")
except KeyError:
    print("not Found")
