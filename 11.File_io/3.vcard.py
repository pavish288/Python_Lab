for i in range(0,100):
    contact = {"NAME": "", "PHONE": 0}
    contact["NAME"] = input("Enter name(Enter q for exit): ").strip()
    if contact["NAME"]=="q" or contact["NAME"]=="Q":
        break
    contact["PHONE"] = input("Enter phone number: ").strip()
    with open(f"{i}.vcf", "w") as f:
        f.write("BEGIN:VCARD\n")
        f.write("VERSION:4.0\n")
        f.write(f"FN:{contact['NAME']}\n")
        f.write(f"TEL;TYPE=CELL:{contact['PHONE']}\n")
        f.write("END:VCARD\n")
    print(f"vCard saved as {i}.vcf")