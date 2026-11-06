#*args accept any number of positional arguments as a tuple
def show(*args):
    print(args)

x = 10
y = 40
show(x,y,"tomal","tuhin")
def iden(name,*args):
    print("Print name ",name)
    print("Print Args",args)

def fun(**kwargs):
    for arg in kwargs:
        print(arg , kwargs[arg])

iden("tomal","tuhin","Shanto","Kudos")
# " **kwargs  " → for keyword arguments (dictionary).

fun(tomal = "10",tonu = "22",ritu = "islam",ratul = "33")

def random(a , b, *args, c = 10, **kwargs):
    print(a)
    print(b)
    print(args)
    print(c)
    print(kwargs)

random(100,200,"tomal","tonu",22,33,tomal=11,tonu=44)