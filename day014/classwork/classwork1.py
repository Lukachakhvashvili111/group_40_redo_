
def odd_index_letters(s):
    result = ""
    for i in range(len(s)):
        if i % 2 == 1:
            result += s[i]
        return result
