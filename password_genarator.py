#Python 3.9.13

import random
import os

low_case = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
upper_case = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
symbols = ["!",'"',"£","$","%","^","&","*","(",")","_","-","+","=","{","}","[","]",";",":","'","@","#","~","<",">",",",".","/","?","|"]

password = ""

no_repeats = True

print("hi")

amountoftimes = random.randint(1,999999) # Yes you read those 9's correctly

def scrambled(orig):
    dest = orig[:]
    random.shuffle(dest)
    return dest

low_case = scrambled(low_case)
upper_case = scrambled(upper_case)
symbols = scrambled(symbols)

#Get a lowercase character

def lowercase(low_case):
    global amountoftimes
    times = 0
    while times < amountoftimes:
        times += random.randint(1,5)
        character = random.choice(low_case)
    return character

#Get a uppercase character

def uppercase(upper_case):
    global amountoftimes
    times = 0
    while times < amountoftimes:
        times += random.randint(1,5)
        character = random.choice(upper_case)
    return character

#Get a lowercase character

def symbolspick(symbols):
    global amountoftimes
    times = 0
    while times < amountoftimes:
        times += random.randint(1,5)
        character = random.choice(symbols)
    return character

#Clear the console.

def clearconsole():
    os.system('cls')


while True:
    clearconsole()
    password = ""

    #Introduction

    print("Welcome to my password generator. (12 characters)")
    print("In a second you will be asked for options on your new password:\n - How random you would like it\n - If you want repeating numbers")
    print("\nPress Enter when your ready.")
    input()
    clearconsole()

    #Randominese

    print("How random do you want your password to be?\n(1) Not really ~ few seconds to generate\n(2) Medium ~ 10-30 seconds to genorate\n(3) Insane Random ~ 1-3 mins to genorate. \n")
    while True:
        option = int(input("- "))
        if option == 1 or option == 2 or option == 3:
            break
        else:
            print("Error - Please type either 1 or 2 or 3")
    if option == 1:
        amountoftimes = 999
    elif option == 2:
        amountoftimes = 999999
    elif option == 3:
        amountoftimes = 11111111
    clearconsole()

    #Repeating Numbers?

    print("Do you want repeating numbers?\n(1) No\n(2) Yes")
    while True:
        option = int(input("- "))
        if option == 1 or option == 2 or option == 3:
            break
        else:
            print("Error - Please type either 1 or 2")
    if option == 1:
        no_repeats = True
    elif option == 2:
        no_repeats = False

    #Actually making the passwords
    clearconsole()
    print("Password is being made...")
    while password.__len__() < 16:
        times = 0
        while times < amountoftimes:
            times = times + random.randint(1,5)
            option = random.randint(1,4)
        
        if option == 1:
            character = lowercase(low_case)
            password = password + character
            if no_repeats == True:
                low_case.remove(character)
        
        elif option == 2:
            character = uppercase(upper_case)
            password = password + character
            if no_repeats == True:
                upper_case.remove(character)
        
        elif option == 3:
            character = symbolspick(symbols)
            password = password + character
            if no_repeats == True:
                symbols.remove(character)
        
        print (password)

        low_case = scrambled(low_case)
        upper_case = scrambled(upper_case)
        symbols = scrambled(symbols)
    clearconsole()
    print(f"Your new password is {password}")
    print("Press enter to start again...")
    input()
print(password)