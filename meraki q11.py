
# my_dict = {
# 'a':50,
# 'b':58,
# 'c':56,
# 'd':40,
# 'e':100,
# 'f':20
# }

# a=[]
# b={}
# for i in my_dict.values():
#     a.append(i)
# print(a)

# first_max=a[0]
# length=len(a)
# i=0
# while i<len(a):
#     if a[i]>first_max:
#         first_max=a[i]
#         # b.update({a[i]:first_max})
#     i=i+1
# print("first maximum value is:",first_max)
# second_max=0
# for i in a:
#     if i>second_max:
#         if i!=first_max:
#             second_max=i
#             # b.update({i:second_max})
# print("second max is:",second_max)
# third_max=0
# for i in a:
#     if i>third_max:
#         if i!=first_max and i!=second_max:
#             third_max=i
#             # b.update({i:third_max})
# print("third max is :",third_max)

    

my_dict = {
'a':50,
'b':58,
'c':56,
'd':40,
'e':100,
'f':20
}

dic={}
first_max=my_dict['a']
for i in my_dict.keys():
    for j in my_dict.values():
        if j>first_max:
            first_max=j
print("firstmax is :",i,first_max)

second_max=0
for i,j in my_dict.items():
    if j>second_max and j<first_max:
        second_max=j
print("second max is:",second_max)

third_max=0
for i in my_dict.values():
    if i>third_max and i<second_max and i<first_max:
        third_max=i
print("third max is :",third_max)











