import random

def is_int(x): #function is_int checks if user input is an integer 
    while x.isdigit() == False: #keeps running loop until the user inputs a integer
        x = input("Error. Only integers are allowed. Try again: ")
    return int(x) 


range = False #range is set to False, when range is set to True; this loop stops 
while range == False:
    user_rangeLow = is_int(input("Please enter the lower end of the range: "))
    user_rangeHigh = is_int(input("Please enter the higher end of the range: "))
    
    if user_rangeLow > user_rangeHigh:
        print("Range is invalid, the upper bound must be larger than the lower bound!")
    elif user_rangeLow == user_rangeHigh:
        print("Range is invalid, range is equal to 0!")
    else:
        range = True

random_Int = random.randint(user_rangeLow, user_rangeHigh) #computer randomly guesses a number inbetween (x, y) 
print(random_Int)

print("Your range is from", user_rangeLow , "to" , user_rangeHigh)

trials = 0
user_guess = None

while user_guess != random_Int:
  while trials < 3:
    user_guess = is_int(input("Please guess a number inbetween your range:"))
    trials += 1 
    if user_guess < user_rangeLow or user_guess > user_rangeHigh:
      print("Your guess is not inbetween the range")
    elif user_guess > random_Int:
        print("Incorrect. The number is higher")
    elif user_guess < random_Int:
        print("Incorrect. The number is lower")
    else: 
        print("Congratulations! You guessed the number")
        break
  break
    
