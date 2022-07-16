# Dragon Realm game 
# Based on the game in the book 
# Invent Your Own Computer Games with Python

import random
import time
import os

dr_title = """

 _______  .______          ___       _______   ______   .__   __.    .______       _______     ___       __      .___  ___. 
|       \ |   _  \        /   \     /  _____| /  __  \  |  \ |  |    |   _  \     |   ____|   /   \     |  |     |   \/   | 
|  .--.  ||  |_)  |      /  ^  \   |  |  __  |  |  |  | |   \|  |    |  |_)  |    |  |__     /  ^  \    |  |     |  \  /  | 
|  |  |  ||      /      /  /_\  \  |  | |_ | |  |  |  | |  . `  |    |      /     |   __|   /  /_\  \   |  |     |  |\/|  | 
|  '--'  ||  |\  \----./  _____  \ |  |__| | |  `--'  | |  |\   |    |  |\  \----.|  |____ /  _____  \  |  `----.|  |  |  | 
|_______/ | _| `._____/__/     \__\ \______|  \______/  |__| \__|    | _| `._____||_______/__/     \__\ |_______||__|  |__| 
                                                                                                                            

"""

def start_game():
    os.system('clear')
    print(dr_title)
    time.sleep(1)

def display_intro():
    print('''
    You are in a land full of dragons. In
    front of you, you see two caves. In one cave, the dragon
    is friendly and will share his treasure with you. The 
    other dragon is greedy and hungry, and will eat you
    on sight.
    ''')
    print("")
    time.sleep(2)

def choose_cave():
    cave = 0
    while cave != 1 and cave != 2:
        cave = input("Which cave will you go into? (1 or 2) ")
        cave = int(cave)
        print("")
    return cave

def check_cave(cave_number):
    print("You approach the cave ...")
    time.sleep(2)
    print("It is dark and spooky ...")
    time.sleep(2)
    print("A large dragon jumps out in front of you!")
    time.sleep(2)
    print("He opens his jaws and ...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)

    friendly_cave = random.randint(1, 2)

    if cave_number == friendly_cave:
        print("Gives you his treasure!")
    else:
        print("Gobbles you down in one bite!")

    print("")


play_again = 'y'

while play_again in ['y', 'yes', 'Y', 'Yes', 'YES']:
    start_game()
    display_intro()
    cave_number = choose_cave()
    check_cave(cave_number)

    play_again = input("Do you want to play again? (yes or no) ")