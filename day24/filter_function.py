#syntax of filter
#newloist=list(filter(lambda x:x>=6,lst))
#uses of filter function
#filter is used for when a condition is satisfied the that value only executed
lst=[1,2,3,4,5,6,7,8,9]
lst1=list(filter(lambda x:x%2==0,lst))
print(lst1)


#create a new list that list contain only above 3 from existing list
lst=[1,2,3,4,5,6,7,8]
newlst=list(filter(lambda x:x>3,lst))
print(newlst)

#print a newlist that greater than the len(x)>5
lst=['apple','grapes','jerry','kiwi','pineapple','pomegranate']
newlst=list(filter(lambda x:len(x)>5,lst))
print(newlst)


#accept a list from user and create a even and odd list from that list
lst=(input("enter the elememts")).split()
newlst=list(map(int,lst))
el=list(filter(lambda x:x%2==0,newlst))
ol=list(filter(lambda x:x%2!=0,newlst))
print("even list is:",el)
print('odd list is:',ol)

