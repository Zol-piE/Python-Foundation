info = {
    "tomal" : "1234",
    "tohidul" : "dhaka123"
}
def add(a,b):
    print(a+b)


def authentication(fun):
    def wrap(username,password,*args,**kwargs):
        if username in info and info[username] == password:
            fun(*args,**kwargs)
        else:
            print("Not found")
    return wrap
@authentication
def mul(a,b):
    print(a*b)
obj1 = authentication(add);
obj1("tomal","123",1,2)
mul("tohidul","dhaka123",5,8)