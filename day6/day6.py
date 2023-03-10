# area of a circle( pi r square(pi*r*r))
r = float(input("enter the radius"))
area = 3.14 * r * r
print("area of circle is", round(area, 5))  #round is used to round the last digits


# circumferrence of a circle -equatiion is 2*pi*r
r = float(input("enter the radius "))
circum = 2 * 3.14 * r
print("circumference of a circle =", circum)


# simple interest equation- si=pnr/100
p =int(input("enter the principle amount"))  # p is principl amount,n is number of years,r is interest rate
n =int(input("enter the number of years"))
r = float(input("enter the interest rate"))
si = (p * n * r) / 100
print("simple interest =", si)


#print last digit of a entered numbers using - %10
num=int(input("enter a number"))
d=num%10
print("last didgit is ",d)


#calculate using n+nn+n
n=int(input("enter a number"))
res=n+n*n+n
print("result is ")


#compound assignment operators (+=,-=,*=,/=,**=)
a=3
a+=5
print(a)
a-=2
print(a)
a*=2
print(a)


#temperature conversion f=(c*9/5)+32
c=int(input("enter a celcius value"))
f=(c*9/5)+32
print(f)



