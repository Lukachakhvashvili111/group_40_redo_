# 2) Factorial
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

# 3) Multiplication Table
def multiplication_table(n):
    table = []
    for i in range(1, n + 1):
        row = []
        for j in range(1, n + 1):
            row.append(i * j)
        table.append(row)
    return table

# 4) Hide String
def hide_string(s):
    return '*' * len(s)

# 5) Split Number into Parts
def split_number(n):
    s = str(n)
    parts = []
    for i in range(len(s)):
        if s[i] != '0':
            zeros = len(s) - i - 1
            parts.append(s[i] + '0' * zeros)
    return ' + '.join(parts)
