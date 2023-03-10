st=input("enter a string")
print(st[::-1])


st=input("enter a string")

if st[::-1]==st[::]:
    print('palindrome')
else:
    print('not palindrome')