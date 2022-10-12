import random
# random.randint(1,10)
# random.random()  # 0.234
answer = random.randint(1,10)

print(answer)
if answer == 1:
  print("Yes")
elif answer == 2:
  print("No")
elif answer == 3:
  print("Maybe")
else:
  print("Try again")