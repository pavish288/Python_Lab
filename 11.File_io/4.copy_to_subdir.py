import os
subdir=input("Enter name of sub directory:").strip()
if os.path.exists(subdir):
    print(f'{subdir} already exists.')
else:
    os.mkdir(subdir)
targate=input("Enter file to be copied:").strip()
found=False
for root,dir,files in os.walk("C:\\Users\\Pavish\\Python"):
    if targate in files:
        abs_path=os.path.join(root,targate).replace("\\","/")
        found=True
        break
if found:
    os.chdir(os.path.abspath(subdir).replace("\\","/"))
    with open(abs_path,"r") as file:
        with open("copy","w") as fcopy:
            ch=file.read(1)
            while ch!="":
                fcopy.write(ch)
                ch=file.read(1)
            print("File copied successfully.")
else:
    print("File not found")