#remove specified id from given list of dictioanry.....


li=[{'id': '#FF0000', 'color': 'Red'}, {'id': '#800000','color': 'Maroon'}, {'id': '#FFFF00', 'color':'Yellow'}, {'id': '#808000', 'color': 'Olive'}]
a=[]

x=input("enter the id :")
for i in range(len(li)):
    if li[i]['id']==x:
        del li[i]
        break
print(li)


# print(li)


