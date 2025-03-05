lst=[("24BEC147","Pavish",18),("24BEC142","Jash",18),("24BEC122","Moksh",18)]
lstrollno=[]
lstname=[]
lstage=[]
for i in lst:
    for j in i:
        if isinstance(j,str) and "24BEC" in j:
            lstrollno.append(j)
        elif isinstance(j,str) and "24BEC" not in j:
            lstname.append(j)
        else:
            lstage.append(j)
print(f"Roll no of student:{lstrollno}")
print(f"Name of student:{lstname}")
print(f"Age of student:{lstage}")