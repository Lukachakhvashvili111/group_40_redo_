flt = input("enter your float : ")
def fltt(user):
    for i in range(int(user)):
        if i == ".":
            user.cut(".")

print(fltt(flt))