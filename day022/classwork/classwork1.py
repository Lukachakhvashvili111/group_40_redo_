def find_vowels(text):
    vowels = "აეიოუ"
    count = 0
    letters = []

    for letter in text:
        if letter in vowels:
            letters.append(letter)
            count += 1

    return letters, count

v, c = find_vowels("გამარჯობა")
print(v, c)
