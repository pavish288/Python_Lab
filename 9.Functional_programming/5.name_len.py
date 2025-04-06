lst=["rameshwar","pavish","jash","kumar","pavan","ravi","shankar","suresh"]
lst_name=list(filter(lambda x:isinstance(x,str) and len(x)>8,lst))
print(lst_name)