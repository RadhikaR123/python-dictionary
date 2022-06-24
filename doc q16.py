#make a dictonary from 2 lists......

a=[1,2,3,4,5]
b=['one','two','three','four','five']
c={}

# for i in range(1,len(a)+1):
#     c[i]=b[i-1]
# print(c)


for i in range(len(a)):
    c.update({a[i]:b[i]})
print(c)

