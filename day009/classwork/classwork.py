# 1)
name_lowercase = "giorgi"
name_capitalized = name_lowercase.capitalize()
print(name_capitalized)

# 2) 
name_uppercase = name_lowercase.upper()
print(name_uppercase)

# 3) 
name_all_caps = "GIORGI"
name_lowercase_again = name_all_caps.lower()
print(name_lowercase_again)

# 4)
surname = "suxitashvili"
index_of_l = surname.index("l")
print(index_of_l)

# 5)
names_list = ["giorgi", "lasha", "beqa", "aleqsandre", 5]
index_of_aleqsandre = names_list.index("aleqsandre")
print(index_of_aleqsandre)

# 6) 
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8]

even_sum = 0  

for i in numbers_list:
    print(i)
    if i % 2 == 0:
        even_sum += i  
print(even_sum)