#count number of element of a dictionary...


a=[{'id': 1, 'success': True, 'name': 'Lary'},{'id': 2, 'success': False, 'name': 'Rabi'},{'id': 3, 'success': True, 'name': 'Alex'}]
id1=0
bol=''
name=''


for i in a:
    for j,k in i.items():
        # print(j)
        if j=="id":
            id1=id1+k
        elif j=="success":
            bol=bol+str(k)
        else:
            name=name+k

print(id1)
print(bol)
print(name)

            



