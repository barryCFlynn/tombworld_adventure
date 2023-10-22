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
      global PLAYER_NAME
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
      PLAYER_NAME = input("What is your name?")
      print(f"Welcome, {PLAYER_NAME}.")
      room_1()




def room_1():
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
            """)
      print(
            r"""
            Options:
            1. Look around
            3. Check your belongings
            4. Move forward
            5. Move left
            6. Move right
            """)

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

main()