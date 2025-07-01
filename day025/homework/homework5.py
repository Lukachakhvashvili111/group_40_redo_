name =  input("enter your name : ")
def nn (word):
    final = ""
    for i in name:
        if i in "aeiou":
            continue
        else:
            final += i
    return(final)
print(nn(name))    
    