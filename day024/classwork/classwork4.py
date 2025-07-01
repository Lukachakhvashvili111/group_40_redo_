straa = "luka is a learning student "
def nen(ww):
    ww.split(" ")
    for i in ww.split(" "):
        if len(i) < 5:
            print("this strings len is lower than 5 ")
        else:
            print ("this strings len is higher than 5, good for u ")
nen(straa)