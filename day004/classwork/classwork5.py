age = 12
name = "luka"
guessed_n = input("guess my name ")
guessed_a = input("guess my age")
while guessed_n != name and int(guessed_a) != age:
    print("Try again!")
    guessed_n = input("guess my name ")
    guessed_a = input("guess my age")
print("Correct!")