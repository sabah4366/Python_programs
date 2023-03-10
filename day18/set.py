#set is unordered and unique
#not allow  duplicate items
#we can create a set in different data types
#set you cant change the value but you can add items
set1= { 2 ,True ,1,22,33, 'male'}
print(len(set1))
print(type(set1))
print(set1)
set2=set((1,3,4,5,6))  #set constructor to make set and note the double bracket
print(set2)

#you can add items into set using add() method
set3={1,2,3,4,'hai'}
set3.add(10)
set3.add("sabah")
print(set3)


#you can concatenate two set into one set unsing update() method
set4={1,2,3,4,'hai'}
set5={ 2 ,True ,1,22,33, 'male'}
set4.update(set5)
print(set4)

#you can concatenate a list into set using update method
set4={1,2,3,4,'hai'}
set5=[ 2 ,True ,1,22,33, 'male']
set4.update(set5)
print(set4)


#difference() function
set1={1,2,3,4}
set2={2,3,6,7,8}
print(set1.difference(set2))
print(set2.difference(set1))



#add() function
set1={1,2,3,4}
set1.add(10)
print(set1)

#remoove function
set1={1,2,3,4,5}
set1.remove(3)
print(set1)

#update function
set1={1,2,3,4}
set1.update({10,11,12,1,2})
print(set1)
