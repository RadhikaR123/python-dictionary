#convert str values into int and float

dic=[{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q':'50', 'r': '60'}]
dic1={}
for i in dic:
    for x,y in i.items():
        dic1[x]=float(y)
print(dic1)        




