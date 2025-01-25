s1=int(input("enter marks of first subject:"))
s2=int(input("enter marks of second subject:"))
s3=int(input("enter marks of third subject:"))
if(s1<=39 or s2<=39 or s3<=39):
    print("fail")
if(40<=s1<=44):
    print("subject 1 grade:P")
elif(45<=s1<=49):
    print("subject 1 grade:C")
elif(50<=s1<=54):
    print("subject 1 grade:B")
elif(55<=s1<=59):
    print("subject 1 grade:B+")
elif(60<=s1<=69):
    print("subject 1 grade:A")
elif(70<=s1<=79):
    print("subject 1 grade:A+")
elif(80<=s1<=100):
    print("subject 1 grade:O")
else:
    print("enter valid marks")
if(40<=s2<=44):
    print("subject 2 grade:P")
elif(45<=s2<=49):
    print("subject 2 grade:C")
elif(50<=s2<=54):
    print("subject 2 grade:B")
elif(55<=s2<=59):
    print("subject 2 grade:B+")
elif(60<=s2<=69):
    print("subject 2 grade:A")
elif(70<=s2<=79):
    print("subject 2 grade:A+")
elif(80<=s2<=100):
    print("subject 2 grade:O")
else:
    print("enter valid marks")
if(40<=s3<=44):
    print("subject 3 grade:P")
elif(45<=s3<=49):
    print("subject 3 grade:C")
elif(50<=s3<=54):
    print("subject 3 grade:B")
elif(55<=s3<=59):
    print("subject 3 grade:B+")
elif(60<=s3<=69):
    print("subject 3 grade:A")
elif(70<=s3<=79):
    print("subject 3 grade:A+")
elif(80<=s3<=100):
    print("subject 3 grade:O")
else:
    print("enter valid marks")