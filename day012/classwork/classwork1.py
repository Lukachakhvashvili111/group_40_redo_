numb = int(input("enter a number"))
def num(number):
    jjj = []
    for i in range(2,number):
        if number % 2 == 0:
            jjj.append(i)
    return jjj
    
print(num(numb))