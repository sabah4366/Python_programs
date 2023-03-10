lst=input("enter the elements").split()
print(lst)
evenlst=[]
oddlst=[]
for i in lst:
    if int(i)%2==0:
        evenlst.append(int(i))
    else:
        oddlst.append(int(i))
print(evenlst)
print(oddlst)



num=input("enter numbers").split()
print(num)
evenlst=[]
oddlst=[]

for i in num:
    if int(i)%2==0:
        evenlst.append(int(i))
    else:
        oddlst.append(int(i))

print(evenlst)
print(oddlst)