#exception handling
try:
    a=int(input("enter first number"))
    b=int(input("enter the second number"))
    div=a/b
    print(div)
except ZeroDivisionError:
    print("donot enter second number 0")
except ValueError:
    print("must enter a number")
except :
    print("error")
#finally:                       #finally will execute at the end
    print("always execute")
else:                       #else will execute if there is no exceptions then else will execute
    print("execute")