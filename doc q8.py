#check whether a key is present or not.....

dic={
"ball":"red",
"bat":4,
"wickets":8,
"ball":"green",
"bat":3
}



key=input("enter the element which you want to check in dict...")

for i in dic:
    if i==key:
        print(key,"is present in dictionary..")
    else:
        print(key,'is not present...')
