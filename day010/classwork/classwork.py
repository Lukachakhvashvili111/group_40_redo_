
names = ["Ana", "Luka", "Nino"]

names.append("Banana")
names.append("Apple")
names.append("ფორთოხალი")

print("Updated list (Part 1):", names)



names_list = ["Ana", "Luka", "Nino", "Saba", "Tina", "Giorgi", "Mariam"]


names_list.insert(3, "mtvare")


names_list.insert(5, 65)

print("Updated list (Part 2):", names_list)



# Task 3
mixed_list = [1, "hello", 3.14, True]
mixed_list.pop(2) 
mixed_list.pop(-1) 
print(mixed_list)

# Task 4
names_and_number = ["giorgi", "lasha", "beqa", "irakli", 45]
names_and_number.remove("lasha")
names_and_number.remove(45)  
print(names_and_number)

# Task 5
# The pop() function removes an element by its index and returns the removed element.
# The remove() function removes the first occurrence of a specified value but does not return it.