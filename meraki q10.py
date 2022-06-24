

dic1 = {
'Alex': ['subj1', 'subj2', 'subj3'],
'David': ['subj1', 'subj2']}
count=0
for i,j in dic1.items():
    for x in range(len(dic1[i])):
        print(dic1[i][x])
        count=count+1
print(count)


