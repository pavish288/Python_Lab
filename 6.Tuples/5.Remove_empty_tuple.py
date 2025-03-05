lst=[(),(1,),("Pavish","Pandya")]
print(lst)
for i in lst:
    if isinstance(i,tuple):
        if not i:
            lst.remove(i)
print(lst)