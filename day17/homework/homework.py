# 1)
def count_unique_letters(word):
    unique = []
    for char in word:
        if char not in unique:
            unique.append(char)
    return len(unique)

# 2) 
def print_letters_loops(word):
    print("for loop:")
    for char in word:
        print(char)
    
    print("while loop:")
    i = 0
    while i < len(word):
        print(word[i])
        i += 1

# 3) 
def split_float(number):
    whole = int(number)
    fractional = round(number - whole, 10)  
    return f"{whole} + {fractional} = {number}"

# 4)
def find_max(numbers):
    if not numbers:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

# BONUS)
import random

def jairani_game():
    options = ["ქვა", "მაკრატელი", "ქაღალდი"]
    lose_count = 0

    while lose_count < 3:
        player = input("შეიყვანე (ქვა, ქაღალდი, მაკრატელი): ")
        computer = random.choice(options)
        print("კომპიუტერი აირჩია:", computer)

        if player == computer:
            print("ფრეა!\n")
        elif (player == "ქვა" and computer == "მაკრატელი") or \
             (player == "მაკრატელი" and computer == "ქაღალდი") or \
             (player == "ქაღალდი" and computer == "ქვა"):
            print("მოიგე!\n")
        else:
            print("წააგე!\n")
            lose_count += 1
    
    print("თამაში დასრულდა. სამჯერ წააგე.")


