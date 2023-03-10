'''#if we accept a tuple from the user then we must use tuple and split'''
tpl=tuple(input("enter tuple elements").split())
print(tpl)


#find the count of elements greater than 10
tup=(1,2,3,4,34,45,11,)
count=0
for i in tup:
    if i>10:
        count = count + 1
print(count)


