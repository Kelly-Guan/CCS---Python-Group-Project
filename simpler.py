import random

print("Hello! Can you guess the number??")

lower = int(input("Wanna pick your lower range? "))

higher = int(input("Wanna pick your higher range? "))

print("The range you picked is between", lower, "and", higher)

random_generated = random.randint(lower, higher)

user_guess = None


while user_guess != random_generated:
  user_guess = int(input("What do you think the number is?? "))
  if user_guess < lower or user_guess > higher:
    print("Error, please put in a number that is between the range you entered.")
  elif user_guess > random_generated:
    print("Incorrect, the number is lower!")
  elif user_guess < random_generated:
    print("Incorrect, the number is higher!")
  else:
    print("Congrats, you guessed the number!")
