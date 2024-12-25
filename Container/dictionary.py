#Like Unordered Map
person = {"Tomal":18,"Tonu":20,"Rina":55}
print(person)
print(person["Tomal"])

print(person.get("Sohan","not Found"))
person["Tomal"] = 21
print(person["Tomal"])
print(person.keys())

for i in person.keys():
    print(i,end=" ")
print()
for i in person.values():
    print(i,end=" ")
print()

print(person.items())
#Removing Items
price = { 
    "apple" : 10,
    "Lebu"  : 13,
    "Kodu" :17,
    "Lau" :20
}
print(price)
print(price.pop("PEPE","NOt Found"))
print(price)
