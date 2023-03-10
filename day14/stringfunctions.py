#there are somany string functions in python some of them are below
#length of the given string
s="sabah pallipparamba"
print(len(s))

#convert string into uppercase of all letters
print(s.upper())

#convert string into frst leter of each word is capital

print(s.title())

#swap lower cae to upper and upper to lower
d="SABAH pallipparamb"
print(d.swapcase())

#check given string is all in upper or lower then return true or false
#return boolean value true or false
s1="hai"
s2="HELLO"
print(s1.isupper())
print(s1.islower())
print(s2.isupper())
print(s2.islower())

#check index number of the character of the given string
s="hello hello how how are you"
print('jjhhih')
print(s.index('u'))
print(s.index('how'))

#count of the perticular character or word in the given string
f="hello hello how are you"
print(f.count('o'))
print(f.count('hello'))

#strip strip,lstrip,rstrip
c="@@#sabah k@@"
print(c.strip('@#'))