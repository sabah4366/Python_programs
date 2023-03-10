#copying the data of  a file to file_2
f1=open('/home/sabah/Downloads/Readme.txt','r')
f=f1.read()
f2=open('/home/sabah/PycharmProjects/luminar1/day24/file_opening/file_2','w')
f2.writelines(f)
f1.close()
f2.close()
