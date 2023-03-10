#create a new tuple that contain only even numbers
tpl=(1,2,3,4,5,6,7,8)
newlst=[]
for i in tpl:
    if i%2==0:
        newlst.append(i)
tpl=tuple(newlst)
print(tpl)

