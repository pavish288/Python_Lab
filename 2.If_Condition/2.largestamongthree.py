a=int(input("enter a:"))
b=int(input("enter b:"))
c=int(input("enter c:"))
if(a>=b and a>=c):
    print("a is largest")
    if(b>=c):
        print("c is smallest")
    else:
        print("b is smallest")
elif(b>=c):
    print("b is largest")
    if(c>=a):
        print("a is smallest")
    else:
        print("c is smallest")
else:
    print("c  is largest")
    if(b>=a):
        print("a is smallest")
    else:
        print("b is smallest")