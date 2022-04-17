#count length of value

a={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5:'black'}
b={}
for i in a.values():
    length=len(i)
    b.update({i:length})
print(b)

