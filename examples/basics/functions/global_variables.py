#Global varible -> defined outside of the function can access any where
#using global keyword
var = 100
num = 66

def print_var():
    print("Print Global Variable in function",var)

print("Normal Var",var)
print_var()
def change_var():
    global var,num
    num = num + 10
    var = 55
    print("Print Var in Change Var fuction",var)
    print("Print Var in Change Num fuction",num)

change_var()
print(var)
print(num)
#Local variable have Same name as Global

def Collision():
    var = globals()['var'] + 100
    globals()['var']=500
    print("Inside Collision Fuction",var)

Collision()
print("Var after Collision Function")
print(var)
