def is_perfect_square(num):
    if num < 0:
        return False
    root = int(num ** 0.5)
    return root * root == num
