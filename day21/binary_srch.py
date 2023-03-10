key=111
lst=[1,2,3,4,5,6,7]

def fun(lsttt,k):
    f = 0
    l = len(lst) - 1
    m = 0
    while (f<=l):
        m=(f+l)//2
        if lsttt[m]<k:
            f=m+1
        elif lsttt[m]>k:
            l=m-1
        else:
            return m
    return -1

res=fun(lst,key)
if res==-1:
    print("not found")
else:
    print("found")


