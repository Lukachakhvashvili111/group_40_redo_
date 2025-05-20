num1 = int(input("enter the first number : "))
num2 = int(input("enter the seccond number : "))

what = int(input("enter 1 for plus, 2 for minus,3 multiply,4 divide "))
if what == 1:
    print(num1 + num2)
elif what == 2 and num1 > num2:
    print(num1 - num2)
elif what == 2 and num1 < num2:
    print(num2 - num1)
elif what == 3:
    print(num1 * num2)
elif what == 4:
    print(num1 / num2)
