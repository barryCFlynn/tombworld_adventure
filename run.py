"""
imports
"""
import time

"""
Global variables
"""
PLAYER_NAME = "Player"
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
      slow_print(
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


main()
