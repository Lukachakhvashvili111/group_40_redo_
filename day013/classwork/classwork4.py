def sum_numbers_in_list(mixed_list):
    total = 0
    for item in mixed_list:
        if isinstance(item, (int, float)):
            total += item
    return total

print(sum_numbers_in_list(4,21,2,3,3,12,3,54))