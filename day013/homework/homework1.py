srang = input(" enter any string : ")

def idk(user):
    result = ""
    for i in user:
        if i.lower in "aeiou":
            result += "!"
        elif i in "qwertypsdfghjklzxcvbnm":
            result += "+"
        else:
            result ("i dont know what to do now :(")
        return result


print(idk(srang))