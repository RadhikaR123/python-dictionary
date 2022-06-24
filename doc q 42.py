#program to check all values are same or not


a={'Cierra Vega': 12, 'Alden Cantrell': 1, 'KierraGentry': 2, 'Pierre Cox': 7}

for i in a.values():
    for j in a.values():
        if i==j:
            print("true")
            break
        else:
            print("false")
            break