import poke_drink_to_pokemon
import poke_main

def display_menu():
    """
    Prints the intro to the program.
    """
    print_stars()
    print('Welcome to the Pokécocktail program')
    print_stars()
    print('Please choose from the following functionalities:')
    print('Function one: Convert Pokémon to matching drink (D)')
    print('Function two: Convert Drink to matching Pokémon (P)')
    print('Function three: Matching drink quiz (Q)')
    print_stars()

def print_stars():
    """
    Prints a line of stars for decorative and readability purposes.
    """
    print('*' * 50)

def run_subsystem(input_value):
    """
    Tells the program which subsystem to point to using user input.
    """
    if input_value == 'd':
        #Will point to drink matching subsystem
        print(input_value)
    elif input_value == 'p':
        #Will point to pokémon matching subsystem
        poke_drink_to_pokemon.run_drink_to_pokemon()
    else:
        #Will point to quiz subsystem
        print(input_value)

def get_func_input():
    """
    Takes input from the user to point to the selected functionality.
    """
    while True:
        input_value = input('Please enter your choice: ').lower()
        if input_value == 'd' or input_value == 'p' or input_value == 'q':
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
