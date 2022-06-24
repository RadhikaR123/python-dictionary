# remove duplicate from a dictionary.....not complited



dic={
"ball":"red",
"bat":4,
"wickets":8,
"ball":"green",
"bat":3
}

dic1={}

for i,j in dic.items():
    if i not in dic1:
        dic1[i]=j
print(dic1)
