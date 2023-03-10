#this will read complete file
# print("HEADING")
# f2=open('/home/sabah/PycharmProjects/luminar1/day24/file_opening/file_1','r')
# print(f2.read())  #this is for read the complete file
# f2.close()          #this is for close the file


#this will read the characters
# print("HEADING")
# f1=open('/home/sabah/PycharmProjects/luminar1/day24/file_opening/file_1','r')
# print(f1.read(6))       #that 6 for the characters read 0th index to 6th index characters
# print(f1.tell())        #tell() function will tell the standing position of the pointer
# f1.seek(0)              #to relocate to 0th index we use seek(0) and we specify the index inside the seek function
# print(f1.read(9))       #ths will read 6th index to 9th index characters because the pointer is stand at 6th index
# f1.close()


# #this will read first single line of the file
print("HEADING")
f4=open('file_1','r')
print(f4.readline().strip())    #this will read the first line of the file
print(f4.readline())    #this will read the second line with the gap of new line (first line and one new line then second line)
f4.close()              #to avoid the new line we use strip function


# #this is for read multiple lines of the file
# print("HEADING")
# f5=open('file_1','r')
# print(f5.readlines())    #this will read complete file lines,but this lines are in the list form with a \n
# f5.close()               #\n indavum at the end of each line

# #in the above program we can print each line in a newline using for loop
# print("HEADING")
# f6=open('file_1','r')
# for i in f6:
#     print(i.strip())         #this strip is used for avoid the extra new line

