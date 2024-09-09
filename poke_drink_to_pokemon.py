import requests
import poke_menu
import poke_main

MAX_POKEMON = 1025

def run_drink_to_pokemon():
    """
    Displays an into to this subsystem and displays the final results at the end.
    """
    poke_menu.print_stars()
    print('Welcome to drink matching menu')
    poke_menu.print_stars()
    print("First let's search for a drink. Try Pina Colada!")

    drink_string = get_drinkinput()
    pokemon_id = convert_pokemon(drink_string)
    poke_name = get_pokemon(pokemon_id)

    poke_menu.print_stars()
    print(f'Your searched drink is: {drink_string}')
    print(f'Your matching pokemon is: {poke_name}')

def convert_pokemon(convert_string):
    """
    Calculates the ID of a Pokémon based on the ascii codes of the drink name.
    """
    output_value = 1
    for i in range(len(convert_string)):
        output_value *= ord(convert_string[i])
        #ord function grabs the ascii value of a character.
    poke_id = output_value % MAX_POKEMON
    return poke_id

def get_pokemon(poke_id):
    """
    Uses the poké API to find a Pokémon based on given ID
    """
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{poke_id}')
    check_api(response)
    response_dict = dict(response.json())
    poke_name = response_dict['name']
    return poke_name

def get_drinkinput():
    """
    Vraagt naar een input en zoekt een overeenkomend drankje, geeft ook foutmeldingen.
    """
    while True:
        input_string = input("Please enter (part of) the name of a drink:")
        drink_response = requests.get(f'https://www.thecocktaildb.com/api/json/v1/1/search.php?s={input_string}')
        check_api(drink_response)
        drink_dict = drink_response.json()
        if input_string.isascii():
            if drink_dict['drinks'] is not None:
                break
            else:
                print("Can't find a valid drink, try again.")

    drink_string = drink_dict['drinks'][0]['strDrink']
    return drink_string

def check_api(response_name):
    """
    Checks if connection to the API was successful, if not, returns to the main menu of the program.
    """
    if response_name.status_code != 200:
        print('Something went wrong with finding a connection, returning to menu.')
        poke_main.main()