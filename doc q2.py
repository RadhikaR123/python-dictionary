# program to find duplicate character of a string...




str1=input("enter the string :")

# d=list(str1)
# print(d)
li={}

for i in str1:
    count=0
    for j in str1:
        if i==j:
            count+=1
    li[i]=count

print(li)





