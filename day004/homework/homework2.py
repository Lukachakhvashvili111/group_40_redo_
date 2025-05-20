print("კვადრატების ჯამი:")
num = int(input("შეიყვანეთ რიცხვი: "))
limit = num ** 2
total = 0
i = num

while i <= limit:
   total += i
   i += 1

print("ჯამი:", total)
