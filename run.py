"""
imports for the game
"""
import time
import os
import random


"""
Global variables for the game
"""
PLAYER_NAME = ""
# WEAPON = False not in use might be deleted
WEAPON_TYPE = ""



def slower_print(print_statement):
    """
    Function to print a string one character at a time at speed 0.1
    """
    for char in print_statement:
        print(char, end='', flush=True)
        time.sleep(0.1)

def slow_print(print_statement):
    """
    Function to print a string one character at a time at speed 0.01
    """
    for char in print_statement:
        print(char, end='', flush=True)
        time.sleep(0.01)

def clear_screen():
    """
    Clear the terminal screen.
    """
    os.system("cls" if os.name == "nt" else "clear")




def main():
    """
    This is the main function that will run the program
    """
    print(r""" 
████████╗ ██████╗ ███╗   ███╗██████╗ ██╗    ██╗ ██████╗ ██████╗ ██╗     ██████╗     
╚══██╔══╝██╔═══██╗████╗ ████║██╔══██╗██║    ██║██╔═══██╗██╔══██╗██║     ██╔══██╗    
   ██║   ██║   ██║██╔████╔██║██████╔╝██║ █╗ ██║██║   ██║██████╔╝██║     ██║  ██║    
   ██║   ██║   ██║██║╚██╔╝██║██╔══██╗██║███╗██║██║   ██║██╔══██╗██║     ██║  ██║    
   ██║   ╚██████╔╝██║ ╚═╝ ██║██████╔╝╚███╔███╔╝╚██████╔╝██║  ██║███████╗██████╔╝    
   ╚═╝    ╚═════╝ ╚═╝     ╚═╝╚═════╝  ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═════╝     
                                                                                    
 █████╗ ██████╗ ██╗   ██╗███████╗███╗   ██╗████████╗██╗   ██╗██████╗ ███████╗       
██╔══██╗██╔══██╗██║   ██║██╔════╝████╗  ██║╚══██╔══╝██║   ██║██╔══██╗██╔════╝       
███████║██║  ██║██║   ██║█████╗  ██╔██╗ ██║   ██║   ██║   ██║██████╔╝█████╗         
██╔══██║██║  ██║╚██╗ ██╔╝██╔══╝  ██║╚██╗██║   ██║   ██║   ██║██╔══██╗██╔══╝         
██║  ██║██████╔╝ ╚████╔╝ ███████╗██║ ╚████║   ██║   ╚██████╔╝██║  ██║███████╗       
╚═╝  ╚═╝╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝       
                                                                                                                                                                                                                                                                                       
""")
    print(
r"""Welcome to Tombworld Adventure, a gripping text-based 
journey set in the grim and mysterious universe of Warhammer 
40,000. You were a miner toiling on a barren planet, but a 
strange blackout has transported you to a Necron tomb world. 
Navigate eerie catacombs, decipher ancient hieroglyphs, and 
confront unspeakable terrors as you strive for survival and 
your escape. Are you prepared to face the malevolent forces 
of the Necrons and find your path back to the world you once knew?
"""
    )
    global PLAYER_NAME
    while True:
        PLAYER_NAME = input("What is your name? ") # Ask the player for their name
        if PLAYER_NAME.isalpha():
            print(f"Welcome, {PLAYER_NAME}.")
            while True:
                game_input = input("Are you ready to escape? (y/n) ") # Ask the player if they are ready to play
                if game_input == "y":
                    room_intro()
                    break
                elif game_input == "n":
                    print("Until next time.")
                    break
                else:
                    print("Please enter a valid command.")
        else:
            print("Please enter a valid name with only alphabetical characters.")


def room_intro():
    """
    Room 1 function and options
    """
    print(
r"""
You awaken in a dimly lit chamber, the cold and metallic floor
beneath you. The air is thick with an otherworldly chill. You 
can hear the faint hum of ancient machinery echoing through the vast 
catacombs. As your eyes adjust, you see eerie hieroglyphs etched into 
the walls, and the unmistakable mark of the Necrons is all around.
"""
        )
    print(
r"""
Options:
1. Look around
2. Check your belongings
3. Move forward
"""
        )
    routes = ["1", "2", "3"]
    user_input = ""

    while user_input not in routes:
        user_input = input("What do you do? ") # Ask the player what they want to do
        if user_input == "1":
            hieroglyphs_1()
        elif user_input == "2":
            print("place holder for function to come 'Check belongings'")
        elif user_input == "3":
            room_1()
        else:
            print("I don't understand that command, try another one.")



def room_1():
    """
    Room 1 function and options
    """
    print(
        r"""
As you step into the room ahead, the air grows colder, and the dim light 
reveals intricate carvings on the walls, you hear the eerie echoes of 
metallic footsteps approaching from the door to your left, a foreboding 
presence drawing nearer.
"""
    )
    print(
r"""
Options:
1. Look around
2. Move left
3. Move forward
"""
        )
    routes = ["1", "2", "3"]
    user_input = ""

    while user_input not in routes:
        user_input = input("What do you do? ") # Ask the player what they want to do
        if user_input == "1":
            hieroglyphs_1()
        elif user_input == "2":
            death_scene()
        elif user_input == "3":
            room_2()
        else:
            print("I don't understand that command, try another one.")


def room_2():
    """
    Room 2 function and options
    """
    print(
        r"""
As you cautiously enter the room ahead, the chamber is bathed in an eerie, 
dim light, casting an eldritch green glow that pervades the air with an 
otherworldly energy. Amidst this mysterious ambiance, you're drawn to a curious 
sight—an ethereal white light emanating from the room to your right. Its source 
and purpose remain enigmatic, yet it fills you with a glimmer of hope."
"""
    )
    print(
r"""
Options:
1. Move back
2. Move right
3. Move forward
"""
        )
    routes = ["1", "2", "3"]
    user_input = ""

    while user_input not in routes:
        user_input = input("What do you do? ") # Ask the player what they want to do
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
    print(
        r"""
As you enter the room with the white light, it's veiled in an unsettling darkness. Your eyes 
gradually adapt to the obscurity, and you're drawn to a flickering white light originating 
from an unclear object concealed in the corner. In the dimly lit surroundings, your attention 
is also captured by an open doorway to your right, hinting at an inviting path to explore. 
However, amidst the uncertainty, you hear the disconcerting sound of metal skittering across stone.
"""
    )
    print(
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
        user_input = input("What do you do? ") # Ask the player what they want to do
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
    print(
        r"""
You step into the room and come face to face with a swarm of small insect-like creatures. 
Something in your mind tells you they are Scarabs, the Necron tomb maintenance creatures. 
You notice a promising open passageway to your right, but a barrier of Scarabs stands between you 
and the path. They have not detected your presence as a threat yet, 
leaving you with a crucial decision: run back the way you came or attempt to fight.
"""
    )
    print(
r"""
Options:
1. Run back
2. Stand and fight
"""
        )
    routes = ["1", "2", "3"]
    user_input = ""

    while user_input not in routes:
        user_input = input("What do you do? ") # Ask the player what they want to do
        if user_input == "1":
            room_3()
        elif user_input == "2":
            fight()
        else:
            print("I don't understand that command, try another one.")

def death_room_1():
    """
    Death 1 room function
    """
    print(
r"""
"As you continue down the dimly lit corridor, the walls start to close in, and 
the air grows increasingly oppressive. Suddenly, a group of sinister Necron warriors 
emerges from the shadows. Their eyes gleam with malevolent intent, and with lightning
 speed, they surround you. You fight valiantly, but their cold, unfeeling metal bodies 
 prove too much. Your vision fades as their unrelenting onslaught overwhelms you, and 
 you succumb to the darkness, becoming another lost soul in the tomb world.
"""
    )
    death_scene()


def death_scene():
    """
    Death scene function
    """

    while True:
        game_input = input(f"you have died {PLAYER_NAME}, would you like to play again? (y/n) ")
        if game_input == "y":
            main()
            break
        elif game_input == "n":
            print("Until next time.")
            break
        else:
            print("Please enter a valid command.")

def weapon_1():
    """
    Function for Mining Laser
    """
    print(
r"""
You move towards the flashing light and discover a cargo palette from your mining facility. 
Hastily rummaging through it, you unearth a valuable mining laser. 
Realizing its potential usefulness, you carefully stow it in your bag, thoughts of its 
utility racing through your mind.
"""
    )
    global WEAPON_TYPE
    WEAPON_TYPE = "Mining Laser"
    input("Press enter to continue") # Wait for the player to press Enter
    room_3()

def fight():
    """
    Function for fighting
    """
    print(
r"""
You make the bold decision to confront the swarm of Scarabs. Your starting health stands 
at a mere 10, while the enemy Scarabs number at 3. The odds are against you as you raise
your mining laser, ready to take a chance. Aiming carefully, you squeeze the trigger, 
hoping to land a hit and reduce their numbers. The outcome remains uncertain; a 
successful hit will decrease their health, but failure means they will retaliate, 
diminishing your own.
"""
    )
    input("Press enter to continue") # Wait for the player to press Enter
    #WEAPON_TYPE = "Mining Laser"
    scarab_health = 3
    player_health = 10

    while scarab_health > 0 and player_health > 0:
        if WEAPON_TYPE == "Mining Laser":
            input("Press Enter to take a shot.")  # Wait for the player to press Enter

            # Generate a random number between 1 and 6
            random_hit = random.randint(1, 6)

            if random_hit >= 3:
                scarab_health -= 1
                print(f"""
    You rolled a {random_hit} and hit the enemy!
    They have {scarab_health} health left.
                """
                )
            else:
                player_health -= 1
                print(f"""
    Your attack missed with a {random_hit},
    the scarabs attack you and you have {player_health} health left.
                """
                )
        else:
            print(r"""
    You don't have the right weapon to fight and you retreat back to the room you came from.
            """
            )
            input("Press Enter to continue") # Wait for the player to press Enter
            room_3()
            break
    else:
        if player_health <= 0:
            print("You have been defeated. Game over.")
            death_scene()

        elif scarab_health <= 0:
            print("You defeated the scarabs. You win!")
            #exit_scene()


def hieroglyphs_1():
    """
    Function for hieroglyphs
    """
    print(
r""" 
You approach the hieroglyphs, they glow with green light and are in a 
language you dont understand but you hear a voice in your head.
"""
        )
    print(
r""" 
In the distant past, long before the Imperium of Man rose to power, this 
desolate planet was once a thriving world of advanced civilization. The 
inhabitants, known as the 'Eldari' by some ancient texts, were masters of
technology and arcane knowledge. They built grand cities and harnessed the 
power of the stars. However, their relentless pursuit of power and forbidden 
experiments led them to the brink of their own destruction.

As their civilization teetered on the edge of annihilation, a dark force, 
now known as the Necrons, emerged from the shadows. The Necrons, beings of 
cold metal and remorseless determination, sought to reclaim the planet for 
their own purposes.

A catastrophic war ensued, and the once-proud Eldari were driven to the brink
of extinction. In a final desperate act, the Eldari used their dwindling power 
to seal themselves within hidden tombs deep beneath the planet's surface. They 
hoped that one day, they might awaken to rebuild their civilization.

Now, eons later, you find yourself in this forsaken place, surrounded by the 
echoes of an ancient conflict and the ominous presence of the Necrons, who have 
waited patiently for the day they would rise once more.
"""
    )
    input("Press enter to continue") # Wait for the player to press Enter
    room_1()


room_3()
#fight()
#main()