from random import randint
from os import system as s
from time import sleep
lb = 1
ub = 50
chance = 5
#Computer Guess
computer_guess = randint(lb,ub)
#Valid Input Taker
def valid_in(st,ty=str):
    while True:
        print("")
        try:
            s = ty(input(f"{st} : ".center(30," ")))
            if s:
                #Emergency Exit Input  
                if s == 7230 or s == '7230':
                    system('cls')
                    print("\n\n","Emergency Exit...".center(100," "),"\n\n")
                    exit()
                else:
                    return s
                    break
            else:
                print("\n","Blank Input!!   Try Agian...".center(60," "))
        except Exception:
            print("\n","You entered an invalid value...".center(60," "))

for i in range(chance):
    sleep(1)
    s('cls')
    print("\n","__"*50,sep="\n")
    print(""" 
                     ______   __    ___    _______     _____    __      __  _______
                    |   _  \ |  |  /  /   /  ___  \   /  _  \  |  \    /  ||   ____|
                    |  | |  ||  | /  /   /  |   |__| /  / \  \ |   \  /   ||  |__
                    |  |_|  ||  |/  /    |  |  ____ |  /   \  ||    \/    ||   __|
                    |   ___/ |     \     |  | |_   ||  |___|  ||  |\  /|  ||  |
                    |  |     |  |\  \    \  \___|  ||   ___   ||  | \/ |  ||  |____
                    |__|     |__| \__\    \_______/ |__|   |__||__|    |__||_______|
         """)
    print("__"*50,"\n")
    print(f"You have {chance-i} chances to guess correctly".center(100," "),end="\n")
    print("_".center(100,"_"),end="\n\n")
    user_guess = valid_in(f"Enter guess a random number between [{lb}--{ub}] ",int)
    print("\n")
    if user_guess not in range(lb,ub): 
        print(f"Plese guess in limit {lb}--{ub} and do not reduce chances".center(100," "),"\n")
        continue
    if user_guess == computer_guess:
        print("You such a master !! You won the game...".center(100," "))
        print("_".center(100,"_"))
        break
    elif user_guess > computer_guess:
        print(f"your guess is high please think a low number".center(100," "))
        ub = user_guess
    elif user_guess < computer_guess:
        print("your guess is low please think a high".center(100," "))
        lb = user_guess
    print("\n")
else :
    print("_".center(100,"_"),"\n")
    print(f"Computer Guess is : {computer_guess}".center(100," "),"shame.... you such a looser ".center(100," "),sep="\n\n")
    print("_".center(100,"_"))
ch = int(valid_in("Want to Play Agian...  Press 1 "))
print("_".center(100,"_"))
if ch:
    s('python guess_game.py')
else:
    exit()
