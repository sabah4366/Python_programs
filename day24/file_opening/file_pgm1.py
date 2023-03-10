#luminar study

f1=open('file_1','r')
# print(f1.readlines())    #this 6 is for read the cha
# print(f1.tell())
# f1.seek(0)
# print(f1.tell())
# print(f1.read(3))

# print(f1.readline())
# print(f1.readlines())
f=f1.readlines()
for i in f:
    print(i.strip())
f1.close()



