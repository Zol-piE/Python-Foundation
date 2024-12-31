"""
range(stop)
range(start,stop)
range(start,step,stop)

only Works for int
step cannot be Zero

"""
number = list(range(5,9))
print(number)
number = tuple(range(1,6))
print(number)
i =0

while (i in range(5)):
    print(i)
    i=i+2

#accessing Index With Range()
ele = range(5)[-2]
print(ele)
ele = range(10,30,5)[2] #10 15 20 25
print(ele)

#negative step in Range
number = list(range(10,5,-1))
print(number)
number = list(range(0,-5,-1))
print(number)
