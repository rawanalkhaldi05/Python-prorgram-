import math
def divprod(x,y):
    return x/y , x*y

def power(x, n):
    return x**n

def sumsq(a,b,c):
    if(a+b >c):
        return math.sqrt(a+b-c)
    else:
        print("third number must ne less than first two numbers u entered")

con='no'
while con[0]=='n':
    print('1- division & product')
    print('2- power n of a number')
    print('3- square root expression ')
    op =eval(input('enter your choice:'))
    if op==1:
            x=int(input("enter a number:"))
            y=int(input("enter a number:"))
            d,p=divprod(x,y)
            print("the result of the division:",d)
            print("the result of the product:",p)
    elif op==2:
     x=int(input('enter the base of the number to find the power'))
     n=int(input("enter the power number:"))
     print("the power of the number is: ",power(x,n))
    elif op==3:
     a,b,c = eval(input("enter three numbers to find square root:"))
     print("square root result:",sumsq(a,b,c) )
    con= input("do u want to stop?")







