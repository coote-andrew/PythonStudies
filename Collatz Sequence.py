#Colatz sequence
print('enter a number')
try:
    Number = (int(input()))
except ValueError:
        print('Please enter a valid integer')

def collatz(inputNumber):
    while inputNumber >= 1:
        print(int(inputNumber))
        if inputNumber % 2 == 0:
            inputNumber /= 2
        elif inputNumber != 1:
            inputNumber = 3* inputNumber + 1
        else:
            break

collatz(Number)
    
