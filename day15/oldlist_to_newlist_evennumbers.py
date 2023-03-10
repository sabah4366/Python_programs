#create a new list that contain  even numbers and odd numbers from excisting list
lst=input("enter the list elements").split()
evenlst=[]
oddlist=[]
for i in lst:
    if int(i)%2==0:
        evenlst.append(int(i))
    else:
        oddlist.append(int(i))

print("even list",evenlst)
print("oddlist",oddlist)