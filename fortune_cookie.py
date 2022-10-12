import random

lucky_number = random.randint(1,100)

fortune_number = random.randint(1,3)

fortune_text = ''

if fortune_number == 1:
  fortune_text = f'You will have a great day! Your lucky number is {fortune_number}.'
elif fortune_number == 2:
  fortune_text = f'You will have lots of luck! Your lucky number is {fortune_number}.'
elif fortune_number == 3:
  fortune_text = f'You will meet the love of your life today. Your lucky number is {fortune_number}.'
else:
  fortune_text = f"I'm sorry - your number {lucky_number} is not lucky today. Try again tomorrow."

print(fortune_text)