import random

class Color:
    CBLACK  = '\33[30m'
    CRED    = '\33[31m'
    CGREEN  = '\33[32m'
    CYELLOW = '\33[33m'
    BLUE   = '\33[34m'
    CVIOLET = '\33[35m'
    CBEIGE  = '\33[36m'
    CWHITE  = '\33[37m'

print(Color.CGREEN+"---------------------------- Number Guesser by ILYAS ----------------------------"+Color.BLUE)
while True:
    flag = True
    while flag:
        x = input(Color.BLUE+"Type a number: ")
        if x.isdigit():
            print("Let's play!")
            x = int(x)
            flag= False
        else:
            print(Color.CYELLOW+"Invalid input! Try Again!"+Color.BLUE)
    

    num = random.randint(1, x)
    guess = None

    while guess != num:
        guess = input(Color.BLUE+"guess a number between 1 and "+str(x)+": ")
        guess = int(guess)

        if guess == num:
            print(Color.CGREEN+"congratulations! you won!")
            break
        else:
            print(Color.CRED+"nope, sorry. try again!")

    while True:
        answer = str(input(Color.BLUE+'Run again? (y/n): '))
        if answer in ('y', 'n'):
            break
        print("invalid input.")
    if answer == 'y':
        continue
    else:
        print("Goodbye")
        break
