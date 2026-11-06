#List Dynamic Array - Contain Mix Type
#Must Use []

Name = ["tomal","Tonu","Saif"]
Roll = [17,16,2]
Mix = ["tomal",7,"saif",25.67]
print("Print List Name ",Name)
print("print Roll ",Roll)
print("Print Mix ",Mix)

#list With Repeated Values

Name = ["tomal"]*5
print(Name)
arr = [0]*10
print(arr)

#list Using Type Conversion Method
brr = list((1,21,"Tomal",55.55))
print(brr)

#List Access - both positive and negative index
#index- 0,1,2, 3, 4
#index->-5,-4,-3,-2,-1
arr =   [5,9,11,21,7]
print("index 0 ->",arr[0])
print("index -5 ->",arr[-5])
print(arr[-5]==arr[0])

#inserting List

Name = []
Name.append(100)
print(Name)
Name.insert(1,10) #insert(i,elem) insert at i index , element b
Name.insert(0,50)
print(Name)
Name = [10,20,30,40,50]
i = Name.index(30) #index of first occurence
Name.insert(i,25)
print("Insert 25 before 30",Name)

#Extend List using Other List

number = [1,3,5]
even_num = [2,4,6]
number.extend(even_num)
print(number)
number.extend((100,200,300))
print(number)
#Remove Elemnts List

arr = [10,20,30,30,40,50,60]
arr.remove(30)
print(arr)
arr.remove(30)
print(arr)
i = arr.index(20)
arr.pop(i)
print(arr)
del(arr[0])
print(arr)
# index
al = list(('a','b','c','d'))
print(al)
try:
    i = al.index('q')
except ValueError:
    print("Not Found")

#Slice in List " : "
org_list = list((1,2,3,4,5,6,7,8,9))
print(org_list)
n_list = org_list[1:9:2] + org_list[0:9:2]
print(n_list)
#reversing 
n_list = org_list[::-1]
print(n_list)