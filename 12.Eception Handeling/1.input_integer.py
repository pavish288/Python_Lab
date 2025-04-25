def enterInteger():
    try:
        integer=int(input("Enter an Integer:"))
    except ValueError:
        print("Please enter an integer...!")
        return True
    except:
        print("Unknown Error..!")
        return True
    return False
while enterInteger():
    pass