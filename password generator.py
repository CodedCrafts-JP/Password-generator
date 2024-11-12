import random
import time

symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]
letters = "qwertyuiopasdfghjklzxcvbnm"
caps_letters = "QWERTYUIOPASDFGHJKLZXCVBNM"
num = "0123456789"

print("Welcome to the strong password generator!")

try:
    number = int(input("Number of characters in your password? "))
    if number <= 0:
        raise ValueError("Number of characters must be positive.")
except ValueError as e:
    print(f"Invalid input: {e}")
    exit()

password = []
x = 0

while x < number:
    options = ["a", "b", "c", "d"]
    way = random.choice(options)

    if way == "a":
        password.append(random.choice(symbols))
    elif way == "b":
        password.append(random.choice(letters))
    elif way == "c":
        password.append(random.choice(caps_letters))
    else:
        password.append(random.choice(num))

    print(f"{x + 1}th letter of your password is generating...")
    time.sleep(0.1)
    x += 1

# Join the list to form the final password string
final_password = ''.join(password)
print("Here")
print(f"Your generated password is: {final_password}")