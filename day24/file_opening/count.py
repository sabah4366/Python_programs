#count the number of lines in a file
f1=open('/home/sabah/PycharmProjects/luminar1/day24/file_opening/fil_5.txt')
lt=f1.readlines()
print(lt)
print(len(lt))
f1.close()


# #count the numbers of words in a file
f1=open('/home/sabah/PycharmProjects/luminar1/day24/file_opening/file_1','r')
lst=f1.read()
s=lst.split()
print(s)
print(len(s))
f1.close()



# #count the numbers of same words
f1=open('/home/sabah/PycharmProjects/luminar1/day24/file_opening/file_1','r')
f2=f1.read()
lst=f2.split()
dict={}
for i in lst:
    if i not in dict:
        dict[i]=1
    else:
        dict[i]=dict[i]+1
print(dict)
for k,v in dict.items():
    print(k,":",v)
f1.close()

