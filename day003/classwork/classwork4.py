string1 = input("Enter the first string: ") 
string2 = input("Enter the second string: ") 
count1 = 0
count2 = 0
for char in string1:
    count1 += 1
for char in string2:
    count2 += 1
print("The number of characters in the first string is: " + str(count1))
print("The number of characters in the second string is: " + str(count2))