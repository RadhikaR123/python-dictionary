# Q1.Write a Python program to combine two dictionaryadding values for common keys.




d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d3={}
# for x in d1:
#     # for y in d2:
#         if x in d2:
#             d1[x]=d1[x]+d2[x]
#             d2.update(d1)
#         else:
#             d1[x]=d1[x]
        
# print(d2)
    

for i in d1.keys():
    for j in d2.keys():
        if i==j:
            d3[i]=(d1[i]+d2[j])
if i not in d3:
    d3[i]=d1[i]
if j not in d3:
    d3[j]=d2[j]
print(d3)