import random
print("Number Guessing Game")
number = random.randint(1,9)
chance = 0
print("Guess a number between 1 and 9: ")

while chance < 5:
    guess = int(input("Enter your number: "))


    if guess == number:
        print("Congratulations, you won !")
        break
    elif guess < number:
        print("Your guess was too low" )

    else:
        print("Your guess was too high")

    chance = chance + 1

if not chance < 4:
    print("...If ur reading this ur BAKA")
    print("BAKA the number was ", number)
