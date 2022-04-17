#sort a list alphabetically....


li=[1,2,3,4,5]
dic=dic1={}
for i in li:
    dic1[i]={}
    dic1=dic1[i]

print(dic)





li=[1,2,3,4,5]
b={}
for i in li[::-1]:
    b={i:b}
print(b)