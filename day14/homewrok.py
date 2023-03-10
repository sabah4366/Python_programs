#remove tha character of the nth index of a given string
#accept a index number for removing
s=input("enter a string")
delt=int(input("enter the removing index"))
f=s[:delt-1]+s[delt:]
print(f)


