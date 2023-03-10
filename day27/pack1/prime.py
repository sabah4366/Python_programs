def primnumbers(a):
    flag=0
    for i in range(2,a):
        if a%i==0:
            flag=1
    if flag==1:
        print("its not a prime number ")
    else:
        print("its a prime number")