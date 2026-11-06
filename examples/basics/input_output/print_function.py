print(10,20,30)
#sep -> what to print between object
#end what should be print after the print fun
print(10,20,30,sep="-")
print(10,20,sep='-',end=" ")
print(60,60,sep='+')
# Open a file in write mode
with open("tomal is a good boy", 'w') as f:
    print(10,20,30,file=f)
    print(10,20,30,sep='+',file=f)
    print("tomal",end=" end",file=f)

