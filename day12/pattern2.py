# num=int(input("enter a limit"))
# sp=num
# f=1
# for i in range(1,num+1):
#     for j in range(1,sp):
#         print(end=" ")
#     sp=sp-1
#     for k in range(1,i):
#         print(k,end=" ")

#     print()


num=5
for i in range(num):
    for j in range(0,num):
        print(" ",end="")
    for k in range(0,i):
        print("*",end="")
    print("")
    num=num-1