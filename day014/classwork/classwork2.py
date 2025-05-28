def even_numbers(lst):
    result = []
    for num in lst:
        if num % 2 == 0:
            result.append(num)
    return result

print(even_numbers([1, 2, 3, 4, 5, 6])) 
