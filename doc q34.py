

a={'key1': 1, 'key2': 3, 'key3':2}
b={'key1': 1, 'key2': 2}

for i,p in a.items():
    for j,q in b.items():
        if i==j:
            print(i,"is present in both")
