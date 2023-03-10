#number of vowels ,spaces and consonants of a given string
a=input("enter a string")
v=0
sp=0
cons=0

for i in a:
    if i in "aeiouAEIOU":
        v=v+1

    elif i==" ":
        sp=sp+1

    else:
        cons=cons+1

print("number of vowels",v,"\nnumber of spaces",sp,"\nnumber of consants",cons)



