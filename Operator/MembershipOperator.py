#in -- not in
#string ->substring , list ->elem,dictonary ->key
import operator
num = [10,20,30]
print(10 in num)
print(22 not in num)
str = "tomal"
ptr = "mal"
print(ptr in str)
print('i' in str)
person = {"tomal":17,"sohan":4,"alamin":5}
str =  "tomal"
if str in person:
    print(str,"is present")
else:
    print(str,"is not present")

number = [10,20,30,40,50,60]
print(operator.contains(number,30))
print(operator.contains(number,55))