
my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
b=[]

for i in my_dict:
    print(i,end=" ")
    b.append(my_dict[i])
# print(b)
print()
i=0
while i<=3:
    j=0
    while j<=3:
        print(b[i][j],end=" ")
        print(b[0][1],end=" ")
        j=j+1
    i=i+1






dic={"a":{"b":{}},"d":{"e":{}}}
dic1={}

for i,j in dic.items():
    for k,v in j.items():
        dic1[k]={i:{}}
print(dic1)
