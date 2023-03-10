
lst=input("enter a list").split()
print(lst)
newlst=[]
for i in lst:
    newlst.append(int(i))
newlst.sort()
print(newlst)
key=int(input("enter the search key"))
def bnry(nwlst,k):
    low=0
    high=len(nwlst)-1
    mid=0
    while low<=high:
        mid=(low+high)//2
        if nwlst[mid]>k:
            high=mid-1
        elif nwlst[mid]<k:
            low=mid+1
        else:
            return mid
    return -1

res=bnry(newlst,key)
if res==-1:
    print("not found")
else:
    print("found")