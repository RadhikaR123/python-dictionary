#drop empty item....

a={'c1': 'Red', 'c2': 'Green', 'c3':""}

size=len(a)
size1=len(a)-1
for i,j in a.items():
    if j=="":
        a.pop(i)
        if size==size1:
            break
    print(a)




