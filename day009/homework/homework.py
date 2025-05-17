# 1)
car_name = "toyota"
print(car_name.capitalize())


plane_name = "boeing"
print(plane_name.capitalize())

# 2) 
fruit_name = "apple"
print(fruit_name.upper())

# Additional examples
vegetable_name = "carrot"
print(vegetable_name.upper())


# 3)
country_name = "GERMANY"
print(country_name.lower())

# 4)
city_name = "tbilisi"
print(city_name.index("s"))

# Additional examples
city_name_2 = "batumi"
print(city_name_2.index("t"))


# 5)
items = ["ირაკლი", "ბექა", 50, "ატამი", 40.50, "თვითმფრინავი"]
print(items.index("ატამი"))
print(items.index(50))

# Additional examples
items_2 = ["apple", "banana", 100, "cherry", 200.5, "grape"]
print(items_2.index("cherry"))
print(items_2.index(100))

items_3 = ["dog", "cat", 300, "bird", 400.75, "fish"]
print(items_3.index("bird"))
print(items_3.index(300))

# 6) 
names = ["irakli", "beka", "giorgi"]
for i in names:
    print(i)