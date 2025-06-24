# 1. თითოეული ასოს დაბეჭდვა სახელებიდან
def print_letters(names):
    for name in names:
        for letter in name:
            print(letter)

# 2. ლუწი რიცხვები ლუწ ინდექსებზე და საშუალო
def even_on_even(nums):
    numbers = []
    for i in range(len(nums)):
        if i % 2 == 0 and nums[i] % 2 == 0:
            numbers.append(nums[i])
    if numbers:
        avg = sum(numbers) / len(numbers)
    else:
        avg = 0
    return numbers, avg

# 3.
#ვერ გავიგე



# 4.
def letter_at_index(name, index):
    if 0 < index <= len(name):
        return name[index - 1]
    return "არასწორი ინდექსი"

# 5.
def slice_from_index(lst, index):
    return lst[index:]

# 6.
def print_2nd_letter_while(name):
    i = 1
    while i < len(name):
        print(name[i])
        i += 2

# 6.
def print_2nd_letter_for(name):
    for i in range(1, len(name), 2):
        print(name[i])

# 7
def password_check(real_password):
    guess = ""
    while guess != real_password:
        guess = input("შეიყვანე პაროლი: ")
    print("სწორია!")
