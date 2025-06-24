# Return only letters at odd positions (1, 3, 5...)
def get_odd_letters(text):
    return text[1::2]

# Return only even numbers from the list
def get_even_numbers(numbers):
    result = []
    for num in numbers:
        if num % 2 == 0:
            result.append(num)
    return result

# Return list of index numbers for each letter in a string
def get_letter_indices(text):
    return list(range(len(text)))

# Return list of index numbers for each item in a list
def get_element_indices(items):
    return list(range(len(items)))

# Same as get_even_numbers, just different name
def remove_odd_numbers(numbers):
    evens = []
    for n in numbers:
        if n % 2 == 0:
            evens.append(n)
    return evens
