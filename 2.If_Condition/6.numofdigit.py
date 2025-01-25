a=int(input("enter number:"))
count=0
if(a==0):
    print("number of digits:1")
else:
    while(a>0):
        a=a//10
        count+=1
    print("number of digits:",count)