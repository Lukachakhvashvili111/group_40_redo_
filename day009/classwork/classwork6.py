numbers_list = [1, 2, 3, 4, 5, 6, 7, 8]

even_sum = 0  

for i in numbers_list:
    print(i)
    if i % 2 == 0:
        even_sum += i  
print(even_sum)