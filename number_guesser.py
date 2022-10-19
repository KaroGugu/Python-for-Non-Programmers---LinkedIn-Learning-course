import random
import time

print("Hi! Welcome to the guessing game. I'll pick a number between 1 and 100. Can you guess it?")
time.sleep(2)
print("Wait while I pick a number...")
time.sleep(1.5)

client_number = int(input("I'm ready. So what is your number guess?: "))
correct_number = random.randint(1, 100)
guess_counter = 0

while client_number != correct_number:
    time.sleep(0.5)
    guess_counter += 1
    if client_number < correct_number:
        print("Opps too low!")
    else:
        print("Opps too high!")
    client_number = int(input("Please try again: "))

print(f"Congrats - you got the right number on the {guess_counter + 1} try!")

