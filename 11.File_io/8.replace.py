import os
targate=input("Enter targate file:").strip()
found = False
for root, dirs, files in os.walk("C:\\Users\\Pavish\\Python"):
    if targate in files:
        abs_file_path=os.path.join(root, targate).replace("\\", "/")
        os.chdir(root)
        found = True
        break
if found:
    with open(abs_file_path,"r") as file:
        with open("Final","w") as cp:
            for line in file: 
                line=line.replace(" a "," ").replace(" an "," ").replace(" the "," ")
                cp.write(line)