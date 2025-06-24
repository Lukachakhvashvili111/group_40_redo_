# 1)
def min_max(numbers):
    if not numbers:
        return None, None
    min_num = numbers[0]
    max_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num
    return min_num, max_num

# 2)
def filter_and_reverse(strings):
    result = []
    for word in strings:
        if len(word) > 6:
            reversed_word = word[::-1].capitalize()
            result.append(reversed_word)
    return result

# 3)
def sentence_to_modified_string(sentence):
    words = sentence.split()
    capitalized_words = []
    for word in words:
        capitalized_words.append(word.capitalize())
    return '@'.join(capitalized_words)

# 4)
def print_odds_for():
    for i in range(1, 101):
        if i % 2 == 1:
            print(i)

def print_odds_while():
    i = 1
    while i <= 100:
        if i % 2 == 1:
            print(i)
        i += 1

# 5)
def print_divisible_for():
    for i in range(1, 51):
        if i % 3 == 0 and i % 5 == 0:
            print(i)

def print_divisible_while():
    i = 1
    while i <= 50:
        if i % 3 == 0 and i % 5 == 0:
            print(i)
        i += 1

# 6)
def print_hello_for():
    for _ in range(100):
        print("hello")

def print_hello_while():
    i = 0
    while i < 100:
        print("hello")
        i += 1

# 7) 
def even_index_average(lst):
    total = 0
    count = 0
    for i in range(0, len(lst), 2):
        total += lst[i]
        count += 1
    if count == 0:
        return 0
    return total / count
