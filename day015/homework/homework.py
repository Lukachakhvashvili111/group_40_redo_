# 1)
def remove_odd_index_letters(text):
    result = ''
    for i in range(len(text)):
        if i % 2 == 0:
            result = result + text[i]
    return result

# 2)
def remove_odd_numbers_at_odd_indexes(numbers):
    new_list = []
    for i in range(len(numbers)):
        if i % 2 != 0 and numbers[i] % 2 != 0:
            continue
        new_list.append(numbers[i])
    return new_list

# 3) 
def remove_vowels(text):
    vowels = 'aeiouAEIOUაეიოუ'
    result = ''
    for char in text:
        if char not in vowels:
            result = result + char
    return result

# 4)
def letter_at_index():
    text = input("შეიყვანე სტრინგი: ")
    index = int(input("შეიყვანე ინდექსი: "))
    if 0 <= index < len(text):
        print("ასო არის:", text[index])
    else:
        print("არასწორი ინდექსია.")

# 5)
def remove_short_words(words):
    result = []
    for word in words:
        if len(word) >= 5:
            result.append(word)
    return result
