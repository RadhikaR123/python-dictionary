#access 5th element from keys....


a={'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],'y': [21, 22, 23, 24, 25, 26, 27, 28, 29],'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]}

for i in a.values():
    for j in range(5,6):
        print(i[j])






#sum of first element of nested list......
a=[[1,2],[3,4],[4,5]]
sum=0
i=0
while i<len(a):
    j=0
    while j<=i-i:
        sum=sum+a[i][j]
        j+=1
    i+=1
print(sum)

