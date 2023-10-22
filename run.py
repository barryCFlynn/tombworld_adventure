import time

def slow_print_01(print_statement):
      for char in print_statement:
        print(char, end='', flush=True)
        time.sleep(0.1)

def slow_print_03(print_statement):
      for char in print_statement:
        print(char, end='', flush=True)
        time.sleep(0.3)


import time

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
      slower_print(
            r""" i am slow 01 this is a test print so see if functions are running
            """)
      slow_print(
            r""" I am slow 03 this is a test print so see if functions are running
            """)

main()
