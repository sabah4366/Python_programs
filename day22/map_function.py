#this program is a list of strings converted directly into a list of integers using map function
lst=['1','2','3','4','5']
newlst=list(map(int,lst))
print(newlst)

# this program is list of strings and print the lenght of that string
str=['apple','orange','mango','banana','pomegranate','kiwi']
newlst=list(map(len,str))
print(newlst)


#in the above program we use bultin function like int ,len
#now this program we will use a user defined function
def sqr(n):
    return n*n
lst=[1,2,3,4,5,6]
newlst=list(map(sqr,lst))
print(newlst)


#this is we adding each element in a list with 10
def sum(n):
    return n+10
lst=[1,3,5,6,8,9]
newlst=list(map(sum,lst))
print(newlst)


#we can reduce code with lambda function dont want a user defined function
lst=[1,3,5,7,9]
newlst=(list(map(lambda x:x*x,lst)))
print(newlst)


#create a new list that contain cube of every element in the excisting list
lst=[2,3,4,5,6,7]
newlst=list(map(lambda y:y**3,lst))
print(newlst)

#create a newlist that contain all the elements in uppercase

lst=['apple','orange','banana']
newlst=list(map(lambda i:i.upper(),lst))
print(newlst)


#above program using bult in function
lst=['apple','orange','banana']
def uppr(n):
    return n.upper()
newlist=list(map(uppr,lst))
print(newlst)
