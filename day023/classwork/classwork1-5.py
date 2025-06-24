# 1)
text = "hello"
for i in range(len(text)):
    print(text[i], i)

# 2)
my_list = ["a", "b", "c", "d"]
for i in range(len(my_list)):
    print(my_list[i], i)

# 3)
my_list.insert(3, "z")
print(my_list)

# 4)
my_list.append("x")
print(my_list)

# 5)
my_list.pop(3)
print(my_list)
