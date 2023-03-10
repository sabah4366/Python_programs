ll=int(input("enter a lower limit"))
ul=int(input("enter a upper limit"))
for i in range(ll,ul+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)



