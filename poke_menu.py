import poke_drink_to_pokemon

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
    print('Function three: Matching drink quizz (Q)')
    print_stars()

def print_stars():
    """
    prints a line of stars for decorative and readability purposes.
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
        #Will point to quizz subsystem
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
