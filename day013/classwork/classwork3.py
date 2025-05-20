def count_strings(lst):
    count = 0
    for item in lst:
        if type(item) == str:
            count += 1
    return count
