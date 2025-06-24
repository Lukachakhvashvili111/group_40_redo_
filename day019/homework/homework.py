def capitalize_sentence(s):
    return s.title()

def filter_strings(lst):
    result = []
    for x in lst:
        if type(x) == str:
            result.append(x)
    return result

def print_letters_with_for(word):
    for l in word:
        print(l)

def print_letters_with_while(word):
    i = 0
    while i < len(word):
        print(word[i])
        i += 1

def odd_squares_sum(n):
    total = 0
    for x in range(1, n+1):
        if x % 2 == 1:
            total += x*x
    return total

def even_indexed_chars(word):
    result = ''
    for i in range(0, len(word), 2):
        result += word[i]
    return result
