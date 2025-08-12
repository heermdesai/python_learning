import random

high = 10
low = 1
numChance = 10
numGuesses = 0

print("I am thinking of a number between 1 and 10. Try to guess what it is!!!")

num = random.randrange(low, high + 1)
print(num)

while(numGuesses < numChance):
    guess = int(input("Enter your guess: "))
    if (guess == num):
       numGuesses += 1
       print("Correct! You win!")
       break
    else:
      numGuesses += 1
      print("Wrong! Try again!")

if (numGuesses == numChance):
   print("Sorry, you're out of guesses. The number was " + num)