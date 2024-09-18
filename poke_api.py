import requests
import poke_menu as menu
POKEAPI_URL = 'https://pokeapi.co/api/v2/pokemon/'
#Declared in this file because of excessive usage in the code.

def call_api(url, param = ''):
    """
    Function that calls an api based on a base URL and a parameter. (custom input)
    """
    try:
        response = requests.get(f"{url}{param}")
        check_api(response)
        response_dict = response.json()
        return response_dict
    except requests.exceptions.ConnectionError:
        print('Cannot connect to API.')
        menu.ask_to_resume()

def check_api(response_name):
    """
    Checks if answer from the API was like expected, if not, returns to the main menu of the program.
    """
    if response_name.status_code != 200:
        print(f'Something went wrong with finding a connection. Error code: {response_name.status_code}')
        menu.ask_to_resume()
