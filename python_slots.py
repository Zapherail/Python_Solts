#importing random
import random

#Choices for slot game
symbols = ['🍉', '🍒', '🍇', '7️⃣']

#Starting game
def welcome():
    print("Hello Welcome to Python slot machine")
    print("First roll is Free")
    play()

#printing results
def play():
    while True:
        result1 = roll()
        result2 = roll()
        result3 = roll()
        print(result1, '|', result2, '|', result3)
        if result1 == '7️⃣' and result2 == '7️⃣' and result3 == '7️⃣':
            print("Jackpot!!!")

        choice = input("Would you like to play again? y/n: ")
        if choice.lower() == 'n':
            break

#roll function
def roll():
    results = random.choice(symbols)
    return results

welcome()
