#some list functions
print(5%2)
lst=['banana','apple','apple','oramge','pomegranate']
print(len(lst))
print(lst.count('apple'))       #count of apple

print(lst.index('pomegranate'))     #index number of pomegranate

lst.pop(3)      #if we use pop then use index number inside the pop function
print(lst)

lst.remove('apple')     #if we use remove then element inside the remove function
print(lst)