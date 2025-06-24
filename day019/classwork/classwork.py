def even_average(n):
    n = int(n)
    evens = list(range(2, n+1, 2))
    if not evens:
        return 0
    return sum(evens) / len(evens)

user_input = input("შეიყვანეთ რიცხვი: ")
print(even_average(user_input))