"""
This is the main file for the game
"""

# Importing modules
import random
import sys
from game_stories import (
    story_main,
    story_intro,
    story_room_1,
    story_room_2,
    story_room_3,
    story_room_4,
    story_room_5,
    story_room_6,
    story_room_7,
    story_room_7_continue,
    story_death_room_1,
    story_death_room_2,
    story_weapon_1,
    story_weapon_2,
    story_fight_1,
    story_fight_2,
    story_exit_scene,
    story_hieroglyphs,
    story_hieroglyphs_1,
    story_hieroglyphs_2,
    wrong_weapon,
)

from gameplay import (
    fast_print,
    slow_print,
    slower_print,
    clear_screen
)

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
    slow_print(story_main())  # Print the main story in game_stories.py
    global PLAYER_NAME
    while True:
        PLAYER_NAME = input("What is your name? \n")  # Player input for name
        if PLAYER_NAME.isalpha():
            slower_print(f"Welcome, {PLAYER_NAME}.\n")
            while True:
                game_input = input("Are you ready to escape? (y/n) \n")
                if game_input.lower() == "y":
                    room_intro()
                elif game_input.lower() == "n":
                    print("Until next time.")
                    sys.exit()
                else:
                    print("Please Enter a valid command.")
        else:
            print("Please Enter a valid name with only"
                  "alphabetical characters.")


def room_intro():
    """
    Room 1 function and options
    """
    clear_screen()
    slow_print(story_intro())  # Print story in game_stories.py
    slower_print(r"""
Options:
1. Look around
2. Move forward
""")
    routes = ["1", "2"]
    user_input = ""

    while user_input not in routes:
        # Player input
        user_input = input("What do you do? \n")
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
    slow_print(story_room_1())  # Print story in game_stories.py
    slower_print(r"""
Options:
1. Move Right
2. Move Forward
""")
    routes = ["1", "2"]
    user_input = ""

    while user_input not in routes:
        user_input = input("What do you do? \n")  # Player input
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
    slow_print(story_room_2())  # Print story in game_stories.py
    slower_print(r"""
Options:
1. Move back
2. Move left
3. Move forward
""")
    routes = ["1", "2", "3"]
    user_input = ""

    while user_input not in routes:
        user_input = input("What do you do? \n")  # Player input
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
    slow_print(story_room_3())  # Print story in game_stories.py
    slower_print(r"""
Options:
1. Look around
2. Move back
3. Move right
""")
    routes = ["1", "2", "3"]
    user_input = ""

    while user_input not in routes:
        user_input = input("What do you do? \n")  # Player input
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
    slow_print(story_room_4())  # Print story in game_stories.py
    slower_print(r"""
Options:
1. Run back
2. Stand and fight
""")
    routes = ["1", "2"]
    user_input = ""

    while user_input not in routes:
        user_input = input("What do you do? \n")  # Player input
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
    slow_print(story_room_5())  # Print story in game_stories.py
    slower_print(r"""
Options:
1. Look Around
2. Move back
3. Move right
4. Move forward
""")
    routes = ["1", "2", "3", "4"]
    user_input = ""

    while user_input not in routes:
        user_input = input("What do you do? \n")  # Player input
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
    slow_print(story_room_6())  # Print story in game_stories.py
    slower_print(r"""
Options:
1. Look Around
2. Move back
3. Move right
""")
    routes = ["1", "2", "3"]
    user_input = ""

    while user_input not in routes:
        user_input = input("What do you do? \n")  # Player input
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
    slow_print(story_room_7())  # Print story in game_stories.py
    slower_print(r"""
Options:
1. Run back
2. Stand and fight
""")
    routes = ["1", "2"]
    user_input = ""

    while user_input not in routes:
        user_input = input("What do you do? \n")  # Player input
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
    slow_print(story_room_7_continue())  # Print story cont in game_stories.py
    slower_print(r"""
Options:
1. Move forward
2. Move left
""")
    routes = ["1", "2"]
    user_input = ""

    while user_input not in routes:
        user_input = input("What do you do? \n")  # Player input
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
    slow_print(story_death_room_1())  # Print the story in game_stories.py
    death_scene()


def death_room_2():
    """
    Death 2 room function
    """
    clear_screen()
    slow_print(story_death_room_2())  # Print the story in game_stories.py
    death_scene()


def death_scene():
    """
    Death scene function
    """
    while True:
        game_input = input(f"\nGame Over {PLAYER_NAME}, "
                           "would you like to play again? (y/n)")
        if game_input.lower() == "y":
            main()
        elif game_input.lower() == "n":
            print("Until next time.")
            sys.exit()
        else:
            print("Please Enter a valid command.")


def weapon_1():
    """
    Function for Mining Laser
    """
    global WEAPON_TYPE
    clear_screen()

    if "Mining Laser" in WEAPON_TYPE:
        print("You have already investigated and picked up a Mining Laser.")
    else:
        slow_print(story_weapon_1())  # Print story in game_stories.py
        WEAPON_TYPE.append("Mining Laser")

    input("\nPress Enter to continue\n")  # Wait for the player to press Enter
    room_3()


def weapon_2():
    """
    Function for Shovel
    """
    global WEAPON_TYPE
    clear_screen()

    if "Shovel" in WEAPON_TYPE:
        print("You have already investigated and picked up a Shovel.")
    else:
        slow_print(story_weapon_2())  # Print the weapon 2 in game_stories.py
        WEAPON_TYPE.append("Shovel")

    input("\nPress Enter to continue\n")  # Wait for the player to press Enter
    room_6()


def fight_1():
    """
    Function for fighting
    """
    clear_screen()
    slow_print(story_fight_1())  # Print story in game_stories.py
    scarab_health = 3
    player_health = 10

    while scarab_health > 0 and player_health > 0:
        if "Mining Laser" in WEAPON_TYPE:
            input("\nPress Enter to take a shot.")

            # Generate a random number between 1 and 6
            random_hit = random.randint(1, 6)

            if random_hit >= 3:
                scarab_health -= 1
                print(f"""
You rolled a {random_hit} and hit the enemy!
They have {scarab_health} health left.
""")
            else:
                player_health -= 1
                print(f"""
Your attack missed with a {random_hit},
the scarabs attack you and you have {player_health} health left.
""")
        else:
            print(wrong_weapon())
            input("Press Enter to continue\n")  # Wait for Enter press
            room_3()
            break
    else:
        if player_health <= 0:
            print("You have been defeated. Game over.\n")
            input("Press Enter to continue\n")  # Wait for Enter press
            death_scene()

        elif scarab_health <= 0:
            print("You defeated the scarabs. You win!\n")
            input("Press Enter to continue\n")  # Wait for Enter press
            exit_scene()


def fight_2():
    """
    Function for fighting 2
    """
    clear_screen()
    slow_print(story_fight_2())  # Print the fight 2 in game_stories.py
    warrior_health = 4
    player_health = 10

    while warrior_health > 0 and player_health > 0:
        if "Shovel" in WEAPON_TYPE:
            input("\nPress Enter to take a shot.\n")  # Wait for Enter press

            # Generate a random number between 1 and 6
            random_hit = random.randint(1, 6)

            if random_hit >= 4:
                warrior_health -= 1
                print(f"""
You rolled a {random_hit} and hit the enemy!
They have {warrior_health} health left.
""")
            else:
                player_health -= 1
                print(f"""
Your attack missed with a {random_hit},
the warrior attacks you and you have {player_health} health left.
""")
        else:
            print(wrong_weapon())
            input("Press Enter to continue\n")  # Wait for Enter press
            room_6()
            break
    else:
        if player_health <= 0:
            print("You have been defeated. Game over.\n")
            input("Press Enter to continue\n")  # Wait for Enter press
            death_scene()

        elif warrior_health <= 0:
            print("You defeated the Warrior. You win!\n")
            input("Press Enter to continue\n")  # Wait for Enter press
            room_7_continue()


def exit_scene():
    """
    Exit scene function
    """
    clear_screen()
    slow_print(story_exit_scene())  # Print the exit scene in game_stories.py
    death_scene()


def hieroglyphs_1():
    """
    Function for hieroglyphs option 1
    """
    clear_screen()
    slow_print(story_hieroglyphs())  # Print story in game_stories.py
    fast_print(story_hieroglyphs_1())  # Print story in game_stories.py
    input("\nPress Enter to continue and move into the room ahead\n")
    room_1()


def hieroglyphs_2():
    """
    Function for hieroglyphs option 2
    """
    clear_screen()
    slow_print(story_hieroglyphs())  # Print story in game_stories.py
    fast_print(story_hieroglyphs_2())  # Print story 2 in game_stories.py
    input("\nPress Enter to continue from the room you are in\n")
    room_5()


main()
