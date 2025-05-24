name = input("Enter your name: ")
age = int(input("Enter your age: "))
my_name = "luka"
my_age = 12

if age > 18:
    if name == my_name:
        print("We have same names and we are adults")
    else:
        print("We don't have same names but we are adults")
elif age < 18:
    if name == my_name:
        print("We have same names but we are not adults")
    else:
        print("We don't have same names and we are not adults")