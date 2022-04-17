# split the dictionary of list and list into dictionary.....

dic={'Science': [88, 89, 62, 95], 'Language': [77, 78,84, 80]}
dic1={}
li=[]
for i in dic.keys():
    li.append(i)
print(li)
for j in dic.values():
    