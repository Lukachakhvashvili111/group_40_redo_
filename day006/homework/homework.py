# 1) მონაცემთა ტიპები და მაგალითები:
# String (სტრინგი) - ტექსტური მონაცემები. მაგ: "Hello, World!"
# Integer (ინტეჯერი) - მთელი რიცხვები. მაგ: 42
# Float (ფლოუტი) - ათწილადი რიცხვები. მაგ: 3.14
# Boolean (ბულეანი) - ლოგიკური მნიშვნელობები. მაგ: True, False
# List (ლისტი) - ელემენტების კოლექცია. მაგ: [1, 2, 3]
# Dictionary (დიქშენარი) - გასაღები-მნიშვნელობის წყვილები. მაგ: {"key": "value"}
# Tuple (ტაპლი) - უცვლელი ელემენტების კოლექცია. მაგ: (1, 2, 3)

# 2) მონაცემთა ტიპების გარდაქმნა:
string_var = "123"
integer_var = 456

# String-დან Integer-ში გარდაქმნა
converted_to_int = int(string_var)

# Integer-დან String-ში გარდაქმნა
converted_to_str = str(integer_var)

# 3) მომხმარებლისგან მონაცემების მიღება და გარდაქმნა:
first_name = input("შეიყვანეთ სახელი: ")  # String
last_name = input("შეიყვანეთ გვარი: ")  # String
age = int(input("შეიყვანეთ ასაკი: "))  # Integer
weight = float(input("შეიყვანეთ წონა: "))  # Float

# 4) მატემატიკური და შედარების ოპერატორები:
num1 = 10
num2 = 5

addition = num1 + num2  
subtraction = num1 - num2
multiplication = num1 * num2 
division = num1 / num2
modulus = num1 % num2  
exponentiation = num1 ** num2  
floor_division = num1 // num2  

greater_than = num1 > num2  
less_than = num1 < num2  
equal_to = num1 == num2 
not_equal_to = num1 != num2 
greater_or_equal = num1 >= num2  
less_or_equal = num1 <= num2 

# 5) and და or ოპერატორები:
# and - აბრუნებს True-ს, თუ ორივე პირობა მართალია.
# or - აბრუნებს True-ს, თუ რომელიმე პირობა მართალია.
example_and = (5 > 3) and (2 < 4)  # True
example_or = (5 > 3) or (2 > 4)  # True

# 6) for და while ციკლები 10 სტეპის გამოტოვებით:
for i in range(1, 101, 10):
    print(i)

i = 1
while i < 101:
    print(i)
    i += 10

# 7) for და while ციკლები რიცხვების ჯამის გამოსათვლელად:
sum_for = 0
for i in range(1, 21):
    sum_for += i
print("ჯამი (for):", sum_for)

sum_while = 0
i = 1
while i < 21:
    sum_while += i
    i += 1
print("ჯამი (while):", sum_while)

# 8) მომხმარებლის ასაკის შემოწმება:
age = int(input("შეიყვანეთ თქვენი ასაკი: "))
if age > 30:
    print("ზრდასრული ხარ")
elif age == 30:
    print("შენ ხარ 30 წლის")
else:
    print("კარგი ასაკი გაქვს")