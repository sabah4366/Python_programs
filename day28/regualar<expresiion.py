#functions
#match,search,findall,substi
#match function is used for check at the beginning of the string
#syntax of match re,match('word',stringname)
import re
# s="hai sabah how are you"
# res=re.match('h',s)
# print(res)      #ith nammal kodthe word eth postionl aan ullath aa location print chyyum
# if res:
#     print("item exist")
# else:
#     print("item not excist")
#search
#search is used for nammal kodkinne word or character search chyyum excisting aaytulla stringl indon check chyyum
#match check chyyunnath at the beginning aayirikkum but search check chyyunnath entire string check chyyum
# s="hai sabah how are you"
# res=re.search('you',s)
# print(res)
# if res:
#     print("item exist")
# else:
#     print("item not excist")

#patterns
#bracket nte ullil kodkkinne r enthinaan vechaal intrepreter regular expression patterns aaanenn manasilaavaan
#findall
# s='das 345 ghfh 56 67 hguhht @@ 768'
# res1=re.findall(r'\d',s)        #\d means only digits will print,each digit print with a string('3','4','5','5','6'...) like this but + will print like
# res2=re.findall(r'\d+',s)       #that + print like ('345','56','67','768')
# res3=re.findall(r'\D',s)        #print withou digits
# res4=re.findall(r'\D+',s)
# print(res1)
# print(res2)
# print(res3)
# print(res4)

#substute
#substute is used for nammal kodkkinne aa pattern na vera oru value vechitt substute or replace chyyan vendi
#sub
# s='das 345 ghfh 56 67 hguhht @@ 768'
# res=re.sub(r'\d','!',s)
# res1=re.sub(r'\s','!',s)        #\s means spaces are replace with !
# print(res)
# print(res1)

#
s="das 345 ghfh 56 67 hguhht @@ 768"
res=re.sub(r'[0-5]','!',s)
res1=re.sub(r'[a-k]','!',s)
print(res)
print(res1)


#
# s='das 345 ghfh 56 67 hguhht @@ 768'
# res=re.sub(r'[0-5 a-f]','!',s)  #this means 0-5 a-f will replace with !
# res1=re.sub(r'\s','$',s,2)      #You can control the number of replacements by specifying the count parameter:
# print(res)
# print(res1)
#
# s='das 345 ghfh 56 67 hguhht @@ 768'
# res=re.sub(r'[^0-5 a-f]','!',s)         #^0-5 means except that values are replace with !
# print(res)
# ress=re.split(r'\s+',s)
# res4=re.split(r'\s+',s,1)             #you can specify maxsplit that is 1
# print(ress)
# print(res4)




#SPECIAL SEQUENCES
# 1 -\A	Returns a match if the specified characters are at the beginning of the string	"\AThe"
# 2-\b	Returns a match where the specified characters are at the beginning or at the end of a word
# (the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\bain"
# r"ain\b"
# 3-\B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
# (the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\Bain"
# r"ain\B"
# 4-\d	Returns a match where the string contains digits (numbers from 0-9)	"\d"
# 5-\D	Returns a match where the string DOES NOT contain digits	"\D"
# 6-\s	Returns a match where the string contains a white space character	"\s"
# 7-\S	Returns a match where the string DOES NOT contain a white space character	"\S"
# 8-\w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"
# 9-\W	Returns a match where the string DOES NOT contain any word characters	"\W"
# 10-\Z	Returns a match if the specified characters are at the end of the string	"Spain\Z"
