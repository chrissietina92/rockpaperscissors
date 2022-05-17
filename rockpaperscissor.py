import random

#rock paper scissors game
#rock = 1
#paper = 2
#scissors = 3

# rock beats scissors 1 -  3 = - 2
# paper beats rock 2 -  1 = 1
# scissors beats paper 3 - 2 = 1
# scissors looses to rock 3 - 1  = 2
# rock looses to paper 1 - 2 = -1
# paper looses to scissors 2 - 3 = -1

# WIN
#RS = -2
#PR = 1
#SP = 1

#LOOSE
#SR = 2
#RP = -1
#PS = -1

options = {'R' : 1 , 'P' : 2, 'S': 3}
optionList = list(options.items())

def rockpapsci():
    x = input("R/P/S?   ")
    z = options.get(x)
    y = random.choice(optionList)
    u = y[1]
    print(y[0])
    q = z - u
    if q == 0:
        print("It's a draw, try again!")
        rockpapsci()
    else:
        q = z - u
        if q == -2 or q == 1:
            print("You win!")
        else:
            print("You loose!")
        gamerepeat()
        

def gamerepeat():
    repeat = input("Play again Y/N?   ")
    if repeat == "Y":
        print("Amazing! OK..")
        print("3...")
        print("2...")
        print("1")
        rockpapsci()


print("Ready to play rock (R), paper (P), scissors (S)?")
print("3...")
print("2...")
print("1")
rockpapsci()

