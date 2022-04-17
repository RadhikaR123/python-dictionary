#sort by condition..value greater than given condition....

a={'Cierra Vega': 175, 'Alden Cantrell': 180, 'KierraGentry': 165, 'Pierre Cox': 190}
x=int(input("enterr the criteria :"))
for i,j in a.items():
    if j>x:
        print(i,j)

