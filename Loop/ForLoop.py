number  = list(range(1,20))

print(number)

for i in range(len(number)):
    print("index",i," ",number[i])

for x in number:
    if not x%2:
        continue
    print(x,end=" ")

print()

even = range(0,11,2)
odd = range(1,11,2)

for x,y in zip(even,odd):
    print("Even :",x,"|","Odd :",y)

num = [10,20,30,40,50]

for x,y in enumerate(num):
    print(x,y)

dic = { "tomal" :17,"tonu":8,"sohan":4}

for x,y in dic.items():
    print(x,y)

for i in range(5):
    for j in range(i,5):
        print(j,end=" ")
    print()

num = [[1,2,3,4,],[5,6,7],[8,9,10]]
for i in num:
    for j in i:
        print(j,end=" ")
    print()