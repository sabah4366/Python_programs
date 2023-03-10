limit=int(input("enter a limit"))
for i in range(1,limit+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

#pyramid printing
n=4
g=1
for i in range(0,5):
    for j in range(1,n+1):
        print(end=" ")
    for k in range(1,g+1):
        print("*",end="")
    print()
    n=n-1
    g=g+2
