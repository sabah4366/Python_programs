#dictionary creating
dict={'name':'sabah','place':'kannur','cource':'bca'}
print(len(dict))
print(dict)
dict.update({'name':'sabah k','mark':'50'})
print(dict)

#print(dict.keys())
#print(dict.values())
#print(dict.items())
# print(len(dict))
# dict.update({'age':22,'fathername':'muhammed kutty'})   #for adding multiple elements
# print(dict)


# #find the count of items occur in the list using dictionary
# lst=['apple','orange','mango','apple','orange','mango']
# dict={}
# for i in lst:
#     if i not in dict:
#         dict[i]=1

#     else:
#         dict[i]=dict[i]+1
# print(dict)

# #deleting items in the dictionary
# dict={"name":'sabah','place':'kannur','school':'kambil','college':'hamdard','course':'bca'}
# dict.pop('name')        #this will remove that key
# dict.popitem()          #this will delete the last item
# print(dict)
# #multiple items added in dictionary
# dict={"name":'sabah','place':'kannur','school':'kambil'}
# dict.update({'college':'hamdard','course':'bca'})   #adding multiple items in ditionary
# print(dict)
# print(dict['name'])     #print that key value
# print(dict.keys())  #printing keys only
# print(dict.values())    #printing values only
# print(dict.items())     #printing dict_items
# dict['school']='chm'    #this for the key school value changing
# print(dict)
# for i in dict.items():      #this will print keys and values into tuple
#     print(i)

# for i,j in dict.items():    #this will print keys and values without bracket and quotes
#     print(i,j)




# lst=['apple','orange','mango','apple','orange','mango']
# dict={}

# for i in lst:
#     if i not in dict:
#         dict[i]=1
#     else:
#         dict[i]=dict[i]+1
# print(dict)