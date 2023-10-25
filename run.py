
# imports

import time


# Global variables

PLAYER_NAME = ""
WEAPON = False
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
        PLAYER_NAME = input("What is your name? ")
        if PLAYER_NAME.isalpha():
            print(f"Welcome, {PLAYER_NAME}.")
            while True:
                game_input = input("Are you ready to escape? (y/n) ")
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
        user_input = input("What do you do? ")
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
        user_input = input("What do you do? ")
        if user_input == "1":
                print("You find nothing of interest.")
        elif user_input == "2":
                death_scene()
        elif user_input == "3":
                print("place holder for function to come 'Move forward'")
        else:
                print("I don't understand that command, try another one.")

def death_scene():
    """
    Death scene function
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
    global PLAYER_NAME
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


main()
