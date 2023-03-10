for i in range(1,5):
    print()
    for j in range(1,5):
        print("*" ,end=" ")

print()

n=int(input("enter a limit"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(j ,end=" ")
    print()