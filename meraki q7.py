

a=[
{"first":"1"},
{"second": "2"},
{"third": "1"},
{"four": "5"},
{"five":"5"},
{"six":"9"},
{"seven":"7"}
]

b=[]

for i in range(7):
    for key,value in a[i].items():
        if value not in b:
            b.append(value)
print(b)

