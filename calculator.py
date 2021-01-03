import math

print("\t_____________CALCULATOR_____________")

def sum(a,b):
    a+=b
    return a

def sub(a,b):
    if (a>b):
        a-=b
        return a
    else :
        b-=a
        return b
def mul(a,b):
    a*=b
    return a

def div(a,b):
    q=a%b
    r=a/b
    print("\n the quotient is  %s  =",q)
    print("\n the  remainder is  %s  =",r)

def sqr(a):
    x=math.sqrt(a)
    return x

while(1):
    print("\n Choose the operation you want to perform")
    print("\n \t 1.addition")
    print("\n \t 2.substraction")
    print("\n \t 3.multiplication")
    print("\n \t 4.Division")
    print("\n \t 5.Square root")
    print("\n \t 6.Exit")
    
    choice=int(input(">"))
    
    if choice==1:
        print("\n \n Enter the two number")
        num1=int(input(">"))
        num2=int(input(">"))
        s=sum(num1,num2)
        print("the sum is %s ",s)
    elif choice==2:
        print("\n \n Enter the two number")
        num1=int(input(">"))
        num2=int(input(">"))
        m=sub(num1,num2)
        print("the sub is %s ",m)
    elif choice==3:
        print("\n \n Enter the two number")
        num1=int(input(">"))
        num2=int(input(">"))
        p=mul(num1,num2)
        print("the mul is %s ",p)
    elif choice==4:
        print("\n \n Enter the two number")
        num1=int(input(">"))
        num2=int(input(">"))
        div(num1,num2)
     
    elif choice==2:
        print("\n \n Enter the two number")
        num1=int(input(">"))
        r=sqrt(num1)
    else:
        print("\n you choose to exit, BYE")
        break
        