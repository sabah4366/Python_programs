#duplication exists
lst=['apple','orange','carrot','apple']
lst2=[]
flag=0
for i in lst:
    if i not in lst2:
        lst2.append(i)
    else:
        print("element exists")
        break

#or (this is another method of the above program)
lst=['apple','orange','carrot','apple','apple']
for i in lst:
    if lst.count(i)>1:
        print("yes element exists")




#fibanoocci series
f=0
s=1
n=8
for i in range(n):
    if f<n:
        print(f)
        t=f+s
        f=s
        s=t





