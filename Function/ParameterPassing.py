#python Uses Pass by assignment
#immutable variable do not change in other function
def fun(x):
    print("x in fun",x)
    x = 10
#can use golbal x cannot change it
def fun2(y):
    y  = x + 10
    print("y using global x in fun2",y)
def containerFun(num):
    num+=[2,3,4]
    for i in range(3):
        num.append(i)

def containerFun2(num):
    """
    num before referencing = number
    but afte num =[1,2,3] 
    num now referncing [1,2,3]
    num is local now
    """
    num = [1,2,3]
    return num
x = 100
print("x before",x)
fun(x)
print("x After fun",x)
fun2(10)
    

number = [10,20,30]
print(number)
containerFun(number)
print(number)

containerFun2(number)#this does not change the number list
print(number)
