
def calc(num1,num2):
    what = int(input("enter 1 for plus, 2 for minus,3 multiply,4 divide "))
    if what == 1:
        return num1 + num2
    if what == 2 and num1 > num2:
        return num1 - num2
    if what == 2 and num1 < num2:
        return num2 - num1
    if what == 3:
        return num1 * num2
    if what == 4:
        return num1 / num2

print(calc(2,4))