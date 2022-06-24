

a='MISSIIMIIS'
b={}
count=0
for i in range(0,len(a)):
    for j in range(0,len(a)):
        if a[i]==a[j]:
            count+=1
    b.update({a[i]:count})
    count-=count
        
print(b)