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