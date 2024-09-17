import requests
import poke_api
import poke_menu as menu
from poke_api import POKEAPI_URL

DRINK_LETTER_URL = 'https://www.thecocktaildb.com/api/json/v1/1/search.php?f='
COCKTAIL_ASCII = 'art/cocktail_ascii.txt'

def run_pokemon_to_drink():
    """
    Displays an intro to this subsystem and displays the final results at the end.
    """
    menu.print_ascii(COCKTAIL_ASCII)
    menu.print_stars()
    print('Welcome to the drink matching menu!')
    menu.print_stars()
    print("First let's search for a Pokemon, try Charizard or Dratini!")

    poke_name = get_pokemon_input()
    drink_name = convert_to_drink(poke_name)

    menu.print_stars()
    print(f'Your searched Pokemon was: {poke_name.capitalize()}')
    print(f'Your matching drink is: {drink_name}')

def get_pokemon_input():
    """
    Asks the user for a Pokémon name, then proceeds to check if it is an existing name.
    """
    while True:
        poke_input = input("Please enter the Pokémon you'd like to convert:").lower()
        if poke_input.isalpha():
            poke_response = requests.get(f'{POKEAPI_URL}{poke_input}')
            if poke_response.status_code == 200:
                return poke_input
            else:
                print("Please enter a valid Pokémon name.")
        else:
            print('Please only use letters to type out the name.')

def convert_to_drink(poke_name = ''):
    """
    Converts the Pokémon name to drink search and corresponding ID.
    """
    drink_letter = get_letter(poke_name)
    #Gets the first letter
    drink_dict= poke_api.call_api(DRINK_LETTER_URL, drink_letter)
    #Searches with the cocktail API
    drink_id = convert_drink(poke_name,len(drink_dict['drinks']))
    #Decided corresponding ID in the search results.
    return drink_dict['drinks'][drink_id]['strDrink']

def get_letter(poke_name):
    """
    Generates the first letter of the Pokémon name to search for a drink and prevents bugs where there are no results.
    """
    drink_letter = poke_name[0]
    for i in range(len(poke_name)):
        if drink_letter in ['u','x']:
            drink_letter = poke_name[i]
            #fixes a bug where there are no drink results when searching U or X

    return drink_letter

def convert_drink(convert_string,length = 1):
    """
    Calculates a drink ID number based on the ascii values of the Pokémon name and the amount of results.
    """
    output_value = 1
    for i in range(len(convert_string)):
        output_value += ord(convert_string[i])

    drink_id = output_value % length
    return drink_id