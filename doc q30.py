#removing space....


dic1={'S  001': ['Math', 'Science'],'S    002': ['Math','English']}

for x,y in dic1.items():
    dic1={x.replace(" ",""):y}

    print(dic1)


