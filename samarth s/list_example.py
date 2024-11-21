dict={"brand":"Maruti",
"year":1980,
"model":"sedan"
}
for x in dict:
    print(x)

#list opertion
mylist=["apple","Banana","Mango"]
mylist.append("cherry")
print(mylist)
mylist.remove("Mango")
print(mylist)
mylist.insert(4,"brinjal")
print(mylist)
mylist.pop(3)
print(mylist)
mylist.pop()
print(mylist)

#list
mylist=["apple","Banana","Mango"]
print(mylist[2:3])
print(mylist[:-1])
print(mylist[::-1])
print(mylist[-2:-1])