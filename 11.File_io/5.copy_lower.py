import os
targate = input("Enter file name to be copied: ").strip()
copy = input("Enter file where to be copied: ").strip()
found = False
for root, dirs, files in os.walk("C:\\Users\\Pavish\\Python"):
    if targate in files:
        abs_file_path=os.path.join(root, targate).replace("\\", "/")
        os.chdir(root)
        found = True
        break
if found:    
    with open(abs_file_path, "r") as tar_file:
        with open(os.path.abspath(copy).replace("\\", "/"), "a+") as cp_file:
            ch = tar_file.read(1)
            while ch != "":
                cp_file.write(ch.upper())
                print(str(ch.upper()), end="")
                ch = tar_file.read(1)
    print("\nFile copied successfully.")
else:
    print("File not found...!")
