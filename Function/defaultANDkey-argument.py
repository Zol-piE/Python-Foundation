def fun(role,name="NA",roll="NA"):
    print(role,name,roll)

def fun2(name,id,role):
    print(name,id,role)

#Variable Length Argument *args and **keyargs
"""
*args ->store multiple item in a tuple 

"""
def sum(*args):
    print(args)
    res =0
    for i in args:
        res+=i
    return res
"""
**keyargs-> store "key,value" pair 
            store in a dictonary
"""
def price(**keyargs):
    print(keyargs)
    for x,y in keyargs.items():
        print(f"{x} : {y}")

def fun2(name,roll,*args,**keyargs):
    print("Name",name)
    print("Roll",roll)
    print("Print Tuple")
    for i in args:
        print(i,end=" ")
    print()
    for key,val in keyargs.items():
        print(f"{key} : {val}")

#main Function
fun("student") #default fun
fun("tomal",17,"student") #positional argument
fun(name="Tomal",role="Teacher",roll=9) #keyword argument

print(sum(10,20,30,40))
a,b,c =1,2,3
price(a= "lebu",b = "kola",c = "pepe")
fun2("Tomal",17,10,20,30,40,Math=100,CSE=75,HSS=89)
num = [1,2,3,4,5]
print(sum(*num)) #unpacking list

id = {"name":"tomal","Roll":17,"subject":"Cse"}
price(**id)
