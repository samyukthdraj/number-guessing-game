## IN LISTS: .append(item)
## IN DICTIONARY: dictionary_name[key]=value
from art import logo
import random

def guessing_game():
    print(logo)
    print("I'M THINKING OF A NUMBER FROM 0-100\n")
    difficulty=input("CHOOSE A DIFFICULTY, 'HARD' OR 'EASY': ").lower()
    number=random.randint(0,100)
    if difficulty=='hard':
        i=5
        while i!=0:
            for i in range(5, 0, -1):
                    print(f"YOU HAVE {i} ATTEMPTS TO GUESS A NUMBER \n")
                    guess=int(input("GUESS A NUMBER: "))
                    if guess==number:
                        print("CORRECT! YOU WIN\n")
                        break
                    elif guess>100:
                        print("PLEASE GUESS A NUMBER BETWEEN 0-100\n")
                    elif guess<number:
                        print("TOO LOW! GUESS HIGHER\n")
                    elif guess>number:
                        print("TOO HIGH! GUESS LOWER\n")
                    else:
                        print("Enter a valid number\n")
            print(f"YOU HAVE NO MORE ATTEMPTS, YOU LOSE THE COMPUTER CHOSE {number}\n")
            break
    if difficulty=='easy':
         i=10
         while i!=0:
            for i in range(10, 0, -1):
                    print(f"YOU HAVE {i} ATTEMPTS TO GUESS A NUMBER \n")
                    guess=int(input("GUESS A NUMBER: "))
                    if guess==number:
                        print("CORRECT! YOU WIN\n")
                        break
                    elif guess>100:
                        print("PLEASE GUESS A NUMBER BETWEEN 0-100\n")
                    elif guess<number:
                        print("TOO LOW! GUESS HIGHER\n")
                    elif guess>number:
                        print("TOO HIGH! GUESS LOWER\n")
                    else:
                        print("Enter a valid number\n")
            print(f"YOU HAVE NO MORE ATTEMPTS, YOU LOSE THE COMPUTER CHOSE {number}\n")
            break
         
guessing_game()
retry=input("DO YOU WANT TO RETRY? 'YES', 'NO': \n").lower()
if retry=='yes':
    guessing_game()
elif retry=='no':
    print("THANK YOU FOR PLAYING NUMBER GUESSING GAME, COME BACK SOON\n")
    exit()