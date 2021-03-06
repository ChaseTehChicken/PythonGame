### IMPORTS ###

from time import sleep
import winsound
import sys
import subprocess
import colorama

### INSTALL COLORAMA? ###

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


### VARIABLES ###

health = 20
score = 0
kills = 0
level = 0
money = 50
backpack = ['Stick', 'Water Bottle', 'Rock']
StickDamage = 2.5
GreenSlimeDamage = 1
possiblelocations = ['Diner', 'Library', 'Blacksmith']

def gameover():
    if health <= 0:
        for n in range(1, 21):
            print('\n')
        print('\033[1;31;40mGAME OVER')

### GAME ###

install('colorama')
colorama.init()
winsound.PlaySound("startmenu.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
name = input("A new adventurer appears! What is their name?: ")
print(f'\033[0;34;40m Welcome {name}, a great adventure awaits you!')
sleep(2.0)
winsound.PlaySound("snowdin.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
print(f'\033[1;36;40m Welcome to the village travellor!')
sleep(3.0)
print(f'\033[1;36;40mI believe your name was {name} wasnt it?')
sleep(2.0)
print('\033[1;36;40mYes, that was it.')
sleep(1.5)
print('\033[1;36;40mAnyways, welcome to our village')
sleep(2.0)
print('\033[1;36;40mWe have many things to do here')
sleep(2.0)
print('\033[1;36;40mWe have a library, where you can learn magic spells, or just read a novel')
sleep(5.0)
print('\033[1;36;40mWe also have a blacksmith, down by the river. He\'s a crazy guy, ignore most of what he says')
sleep(7.0)
print('\033[1;36;40mTheres also an amazing diner down the road. Family owned and the best food in town.')
sleep(5.0)
print('\033[1;36;40mBecause its the only food in town...')
sleep(5.0)
print('\033[1;36;40mWhy dont you go explore? I\'ll be here until you get back.')
sleep(5.0)
print('\033[1;36;40mOh yeah! My name is Tyke! I live here. Uhh, yeah. OK, you can go explore')
print('\033[1;36;40mWhere do you want to go? Library, Blacksmith, or Diner?\n\033[1;31;40m')

while True:
    location = input("LOCATION: ")
    lowerlocation = location.lower()
    if lowerlocation == 'blacksmith':
        break
    elif lowerlocation == 'library':
        break
    elif lowerlocation == 'diner':
        break
    else:
        print("\033[1;30;40mPLEASE ENTER A VALID LOCATION")

print(f'\033[0;34;40m On your way to the {location}, you stumble across a green slime')
locationUpper = location.capitalize()
sleep(2.0)
print('\033[0;34;40mIt may look friendly, but trust me, the narrator, it isnt.')
sleep(4.0)
print("\033[0;34;40mWhen you stumble across an enemy, you can run, or you can fight.")
sleep(2.0)
print('\033[1;30;40mWhat do you choose to do now?')
while True:
    action = input("RUN OR FIGHT?: ")
    if action == 'fight':
        break
    else:
        print('\033[0;34;40m Sorry you have to fight this one..')
print('\033[0;34;40mHi, narrator again.')
sleep(1.0)
print('\033[0;34;40mYou really think you can fight that thing with your fists??')
sleep(3.0)
print('\033[0;34;40mHA!')
sleep(1.0)
print('\033[0;34;40mYou must first equip a weapon.')
sleep(3.0)
print('\033[0;34;40mI\'m pretty sure I left a stick in your backpack\n\033[1;31;40m')

while True:
    weapon = input('SELECT A WEAPON: ')
    if weapon == 'stick':
        print(f'\033[1;30;40mSELECTED WEAPON IS NOW: {weapon}')
        sleep(3.0)
        print('\033[0;34;40mThats more like it. I\'ll leave you to it')
        sleep(2.0)
        print('\033[1;30;40mTO ATTACK, TYPE attack')
        print('\033[1;30;40mTO DEFEND, TYPE defend')
        print('\033[1;30;40mTO RUN, TYPE run')
        print('\033[1;30;40mTO SHOW MERCY OR SPARE YOUR OPPONENT, TYPE mercy')
        while True:
            action = input('WHAT DO YOU DO?:')
            if action == 'attack':
                break
            else:
                print('\033[0;34;40mSorry, you have to fight this one..')
        winsound.PlaySound('enemyapproaching.wav', winsound.SND_LOOP + winsound.SND_ASYNC)
        GreenSlimeHealth = 5
        print('\033[1;30;40mYOU ATTACKED THE SLIME')
        sleep(1.0)
        GreenSlimeHealth = GreenSlimeHealth - StickDamage
        print(f'\033[1;30;40mGREEN SLIME HEALTH IS NOW {GreenSlimeHealth}')
        sleep(3.0)
        print('\033[1;30;40mGREEN SLIME IS ANGERED')
        sleep(1.0)
        print('\033[1;30;40mGREEN SLIME ATTACKS')
        sleep(1.0)
        print(f'\033[1;30;40mYOU LOSE {GreenSlimeDamage} HEALTH!')
        gameover()
        sleep(2.0)
        health = health - GreenSlimeDamage
        print(f'\033[1;30;40mHEALTH: {health}')
        print('\033[1;30;40mattack, run, mercy')
        action = input('WHAT DO YOU DO?:')
        while True:
            if action == 'attack':
                break
            else:
                print('\033[0;34;40m Sorry, you have to fight this one..')
        print('\033[1;30;40m YOU ATTACKED THE SLIME')
        sleep(1.0)
        GreenSlimeHealth = GreenSlimeHealth - StickDamage
        print(f'\033[1;30;40m GREEN SLIME HEALTH IS NOW {GreenSlimeHealth}')
        print('\033[1;30;40m YOU KILLED THE GREEN SLIME!')
        break
    else:
        print('\033[0;34;40m Sorry, you only have a stick at the moment...')
sleep(3.0)
print('\033[0;34;40m Wow..')
sleep(5.0)
print("\033[0;34;40m I thought you would die there..")
sleep(2.0)
print("\033[0;34;40m Oh well..")
sleep(3.0)
print(f'YOU ARRIVE AT {locationUpper}')
while True:
    if lowerlocation == 'diner':
        print(f"\033[1;31;40m Welcome {name} to the Crapple Diner!")
        sleep(3.0)
        print('\033[1;31;40m My name\'s Shaz')
        print("\033[1;31;40m Would you like somthing to eat?")
        while True:
            eat = input("EAT?: ")
            answer = eat.lower()
            if answer == 'yes':
                print('\033[1;31;40m Awesome!')
                sleep(2.0)
                print('\033[1;31;40m We dont have much at the moment sorry...')
                sleep(2.0)
                print("\033[1;31;40m Would you like some fries?")
                while True:
                    fries = input("EAT?: ")
                    if fries == 'yes':
                        print("\033[1;31;40m Awesome!")
                        sleep(3.0)
                        print("\033[1;31;40m I'll go get them ready!")
                        sleep(2.0)
                        print('\033[0;34;40m Hi. Narrator again')
                        sleep(2.0)
                        
                    if fries == 'no':
                        print("Ok then..")
                        sleep(3.0)
                        print("\033[1;31;40m Enjoy the rest of your day!")
                        break
                    break
            elif answer == 'no':
                break
            else:
                print('\033[1;30;40m PLEASE ANSWER IN A YES OR NO FORM')
    elif lowerlocation == 'library':
        print('Ah, hi Mark.. I was waiting for y-')
        sleep(5.0)
        print('Wait a minute..')
        sleep(2.0)
        print('Youre not Mark..')
        sleep(2.0)
        print('Wait! Are you?..')
        sleep(2.0)
        print('Sorry, excuse me. My name is Debbie..')
        sleep(2.0)
        print('Im not used to having people around here..')
        sleep(3.0)
        print(f'What was your name again? {name}')