import random
from art import logo

print(logo)
print("I'm Thinking NUmber between 1 and 100")

def play():
    number = random.randint(1,100)


    mode=input("Choose a difficulty. Type 'easy' or 'hard':")
    chances=0
    if mode=="easy":
        chances=10
        print(f"You have {chances} attempts remaining to guess the number.")
    else:
        chances = 5
        print(f"You have {chances} attempts remaining to guess the number.")
    win=False
    i=0
    while not win:
        if i<chances:
            guess=int(input("Guess a Number:"))
            if guess<number:
                print("Too Low")
                print(f"You have {chances - (i + 1)} attempts remaining to guess the number.")
                i+=1
            elif guess>number:
                print("Too High")
                print(f"You have {chances - (i + 1)} attempts remaining to guess the number.")
                i+=1
            elif guess==number:
                print(f"you guessed right number:{guess}")
                i+=11
                win=True
        else:
            print(f"You Lose!!! The correct number is {number} ")
            win=True
    replay=input("Play this game again press 'y' , to end press 'n': ")
    if replay=="y":
        play()
    else:
        print("THANK YOU!!!")


play()