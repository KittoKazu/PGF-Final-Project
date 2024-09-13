import poke_drink_to_pokemon
import poke_pokemon_to_drink
import poke_quiz
import poke_main

MENU_ART = 'art/menu_ascii.txt'

def display_menu():
    """
    Prints the intro to the program.
    """
    print_ascii(MENU_ART)
    print_stars()
    print('Welcome to the Pokécocktail program')
    print_stars()
    print('Please choose from the following functionalities:')
    print('Function one: Convert Pokémon to matching drink (D)')
    print('Function two: Convert Drink to matching Pokémon (P)')
    print('Function three: Matching Pokemon/drink quiz (Q)')
    print_stars()

def print_stars():
    """
    Prints a line of stars for decorative and readability purposes.
    """
    print('*' * 70)

def run_subsystem(input_value):
    """
    Tells the program which subsystem to point to using user input.
    """
    if input_value == 'd':
        #Will point to drink matching subsystem
        poke_pokemon_to_drink.run_pokemon_to_drink()
    elif input_value == 'p':
        #Will point to pokémon matching subsystem
        poke_drink_to_pokemon.run_drink_to_pokemon()
    else:
        #Will point to quiz subsystem
        poke_quiz.run_quiz()

def get_func_input():
    """
    Takes input from the user to point to the selected functionality.
    """
    while True:
        input_value = input('Please enter your choice: ').lower()
        if input_value in ['d','p','q']:
            #Checks if the input matches one of the valid options.
            return input_value
        else:
            #Handles error and asks user for another input.
            print('Please enter a valid option.')
            print_stars()

def ask_to_resume():
    """
    Function that asks the user if they want to keep the program running to use another functionality.
    """
    while True:
        print_stars()
        resume_input = input('Would you like to continue using the program? (Y/N): ').lower()
        if resume_input == 'y' or resume_input == 'n':
            if resume_input == 'n':
                exit()
            if resume_input == 'y':
                poke_main.main()
        else:
            print('Please enter a valid input.')

def print_ascii(filepath):
    """
    Uses a specified filepath to print an ascii art from a txt file, not cluttering the code.
    """
    try:
        with open(f'{filepath}', 'r') as file:
            ascii_art = file.read()
            print(ascii_art)
    except FileNotFoundError:
        print('No .txt file found for ascii art.')