#convert more than one list to dictionary...

a=['S001', 'S002', 'S003', 'S004']
b=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'SaimRichards']
c=[85, 98, 89, 92]
dic={}
dic1={}
i=0
while i<len(b):
    dic={b[i]:c[i]}
    dic1[a[i]]=dic
    i+=1
print(dic1)







