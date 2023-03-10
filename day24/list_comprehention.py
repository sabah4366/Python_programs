#list comprehension
#syntax
#expression for i in sequence
#advantage-reduce code than the map,filter and lambda

#
lst=['apple','orange','mango']
newlst=[x.upper() for x in lst]
print(newlst)


#
lst=[1,2,3,4,5,6,7,8,9,10]
newlst=[i*i for i in lst]
print(newlst)


#
lst=[1,2,3,4,5,6]
newlst=['hello' for i in lst]
print(newlst)


#
lst=[i for i in range(10)]
print(lst)

#
lst=[i*i for i in range(10)]
print(lst)


#
lst=['hello'.upper() for i in range(10)]
print(lst)


#list compprehention using if condition
3
lst=[1,2,3,4,5,6,7,8,9]
lmt=6
newlst=[x for x in lst if x<=lmt]
print(newlst)


#
lst=[1,2,3,4,5,6,7,8,9,10]
newlst=[x*x for x in lst if x%2==0]
print(newlst)


# create a new list taht contains word with letter '0'
lst=['lilly','rose','lotus','daisy']
newlst=[x for x in lst if 'o' in x ]
print(newlst)



# two condition that is we want to execute if statement and else statement
lst=[1,2,3,4,5,6,7,8,9]
newlst=['even' if x%2==0 else 'odd' for x in lst]
print(newlst)