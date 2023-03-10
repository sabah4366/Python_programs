#find the maximum element in a tuple without using any functions
tup=tuple(input("enter the tuple elements").split())
max=0
for i in tup:
    if int(i)>max:
        max=int(i)
print(max)

