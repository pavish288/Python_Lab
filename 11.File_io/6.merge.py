fo1=open("/home/netvincible/Documents/Python/college-sem-2/lab-10/6/shell_history.txt","r")
fo2=open("/home/netvincible/Documents/Python/college-sem-2/lab-10/6/shell.txt","r")
fw=open("/home/netvincible/Documents/Python/college-sem-2/lab-10/6/result.txt","w")

line1=fo1.readline()
line2=fo2.readline()
while(line1 and line2):
    fw.write(line1)
    fw.write(line2)
    line1=fo1.readline()
    line2=fo2.readline()
else:
    remaining=fo1 if line1 else fo2
    line=line1 if line1 else line2
    fw.write(line)
    fw.write(remaining.read())
fo1.close()
fo2.close()
fw.close()