#This game will help demonstrate the use of random numbers and loops

import random
#This will allow us to import code to generate random numbers

guesses = 0

print('Welcome to the guessing game, what is your name?')
yourname = raw_input()
#Now we will prompt for input for your name

rn_number = random.randint(1,100)
#We are now generating a random number from 1- 100 using the import random

#Now we will begin out loop to guess until the user is out of guesses
while guesses < 10:
    print('Guess a number from 1 to 100')
    guess = input()
    guess = int(guess)
    #Now we check that it is an integer

    guesses = guesses + 1
    # This is our counter to add guess tries

    if guess < rn_number:
        print('Your guess is too low')

    if guess > rn_number:
        print('Your guess is too high')

    if guess == rn_number:
        break
        #We have a break here in order to stop the program after the loop runs 10 times

if guess == rn_number:
    guesses = str(guesses)
    #Print a the number of guesses taken
    print('Great job,' + yourname + '. You guessed my number in ' + guesses + ' guesses')

#This happens at the end of the game, pay attention to the indentation

if guess != rn_number:
    rn_number = str(rn_number)
    print('You did not guess correctly, I was thinking of the number' + rn_number)
