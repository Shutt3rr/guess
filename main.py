import random

print("I have chosen a random number between 1 and 10. I want you to guess it.")
magic_number = random.randint(1,10)
#print(magic_number)

guess = int(input("What's your lucky guess: "))
if guess == magic_number:
  print(f"you are correct, the number was {magic_number}")
else:
  print(f"You are wrong, the number was {magic_number}")


     
