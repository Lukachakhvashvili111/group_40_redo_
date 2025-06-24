num11 = int(input("enter number N1 "))
num22 = int(input("enter number N2 "))
cccc = int(input("enter either:plus,minus,divide,multiply:1,2,3,4 "))
def calc(num1,num2,ccc):
    if ccc == 1:
        return num1 + num2
    elif ccc == 2:
        return num1 - num2
    elif ccc == 3:
        return num1 / num2
    elif ccc == 4:
        return num1 * num2
print(calc(num11,num22,cccc))