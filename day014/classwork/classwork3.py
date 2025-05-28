def letter_indexes(s):
    result = []
    index = 0
    for _ in s:
        result.append(index)
        index += 1
    return result

