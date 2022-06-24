




dic1 = {
'a':50,
'b':58,
'c': 56,
'd':40,
'e':100,
'f':20
}
justValues=dic1.values()
max=0
newList=[]
for i in justValues:
    newList.append(i)
    if i>max:
        max=i
print(max,"first max")
newList.remove(max)
print(newList)
    

