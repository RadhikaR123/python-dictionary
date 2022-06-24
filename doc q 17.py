# sort the dictoianry by key....

dic={2:'two',5:'five',1:'one',4:'four',3:'three'}
temp={}
li=[]
for i in dic.keys():
    li.append(i)
print(li)
for j in range(len(li)):
    for k in range(j+1,len(li)):
        if li[j]>li[k]:
            li[j],li[k]=li[k],li[j]
print(li)
for l in li:
    for r in dic.keys():
        if l==r:
            temp[l]=dic[r]
print(temp)


print("hi hello")