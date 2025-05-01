num = int(input("Enter a number greater than 10: "))

if num <= 10:
    print("The number must be greater than 10.")
else:

    print("Using for loop:")
    for_sum = 0
    for i in range(5, num + 1):
        for_sum += i
    print("Sum:", for_sum)


    print("Using while loop:")
    while_sum = 0
    i = 5
    while i <= num:
        while_sum += i
        i += 1
    print("Sum:", while_sum)