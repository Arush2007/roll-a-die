import random
response = "Y"
while response == "Y":
    number= random.randint(1,6)
    if number==1:
        print("[-----]")
        print("[-----]")
        print("[--0--]")
        print("[-----]")
        print("[-----]")
    if number ==2:
        print("[-----]")
        print("[--0--]")
        print("[-----]")
        print("[--0--]")
        print("[-----]")
    if number==3:
        print("[-----]")
        print("[-----]")
        print("[-000-]")
        print("[-----]")
        print("[-----]")
    if number==4:
        print("[-----]")
        print("[-00--]")
        print("[-----]")
        print("[--00-]")
        print("[-----]")
    if number==5:
        print("[-----]")
        print("[-00--]")
        print("[-0-]")
        print("[--00-]")
        print("[-----]")
    if number==6:
        print("[-----]")
        print("[-000-]")
        print("[-----]")
        print("[-000-]")
        print("[-----]")

    response= input("Press Y to roll again, and press N to exit")
    print("\n")
