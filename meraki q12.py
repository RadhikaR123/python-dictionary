
size=int(input("enter number of values that u want to print :"))
dic={}
for i in range(size):
    a=int(input("enter the key :"))
    
    b=a*a
    dic.update({a:b})

print(dic)





