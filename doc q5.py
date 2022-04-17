#ascending order///////incomplete


d={1: 2, 3: 4, 4: 3, 2: 1, 0:0}
d1=[]
# d2=[]
li={}
for k in d.keys():
    d1.append(k)
    # d2.append(d[k])
# print(d1)

for i in range(0,len(d1)):
    for j in range(i+1,len(d1)):
        if d1[i]>d1[j]:
            d1[i],d1[j]=d1[j],d1[i]
# print(d1)
for x in d1:
    li.update({x:d[x]})
print(li)




# d1=(sorted(d.values()))
# print(d1)






