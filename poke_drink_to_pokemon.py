import poke_menu as menu
import poke_api
from poke_api import POKEAPI_URL

DRINK_SEARCH_URL = "https://www.thecocktaildb.com/api/json/v1/1/search.php?s="

MAX_POKEMON = 1025
POKEMON_ASCII = 'art/pokemon_ascii.txt'

def run_drink_to_pokemon():
    """
    Displays an into to this subsystem and displays the final results at the end.
    """
    menu.print_ascii(POKEMON_ASCII)
    menu.print_stars()
    print('Welcome to the Pokemon matching menu!')
    menu.print_stars()
    print("First let's search for a drink. Try Pina Colada or Mojito!")

    drink_string = get_drinkinput()
    poke_name = convert_to_pokemon(drink_string)

    menu.print_stars()
    print(f'Your searched drink is: {drink_string}')
    print(f'Your matching pokemon is: {poke_name.capitalize()}')

def convert_to_pokemon(convert_string):
    """
    Calculates the ID of a Pokémon based on the ascii codes of the drink name.Then returns the name of the Pokémon
    """
    output_value = 1
    for i in range(len(convert_string)):
        output_value *= ord(convert_string[i])
        #ord function grabs the ascii value of a character.
    poke_id = output_value % MAX_POKEMON
    if poke_id == 0:
        poke_id =+ 1
        #Fixes a bug where the program can't make a valid API call when poke_id is 0

    poke_name = get_pokemon(poke_id)
    return poke_name

def get_pokemon(poke_id):
    """
    Uses the poké API to find a Pokémon based on given ID
    """
    pokemon_dict = poke_api.call_api(POKEAPI_URL, poke_id)
    poke_name = pokemon_dict['name']
    return poke_name

def get_drinkinput():
    """
    Asks for input and searches for a drink. Returns a valid drink.
    """
    while True:
        input_string = input("Please enter (part of) the name of a drink:")
        drink_dict = poke_api.call_api(DRINK_SEARCH_URL,input_string)
        if drink_dict['drinks'] is not None:
            break
        else:
            print("Can't find a valid drink, try again.")

    drink_string = drink_dict['drinks'][0]['strDrink']
    return drink_string
