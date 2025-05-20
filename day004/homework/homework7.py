correct_password = "1234"
attempts = 3

while attempts > 0:
   password = input("შეიყვანეთ პაროლი: ")
   if password == correct_password:
       print("პაროლი სწორია!")
   else:
       attempts -= 1
       print("არასწორია. დარჩენილი ცდები:", attempts)

if attempts == 0:
  print("შესვლის ცდების ლიმიტი ამოწურულია.")
