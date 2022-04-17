#sort a list alphabetically...



dic={
    "L1":[87,34,56,12],
    "L2":[23,00,30,10],
    "L3":[1,6,2,9],
    "L4":[40,34,21,67]
}

for i,j in dic.items():
    dic1={i:sorted(j)}

    print(dic1)






dic={1:['a','f','d','c'],2:['f','s','a']}


for i,j in dic.items():
    dic2={i:sorted(j)}
    print(dic2)

