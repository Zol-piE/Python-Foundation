var = "GLOBAL"
gNum = 10
def inner():
    #here var is local to inner ..we can assign new obj to var..can not change
    var = "local"
    print("Var inside inner function is ",var)
    #cannot go gNum +=10
    gNum =100
    print(gNum)
    def inner_inner():
        var = "var inside inner inner"
        print("Inner inner")
        print(var)
    inner_inner()


print("Main function")
inner()
print("Var outside inner function is ",var)
