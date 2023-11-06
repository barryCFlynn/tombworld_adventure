"""
collection of all gameplay statements
"""

import time
import os


def fast_print(print_statement):
    """
    Function to print a string one character at a time at speed 0.001
    """
    for char in print_statement:
        print(char, end='', flush=True)
        time.sleep(0.001)


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
