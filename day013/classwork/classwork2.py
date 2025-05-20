def count_k(word):
    count = 0
    for char in word.lower():
        if char == 'k':
            count += 1
    return count
