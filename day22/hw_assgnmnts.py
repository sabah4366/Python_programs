#a list of string elements split into elemenmts in a string
lst=['sabah','irfan','aslah','safwan']
newlst=list(map(list,lst))
print(newlst)


#check given string is symmetric or not
strg="saazsaa"
if len(strg)%2==0:
    str1=strg[:int(len(strg)/2)]
    str2=strg[int(len(strg)/2):]
else:
    str1=strg[:int(len(strg)//2)]
    str2=strg[int((len(strg)//2)+1):]
if str1==str2:
        print('symmetric')
else:
        print("not symmetric")




#find the words in a string that is greater than given length
strng="hai iam sabah k".split()
print(strng)
def sss(s):
    leng = 5
    if len(s)>=leng:
        print(s)
newls=(list(map(sss ,strng)))


#multiply all the elemets in alist
lst1=[1,2,3,4,5,6]
newlst=list(map(lambda x:x*x,lst1))
print(newlst)


