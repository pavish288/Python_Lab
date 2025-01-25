a=int(input("enter radius:"))
x=int(input("enter x coordinate of center:"))
y=int(input("enter y coordinate of center:"))
x1=int(input("enter x coordinate of point:"))
y1=int(input("enter y coordinate of point:"))
if int(pow(x1-x,2)+pow((y1-y),2))==a*a:
    print("point is on circle")
elif int(pow(x1-x,2)+pow((y1-y),2)>a*a):
    print("point is outside circle")
else:
    print("point is inside circle")