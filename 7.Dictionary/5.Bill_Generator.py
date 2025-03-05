items={"milk":60,"bread":30,"sugar":30}
#quantities are in liter,kg,packet
bill1={"milk":2,"bread":2,"sugar":1}
sum=0
for i,j in bill1.items():
    sum+=items[i]*j
print(bill1)
print(f"Total Bill:Rs.{sum}")