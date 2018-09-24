#Krystal Bush
#9/24/18

import random

min = 1
max = 6

def roll_die():
    player = {
        'one':one,
        'two':two,
        'three':three,
        'four':four,
        'five':five,
        'six':six,
        }

def roll_die_opp():
    opponent = {
        'one':one,
        'two':two,
        'three':three,
        'four':four,
        'five':five,
        'six':six,
        }
    
roll_again = input("Would you like to play again? If so, say yes. If not, say no. ")

while True:
    if roll_again == "yes":
        print(roll_die_opp.random(min, max))
        print(roll_die.random(min, max))
    else:
        print("Thank you for playing!")
        break

#When we get the chance, I need to talk to you after class.
#It's nothing serious, I just want to tell you why I've been panicking so much lately.
