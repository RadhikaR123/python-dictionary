
a=[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue',4), ('red', 1)]

dic={}

for i,j in a:
    dic.setdefault(i,[]).append(j)

print(dic)



