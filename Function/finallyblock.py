'''
finally block must get executed 
even if a function has a return statement finlly block gets executed 
'''
def div(a,b):
    try:
        return a/b
    except:
        print("not possible")
    finally:
        print("Yahooo!!")
        return 99
        

x = div(a=55,b=5)
print(x)
print(div(10,0))
