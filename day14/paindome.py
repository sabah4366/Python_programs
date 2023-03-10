
#string palindrom
st=input("enter a string")
ds=st[::-1]
if st==ds:
    print(st,"is a palidrome")
else:
    print(st,"is not palindrome")


#number palindrome
#if we accept a number in int then it will be error so accept in the same way of string(not use int)
st=input("enter numbers")
ds=st[::-1]
if st==ds:
    print(st,"is a palidrome")
else:
    print(st,"is not palindrome")

