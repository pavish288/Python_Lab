def frequency(String):
    dict={}
    lst=sorted(String.split())
    for i in lst:
        dict.update({i:lst.count(i)})
    return dict
print(frequency("Pavish Pandya Pandya Dhaval Dhaval Dhaval"))