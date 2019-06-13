import random
import time
secretNumber = random.randint(1,20)
print('I am thinking of a number between 1 and 20')
guesses = '0'
while int(guesses) < 7:
    guesses = int(guesses) + 1
    print('take a guess')
    guess = input()

    if int(guess) < secretNumber:
        print('too low')
        print('-----------------------------------------------')
    elif int(guess) > secretNumber:
        print('too high')
        print('-----------------------------------------------')
    else:
        break

if int(guess) == int(secretNumber):
    print()
    time.sleep(1)
    print('.', end = '')
    time.sleep(0.5)
    print('.', end = '')
    time.sleep(.5)
    print('.', end = '')
    time.sleep(1)
    print('congratulations, you guessed my number, it was ' + str(secretNumber))
