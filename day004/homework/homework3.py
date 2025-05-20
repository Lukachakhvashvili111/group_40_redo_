text = input("შეიყვანეთ სიტყვა: ")
number = int(input("შეიყვანეთ რიცხვი: "))
result = ""

for char in text:
   result += char * number

print("შედეგი:", result)
