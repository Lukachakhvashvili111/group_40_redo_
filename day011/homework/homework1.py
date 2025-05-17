def plus(num1,num2):
    return num1 + num2

print(plus(89,76))


def minus(num1,num2):
    if num1 > num2:
        return num1 - num2
    elif num2 > num1:
        return num2 - num1
    else:
        return 0
    
print(minus(4,2))

def multiply (num1,num2):
    return num1 * num2

print(multiply(426,951))

def division (num1,num2):
    if num1 > num2:
        return num1 / num2
    elif num2 > num1:
        return num2 / num1
    
print(division(6,3))