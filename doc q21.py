#unique element

a=[{"V":"S001"}, {"V": "S002"}, {"VI":"S001"}, {"VI": "S005"}, {"VII":"S005"},{"V":"S009"},{"VIII":"S007"}]
b=[]
for i in range(0,len(a)):
    for j in a[i]:
        if a[i][j] not in b:
         b.append(a[i][j])

print(b)