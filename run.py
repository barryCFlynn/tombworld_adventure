"""
imports for the game
"""
import time
import os
import random
import sys


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
    clear_screen()
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
                # Ask the player if they are ready to play
                game_input = input("Are you ready to escape? (y/n) ")
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
2. Move forward
"""
        )
    routes = ["1", "2"]
    user_input = ""

    while user_input not in routes:
        user_input = input("What do you do? ") # Ask the player what they want to do
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
    print(
r"""
As you step into the room ahead, the air grows colder, and the dim light 
reveals intricate carvings on the walls, you hear the eerie echoes of 
metallic footsteps approaching from the door to your right, a foreboding 
presence drawing nearer but you see another passageway forward.
"""
    )
    print(
r"""
Options:
1. Move Right
2. Move Forward
"""
        )
    routes = ["1", "2"]
    user_input = ""

    while user_input not in routes:
        user_input = input("What do you do? ") # Ask the player what they want to do
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
    print(
r"""
As you cautiously enter the room ahead, the chamber is bathed in an eerie, 
dim light, casting an eldritch green glow that pervades the air with an 
otherworldly energy. Amidst this mysterious ambiance, you're drawn to a curious 
sight. An ethereal white light emanating from the room to your left. Its source 
and purpose remain enigmatic, yet it fills you with a glimmer of hope."
"""
    )
    print(
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
    clear_screen()
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
    clear_screen()
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
    routes = ["1", "2"]
    user_input = ""

    while user_input not in routes:
        user_input = input("What do you do? ") # Ask the player what they want to do
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
    print(
r"""
As you cautiously advance into the chamber, the surroundings reveal an eerie scene.
Directly ahead, a passage looms in the dim light, but a foreboding presence lingers there,
a palpable sense of danger.

To your right, an alternative route beckons, seeming the wiser choice. The walls are
adorned with ancient hieroglyphs, their symbols etched into the stone, hinting at cryptic
knowledge. It's a room filled with a sense of unease, and your path must be
chosen carefully.
"""
    )
    print(
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
        user_input = input("What do you do? ") # Ask the player what they want to do
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
    print(
r"""
Upon entering the room, your surroundings unfold before you. To the far side, a peculiar object
protrudes from the ground, its nature hidden in the shadows. It beckons with an air of mystery,
enticing your curiosity.

On the right, a passage extends, promising a path forward, yet it something tells you that 
there is danger that way. This chamber is a crossroads of choices, each fraught with 
uncertainty and potential peril, and your next move will determine your fate in this necron tomb.
"""
    )
    print(
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
        user_input = input("What do you do? ") # Ask the player what they want to do
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
    print(
r"""
In the dim, eerie light, you step into a chilling room. A harrowing sight unfolds before you as 
the lifeless forms of your comrades lie strewn across the floor, victims of the relentless 
Necron warriors. Silence hangs heavily in the air, broken only by your own breath.

Amidst the carnage, a single Necron warrior stands, visibly damaged, its once-imposing form now
showing signs of wear. It gazes at you with its cold, metallic eyes, a solitary sentinel in this
chamber of death.

A choice looms before you — do you attack the wounded Necron warrior, or do you go back the way 
you came?
"""
    )
    print(
r"""
Options:
1. Run back
2. Stand and fight
"""
        )
    routes = ["1", "2"]
    user_input = ""

    while user_input not in routes:
        user_input = input("What do you do? ") # Ask the player what they want to do
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
    print(
r"""
You have defeated the Necron warrior, but not without injury. You stand in the same room, your
own wounds a reminder of the battle.

Two passages stretch before you. The one directly ahead reverberates with eerie echoes of 
metallic footsteps drawing near, a haunting presence approaching.

The other passageway appears as your only viable option, beckoning you to venture deeper into 
this labyrinthine tomb, the choices ahead shrouded in uncertainty and danger.
"""
    )
    print(
r"""
Options:
1. Move forward
2. Move left
"""
        )
    routes = ["1", "2"]
    user_input = ""

    while user_input not in routes:
        user_input = input("What do you do? ") # Ask the player what they want to do
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
    print(
r"""
As you continue down the dimly lit corridor, the walls start to close in, and 
the air grows increasingly oppressive. Suddenly, a group of sinister Necron Immortals 
emerges from the shadows. Their eyes gleam with malevolent intent, they snap out of
existence and instantly reappear around you. You fight valiantly, but their cold, 
unfeeling metal bodies prove too much. Your vision fades as their unrelenting onslaught
overwhelms you, and you succumb to the darkness, becoming another lost soul in the tomb world.
"""
    )
    death_scene()

def death_room_2():
    """
    Death 2 room function
    """
    clear_screen()
    print(
r"""
Intrigued by the path forward, you venture deeper into the room, only to witness an unsettling 
sight.A dark, shadowy figure moves through the far wall with an eerie, ethereal grace. It's a 
Necron Wraith, a dreaded sentinel of the tomb world.

Before you can react, its piercing crimson gaze locks onto you. In an instant, it darts forward, its
form engulfing you. The world fades to black as the Necron Wraith's piercing touch claims your life,
leaving you as one more lost soul in the necropolis of the tomb world.
"""
    )
    death_scene()

def death_scene():
    """
    Death scene function
    """
    while True:
        game_input = input(f"Game Over {PLAYER_NAME}, would you like to play again? (y/n) ")
        if game_input == "y":
            main()
        elif game_input == "n":
            print("Until next time.")
            sys.exit()
        else:
            print("Please enter a valid command.")

def weapon_1():
    """
    Function for Mining Laser
    """
    clear_screen()
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

def weapon_2():
    """
    Function for Shovel
    """
    clear_screen()
    print(
r"""
As you cautiously venture deeper into the room approaching the object. In the dim light,
your eyes fix on something unusual. As you draw nearer, you discern the eerie sight of a
lifeless figure slumped over a shovel, still stuck in the stone. It's a chilling discovery.

You recognize the man as one of your fellow miners, a member of your team. Questions flood
your mind. What could have driven him to such despair that he resorted to using a shovel in
a futile attempt to dig through the impenetrable stone face of this necron tomb?

The mystery deepens, and the choices before you weigh heavily in this enigmatic world of
shadows and secrets. You reach down and pick up the shovel, carrying it with you as a grim 
reminder of the perils that surround you.
"""
    )
    global WEAPON_TYPE
    WEAPON_TYPE = "Shovel"
    input("Press enter to continue") # Wait for the player to press Enter
    room_6()

def fight_1():
    """
    Function for fighting
    """
    clear_screen()
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
    scarab_health = 3
    player_health = 10

    while scarab_health > 0 and player_health > 0:
        if WEAPON_TYPE == "Mining Laser":
            input("Press Enter to take a shot.")  # Wait for the player to press Enter

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
            print(
r"""
You don't have the right weapon to fight and you retreat back to the room you came from.
"""
            )
            input("Press Enter to continue") # Wait for the player to press Enter
            room_3()
            break
    else:
        if player_health <= 0:
            print("You have been defeated. Game over.")
            input("Press Enter to continue") # Wait for the player to press Enter
            death_scene()

        elif scarab_health <= 0:
            print("You defeated the scarabs. You win!")
            input("Press Enter to continue") # Wait for the player to press Enter
            exit_scene()

def fight_2():
    """
    Function for fighting 2
    """
    clear_screen()
    print(
r"""
You make the bold decision to confront the damaged Necron warrior. Your starting health stands 
at a mere 10, while the enemy health is at 4.
You choose to fight, rushing the wounded Necron warrior with your shovel. In a swift, intense
clash, sparks fly as metal meets metal. The battle rages on, a desperate struggle between flesh
and steel.
"""
    )
    input("Press enter to continue") # Wait for the player to press Enter
    warrior_health = 4
    player_health = 10

    while warrior_health > 0 and player_health > 0:
        if WEAPON_TYPE == "Shovel":
            input("Press Enter to take a shot.")  # Wait for the player to press Enter

            # Generate a random number between 1 and 6
            random_hit = random.randint(1, 6)

            if random_hit >= 4:
                scarab_health -= 1
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
            print(
r"""
You don't have the right weapon to fight and you retreat back to the room you came from.
"""
            )
            input("Press Enter to continue") # Wait for the player to press Enter
            room_6()
            break
    else:
        if player_health <= 0:
            print("You have been defeated. Game over.")
            input("Press Enter to continue") # Wait for the player to press Enter
            death_scene()

        elif scarab_health <= 0:
            print("You defeated the Warrior. You win!")
            input("Press Enter to continue") # Wait for the player to press Enter
            room_7_continue()

def exit_scene():
    """
    Exit scene function
    """
    clear_screen()
    print(
r"""
You sprint past the defeated foes obstructing your path, hurtling into the corridor where an 
intense, blinding light beckons from the far end. Without hesitation, you discard your weapons
and dash toward the radiance. As you approach, an invisible barrier halts your advance, revealing
a looming figure on the other side. It's a Necron Overlord, and an eerie awareness in your mind
whispers his name: Trazyn. In a cold, robotic voice projected into your consciousness, he 
utters, 'Shall we try again?'
"""
    )
    death_scene()

def hieroglyphs_1():
    """
    Function for hieroglyphs option 1
    """
    clear_screen()
    print(
r""" 
You approach the hieroglyphs, they glow with green light and are in a 
language you dont understand but you hear a voice in your head.
"""
        )
    print(
r""" 
Long before the current age, the Necrons were an advanced and powerful civilization.
Known as the 'Necrontyr,' their existence was marred by a relentless hunger for power
and a thirst for immortality. In their pursuit of these ambitions, they entered into
a Faustian pact with mysterious cosmic beings known as the C'tan.

The Necrontyr were transformed into soulless, mechanical beings called the 'Necrons'
in exchange for extended life. Their flesh turned to metal, and their consciousnesses
were bound to intricate machine bodies. These soulless warriors served the C'tan
with unwavering loyalty.

A devastating war between the Necrons and the ancient Eldari, once a thriving
civilization, reshaped the galaxy. The Necrons retreated to dormant tombs scattered
across the stars, awaiting the day they would reawaken and reclaim their dominion
over the universe.

As you decipher the hieroglyphs, you catch glimpses of this dark history, filled with
promises of power, immortality, and a looming sense of malevolence.
"""
    )
    # Wait for the player to press Enter
    input("Press enter to continue and move into the room ahead")
    room_1()

def hieroglyphs_2():
    """
    Function for hieroglyphs option 2
    """
    clear_screen()
    print(
r""" 
You approach the hieroglyphs, they glow with green light and are in a 
language you dont understand but you hear a voice in your head.
"""
    )
    print(
r"""
The hieroglyphs unveil the enigmatic figure of 'Trazyn,' a formidable Necron Overlord
renowned not only for his dominion over the legions of Necrons but also for his profound
mastery of time and ancient relics. Trazyn is a collector without peer, amassing an
unparalleled trove of artifacts and esoteric knowledge spanning the ages.

His arcane vaults house treasures from epochs long past, relics from bygone civilizations,
and the technology to manipulate time itself. Trazyn's control over temporal forces grants
him the ability to traverse history, and his formidable intellect wields power over the
past, present, and future.

With his keen intellect, strategic brilliance, and access to these awe-inspiring
artifacts, Trazyn is a force to be reckoned with in the dark and mysterious realm of
the Necrons.
"""
    )
    input("Press enter to continue from the room you are in") # Wait for the player to press Enter
    room_5()

main()
