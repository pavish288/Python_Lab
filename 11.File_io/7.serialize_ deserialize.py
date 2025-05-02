import json
employee={"empcode":1, "empname":"Baigan", "Date of Joining":"1/1/2898", "Salary":"1 kaudi"}
f=open("/home/netvincible/Documents/Python/college-sem-2/lab-10/7/file.txt","w+")
json.dump(employee,f)
f.seek(0)
dictionary=json.load(f)
print(dictionary)
f.close()