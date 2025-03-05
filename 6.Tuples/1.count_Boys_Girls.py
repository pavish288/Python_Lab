lst=[("Pavish","Jash","Kirtna","Jay"),"Ananya","Heli","Mokshda","Nandani"]
countb=0
countg=len(lst)
for i in lst:
    if(isinstance(i,tuple)):
        countg-=1
        for j in i:
            countb+=1
print(f"Number of boys:{countb}")
print(f"Number of girls:{countg}")