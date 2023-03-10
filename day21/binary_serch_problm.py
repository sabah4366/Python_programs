list1=[1,2,3,4,5,6,7]
key=10

def bnrysrch(lst,k):
    low=0
    high=len(lst)-1
    mid=0
    while (low<=high):
        mid=(low+high)//2
        if lst[mid]>k:
            high=mid-1
        elif lst[mid]<k:
            low=mid+1
        else:
            return mid
    return -1
res=bnrysrch(list1,key)
if res==-1:
    print("not found")
else:
    print("found")
