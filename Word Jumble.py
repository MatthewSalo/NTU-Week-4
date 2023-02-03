# Importing relevant modules

import math
import time
import random

# Defining the word list and jmbled_word
word_list = ['tiger', 'elephant', 'hippo', 'rabbit', 'ostrich', 'hyena']
jmbled_word = ''

# defining a function which encapsulates the game
def jumble_word_game():
    score = 0 # need to declare the score variable outside the for loop
    for word in word_list.copy(): # for loop which iterates through each word in word_list
        chosen_word = random.choice(word_list) # pick out a random word from word_list

        # randomly shuffles the chosen word
        # then using ''.join to join the characters back together into a single string
        jumbled_word = ''.join(random.sample(chosen_word, len(chosen_word)))
        print(jumbled_word)
        time.sleep(1) # making the program sleep for 1 sec using time module, makes it more authentic
        answer2 = input("Can you guess what the above word is? ")
        time.sleep(1)

        if answer2.lower() == chosen_word:
            print("Well done! You got that right :)")
            time.sleep(1)
            score += 1
        else:
            print("Sorry, that was incorrect. Better luck next time!")
            time.sleep(1)
        # removing chosen word from word_list as I don't want the program to select 2 of the same words
        word_list.remove(chosen_word)

    # {} and .format() allow me to input a variable within a print() statement
    print("\nNice, you got {} questions right!".format(score))

# The game begins with a question
answer = input('Do you want to play the word jumble game? ')
if answer.lower() == 'yes':
    time.sleep(1)
    jumble_word_game() # calling the function jumble_word_game
else:
    print("That's okay, I'll go back to sleep.")

