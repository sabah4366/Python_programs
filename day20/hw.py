#print only even length words in a given string
strng="i am very happy and how are you my girl".split()
print(strng)
for i in strng:
    if len(i)%2==0:
         print(i)


