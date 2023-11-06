
# imports for the game

# import time
# import os
import random
import sys
from print_statements import *
from gameplay import fast_print, slow_print, slower_print, clear_screen

# Global variables for the game
PLAYER_NAME = ""
WEAPON_TYPE = []

def main():
    """
    This is the main function that will run the program
    """
    clear_screen()
    print(r""" 
████████╗ ██████╗ ███╗   ███╗██████╗ ██╗    ██╗ ██████╗ ██████╗ ██╗   ██████╗     
╚══██╔══╝██╔═══██╗████╗ ████║██╔══██╗██║    ██║██╔═══██╗██╔══██╗██║   ██╔══██╗    
   ██║   ██║   ██║██╔████╔██║██████╔╝██║ █╗ ██║██║   ██║██████╔╝██║   ██║  ██║    
   ██║   ██║   ██║██║╚██╔╝██║██╔══██╗██║███╗██║██║   ██║██╔══██╗██║   ██║  ██║    
   ██║   ╚██████╔╝██║ ╚═╝ ██║██████╔╝╚███╔███╔╝╚██████╔╝██║  ██║█████╗██████╔╝    
   ╚═╝    ╚═════╝ ╚═╝     ╚═╝╚═════╝  ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚════╝╚═════╝     
                                                                                    
 █████╗ ██████╗ ██╗   ██╗███████╗███╗   ██╗████████╗██╗   ██╗██████╗ ███████╗       
██╔══██╗██╔══██╗██║   ██║██╔════╝████╗  ██║╚══██╔══╝██║   ██║██╔══██╗██╔════╝       
███████║██║  ██║██║   ██║█████╗  ██╔██╗ ██║   ██║   ██║   ██║██████╔╝█████╗         
██╔══██║██║  ██║╚██╗ ██╔╝██╔══╝  ██║╚██╗██║   ██║   ██║   ██║██╔══██╗██╔══╝         
██║  ██║██████╔╝ ╚████╔╝ ███████╗██║ ╚████║   ██║   ╚██████╔╝██║  ██║███████╗       
╚═╝  ╚═╝╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝       
                                                                                                                                                                                                                                                                                       
""")
    slow_print(story_main()) # Print the main story from print_statements.py
    global PLAYER_NAME
    while True:
        PLAYER_NAME = input("What is your name? \n") # Ask the player for their name
        if PLAYER_NAME.isalpha():
            slower_print(f"Welcome, {PLAYER_NAME}.")
            while True:
                # Ask the player if they are ready to play
                game_input = input("Are you ready to escape? (y/n) \n")
                if game_input == "y":
                    room_intro()
                elif game_input == "n":
                    print("Until next time.")
                    sys.exit()
                else:
                    print("Please enter a valid command.")
        else:
            print("Please enter a valid name with only alphabetical characters.")


def room_intro():
    """
    Room 1 function and options
    """
    clear_screen()
    slow_print(story_intro()) # Print the intro from print_statements.py
    slower_print(
r"""
Options:
1. Look around
2. Move forward
"""
        )
    routes = ["1", "2"]
    user_input = ""

    while user_input not in routes:
        user_input = input("What do you do? \n") # Ask the player what they want to do
        if user_input == "1":
            hieroglyphs_1()
        elif user_input == "2":
            room_1()
        else:
            print("I don't understand that command, try another one.")

def room_1():
    """
    Room 1 function and options
    """
    clear_screen()
    slow_print(story_room_1()) # Print the room 1 from print_statements.py
    slower_print(
r"""
Options:
1. Move Right
2. Move Forward
"""
        )
    routes = ["1", "2"]
    user_input = ""

    while user_input not in routes:
        user_input = input("What do you do? \n") # Ask the player what they want to do
        if user_input == "1":
            death_room_1()
        elif user_input == "2":
            room_2()
        else:
            print("I don't understand that command, try another one.")


def room_2():
    """
    Room 2 function and options
    """
    clear_screen()
    slow_print(story_room_2()) # Print the room 2 from print_statements.py
    slower_print(
r"""
Options:
1. Move back
2. Move left
3. Move forward
"""
        )
    routes = ["1", "2", "3"]
    user_input = ""

    while user_input not in routes:
        user_input = input("What do you do? \n") # Ask the player what they want to do
        if user_input == "1":
            room_1()
        elif user_input == "2":
            room_3()
        elif user_input == "3":
            room_5()
        else:
            print("I don't understand that command, try another one.")

def room_3():
    """
    Room 3 weapon room function and options
    """
    clear_screen()
    slow_print(story_room_3()) # Print the room 3 from print_statements.py
    slower_print(
r"""
Options:
1. Look around
2. Move back
3. Move right
"""
        )
    routes = ["1", "2", "3"]
    user_input = ""

    while user_input not in routes:
        user_input = input("What do you do? \n") # Ask the player what they want to do
        if user_input == "1":
            weapon_1()
        elif user_input == "2":
            room_2()
        elif user_input == "3":
            room_4()
        else:
            print("I don't understand that command, try another one.")

def room_4():
    """
    Room 4 monster room function and options
    """
    clear_screen()
    slow_print(story_room_4()) # Print the room 4 from print_statements.py
    slower_print(
r"""
Options:
1. Run back
2. Stand and fight
"""
        )
    routes = ["1", "2"]
    user_input = ""

    while user_input not in routes:
        user_input = input("What do you do? \n") # Ask the player what they want to do
        if user_input == "1":
            room_3()
        elif user_input == "2":
            fight_1()
        else:
            print("I don't understand that command, try another one.")

def room_5():
    """
    Room 5 function and options
    """
    clear_screen()
    slow_print(story_room_5()) # Print the room 5 from print_statements.py
    slower_print(
r"""
Options:
1. Look Around
2. Move back
3. Move right
4. Move forward
"""
        )
    routes = ["1", "2", "3", "4"]
    user_input = ""

    while user_input not in routes:
        user_input = input("What do you do? \n") # Ask the player what they want to do
        if user_input == "1":
            hieroglyphs_2()
        elif user_input == "2":
            room_2()
        elif user_input == "3":
            room_6()
        elif user_input == "4":
            death_room_2()
        else:
            print("I don't understand that command, try another one.")

def room_6():
    """
    Room 6 function and options
    """
    clear_screen()
    slow_print(story_room_6()) # Print the room 6 from print_statements.py
    slower_print(
r"""
Options:
1. Look Around
2. Move back
3. Move right
"""
        )
    routes = ["1", "2", "3"]
    user_input = ""

    while user_input not in routes:
        user_input = input("What do you do? \n") # Ask the player what they want to do
        if user_input == "1":
            weapon_2()
        elif user_input == "2":
            room_5()
        elif user_input == "3":
            room_7()
        else:
            print("I don't understand that command, try another one.")

def room_7():
    """
    Room 7 monster room function and options
    """
    clear_screen()
    slow_print(story_room_7()) # Print the room 7 from print_statements.py
    slower_print(
r"""
Options:
1. Run back
2. Stand and fight
"""
        )
    routes = ["1", "2"]
    user_input = ""

    while user_input not in routes:
        user_input = input("What do you do? \n") # Ask the player what they want to do
        if user_input == "1":
            room_6()
        elif user_input == "2":
            fight_2()
        else:
            print("I don't understand that command, try another one.")

def room_7_continue():
    """
    Room 7 continued function and options
    """
    clear_screen()
    slow_print(story_room_7_continue()) # Print the room 7 continued from print_statements.py
    slower_print(
r"""
Options:
1. Move forward
2. Move left
"""
        )
    routes = ["1", "2"]
    user_input = ""

    while user_input not in routes:
        user_input = input("What do you do? \n") # Ask the player what they want to do
        if user_input == "1":
            death_room_1()
        elif user_input == "2":
            exit_scene()
        else:
            print("I don't understand that command, try another one.")


def death_room_1():
    """
    Death 1 room function
    """
    clear_screen()
    slow_print(story_death_room_1()) # Print the death room 1 from print_statements.py
    death_scene()

def death_room_2():
    """
    Death 2 room function
    """
    clear_screen()
    slow_print(story_death_room_2()) # Print the death room 2 from print_statements.py
    death_scene()



def weapon_1():
    """
    Function for Mining Laser
    """
    clear_screen()
    slow_print(story_weapon_1()) # Print the weapon 1 from print_statements.py
    global WEAPON_TYPE
    WEAPON_TYPE.append("Mining Laser")
    input("Press enter to continue\n") # Wait for the player to press Enter
    room_3()

def weapon_2():
    """
    Function for Shovel
    """
    clear_screen()
    slow_print(story_weapon_2()) # Print the weapon 2 from print_statements.py
    global WEAPON_TYPE
    WEAPON_TYPE.append("Shovel")
    input("Press enter to continue\n") # Wait for the player to press Enter
    room_6()

def fight_1():
    """
    Function for fighting
    """
    clear_screen()
    slow_print(story_fight_1()) # Print the fight 1 from print_statements.py
    input("Press enter to continue\n") # Wait for the player to press Enter
    scarab_health = 3
    player_health = 10

    while scarab_health > 0 and player_health > 0:
        if "Mining Laser" in WEAPON_TYPE:
            input("Press Enter to take a shot.\n")  # Wait for the player to press Enter

            # Generate a random number between 1 and 6
            random_hit = random.randint(1, 6)

            if random_hit >= 3:
                scarab_health -= 1
                print(
f"""
You rolled a {random_hit} and hit the enemy!
They have {scarab_health} health left.
"""
                )
            else:
                player_health -= 1
                print(
f"""
Your attack missed with a {random_hit},
the scarabs attack you and you have {player_health} health left.
"""
                )
        else:
            print(wrong_weapon())
            input("Press Enter to continue\n") # Wait for the player to press Enter
            room_3()
            break
    else:
        if player_health <= 0:
            print("You have been defeated. Game over.\n")
            input("Press Enter to continue") # Wait for the player to press Enter
            death_scene()

        elif scarab_health <= 0:
            print("You defeated the scarabs. You win!\n")
            input("Press Enter to continue") # Wait for the player to press Enter
            exit_scene()

def fight_2():
    """
    Function for fighting 2
    """
    clear_screen()
    slow_print(story_fight_2()) # Print the fight 2 from print_statements.py
    input("Press enter to continue\n") # Wait for the player to press Enter
    warrior_health = 4
    player_health = 10

    while warrior_health > 0 and player_health > 0:
        if "Shovel" in WEAPON_TYPE:
            input("Press Enter to take a shot.\n")  # Wait for the player to press Enter

            # Generate a random number between 1 and 6
            random_hit = random.randint(1, 6)

            if random_hit >= 4:
                warrior_health -= 1
                print(
f"""
You rolled a {random_hit} and hit the enemy!
They have {warrior_health} health left.
"""
                )
            else:
                player_health -= 1
                print(
f"""
Your attack missed with a {random_hit},
the warrior attacks you and you have {player_health} health left.
"""
                )
        else:
            print(wrong_weapon())
            input("Press Enter to continue\n") # Wait for the player to press Enter
            room_6()
            break
    else:
        if player_health <= 0:
            print("You have been defeated. Game over.")
            input("Press Enter to continue\n") # Wait for the player to press Enter
            death_scene()

        elif warrior_health <= 0:
            print("You defeated the Warrior. You win!")
            input("Press Enter to continue\n") # Wait for the player to press Enter
            room_7_continue()

def exit_scene():
    """
    Exit scene function
    """
    clear_screen()
    slow_print(story_exit_scene()) # Print the exit scene from print_statements.py
    death_scene()

def hieroglyphs_1():
    """
    Function for hieroglyphs option 1
    """
    clear_screen()
    slow_print(story_hieroglyphs()) # Print the hieroglyphs from print_statements.py
    fast_print(story_hieroglyphs_1()) # Print the hieroglyphs 1 from print_statements.py
    # Wait for the player to press Enter
    input("Press enter to continue and move into the room ahead\n")
    room_1()

def hieroglyphs_2():
    """
    Function for hieroglyphs option 2
    """
    clear_screen()
    slow_print(story_hieroglyphs()) # Print the hieroglyphs from print_statements.py
    fast_print(story_hieroglyphs_2()) # Print the hieroglyphs 2 from print_statements.py
    input("Press enter to continue from the room you are in\n") # Wait for the player to press Enter
    room_5()



main()
