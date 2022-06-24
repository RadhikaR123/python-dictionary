

list1=['one','two','three','four','five']

list2=[1,2,3,4,5,]


dict1={}


i=0
while i<5:
    dict1.update({list1[i]:list2[i]})
    i=i+1

print(dict1)