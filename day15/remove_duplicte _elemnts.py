# #create a new list and remove duplicate elements in a list in a exciting list
# lst=input("enter the elements ").split()
# newlst=[]
# for i in lst:
#     if int(i) not in newlst:
#         newlst.append(int(i))
# ao=f"newlist{newlst}"
# print(ao)
#
#


lst=input('enter numbers').split()
print(lst)
nwlst=[]
for i in lst:
    if i not in nwlst:
        nwlst.append(i)
print(nwlst)