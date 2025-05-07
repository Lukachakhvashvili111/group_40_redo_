# 1)
names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
print(names[0]) 
print(names[-1])

# 2) 
names_with_indices = ["Alice", "Bob", "Charlie", "Diana", "Eve"]


# 3)
for name in names_with_indices:
    print(name)

# 4) 
string_var = "konstantinopoli"
for char in string_var:
    print(char)

# 5)
ten_names = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Hank", "Ivy", "Jack"]
print(ten_names[2:8])

# 6)
string_var = "konstantinopoli"
print(string_var[-8:])

# 7) 
fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
countries = ["USA", "Germany", "France", "Italy", "Spain"]
fruits = countries
print(fruits)

# 8)
string_var = "konstantinopoli"
# string_var[-1] = "k"  # This will raise an error because strings are immutable in Python.
# Strings cannot be modified after creation. To change a string, you need to create a new one.

# 9) 
string_var = "kurdgelia"
substring = string_var[4:8]
print(substring)

# 10)
numbers = [10, 5, 20, 40]
print(sum(numbers))