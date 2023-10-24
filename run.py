"""
imports
"""
import time

"""
Global variables
"""
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
                              intro_scene()
                              break
                        elif game_input == "n":
                              print("Until next time.")
                              break
                        else:
                              print("Please enter a valid command.")
            else:
                  print("Please enter a valid name with only alphabetical characters.")


def intro_scene():
      """
      Room 1 function and options
      """
      routes = ["1", "2", "3", "4", "5"]
      user_input = ""
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
3. Check your belongings
4. Move forward
5. Move left
6. Move right
"""
            )

      while user_input not in routes:
            user_input = input("What do you do? ")
            if user_input == "1":
                  print("place holder for function to come 'Investigate hieroglyphs'")
            elif user_input == "2":
                  print("place holder for function to come 'Check belongings'")
            elif user_input == "3":
                  print("place holder for function to come 'Move forward'")
            elif user_input == "4":
                  print("place holder for function to come 'Move left'")
            elif user_input == "5":
                  print("place holder for function to come 'Move right'")
            else:
                  print("I don't understand that command, try another one.")

def hieroglyphs():
      """
      Function for hieroglyphs
      """
      routes = ["1", "2", "3", "4", "5"]
      user_input = ""

      print(
            r""" 
            You approach the hieroglyphs, they glow with green light and are in a 
            language you dont understand but you hear a voice in your head.
            """)
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
            """)
      


main()