#in writing function we can write somethinf into file using "w"
#1
f2=open('file_1','w')
f2.write('hello')       #hello will write into the file_1
f2.close()

#
#2
f3=open('file_1','w')
f3.writelines(['first line\n','second line\n','third line'])    #this will write three lines into the file_1
f3.close()                                                      #you must write [] inside of these bracket
                                                                #if you not use these bracket you cannot write multiple lines