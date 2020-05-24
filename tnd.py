                                                    ### Making a game ###
#importing data
import string
import Truth_and_dare_dictionary
import random
import string


### Greeting the user ###
print("Hey there,\n welcomr to TRUTH AND DARE")


### Taking Inputs ###
t_or_d=input("BOT: What do you choose? Truth or dare?\nYOU:")
        ###remove whitespace and lowercase the imput###
print(t_or_d.lower)



### Processing the data and interactions ###
def mid_game_function():
    ans=input("YOU:")
    print('lol..XD')

if t_or_d=="truth":
    print("BOT: "+random.choice(Truth_and_dare_dictionary.truth))
    mid_game_function
if t_or_d=="dare":
    print("BOT: "+random.choice(Truth_and_dare_dictionary.dare))
    mid_game_function
else:
    print("BOT: I can't undersatand what you said... I'm made only for truth and dare")
    
                                                    ### Game End Message###
