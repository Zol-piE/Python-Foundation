#Used to compare object -> true -> Same Object with Same location
# Compare Values of id()
#is -- is not

x = 10 
y = x

if x is y:
    print("x and y same")
else:
    print("x and y dif")

# comparing two contaibner with same element
num1 = [10,20,30]
num2 = [10,20,30]
print(num1 is num2)
print(num1 is not num2)
print(num1==num2)

for x,y in zip(num1,num2):
    if(x is y):
        print("same",end=" ")
    else:
        print("but diffrent")