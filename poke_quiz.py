import random
import requests
answer_array = []

def run_quiz():
    add_randoms()
    print(answer_array)
    random_pokemon = get_randompokemon()
    print(random_pokemon)
    right_answer = match_drink(random_pokemon)
    print(answer_array)
    shuffle_answers()
    print(answer_array)
    print_options()
    answer = ask_answer()
    check_answer(answer, right_answer)


def add_randoms():
    for i in range(2):

        random_json = requests.get('https://www.thecocktaildb.com/api/json/v1/1/random.php')
        print(random_json.json())
        drink_dict = random_json.json()
        drink_string = drink_dict['drinks'][0]['strDrink']
        answer_array.append(drink_string)
        print(answer_array)

def shuffle_answers():
    random.shuffle(answer_array)

def get_randompokemon():
    random_id = random.randint(1,1025)
    print (random_id)
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{random_id}')
    response_dict = dict(response.json())
    poke_name = response_dict['name']
    return poke_name

def match_drink(poke_name):
    drink_letter = poke_name[0]
    if drink_letter == 'u' or drink_letter == 'x':
        drink_letter = poke_name[1]
    drink_response = requests.get(f'https://www.thecocktaildb.com/api/json/v1/1/search.php?f={drink_letter}')
    print(drink_response.status_code)
    print(drink_response.json())
    drink_dict = drink_response.json()
    drink_id = convert_drink(poke_name, len(drink_dict['drinks']))
    print('Your drink is:', drink_dict['drinks'][drink_id]['strDrink'])
    answer_array.append(drink_dict['drinks'][drink_id]['strDrink'])
    return drink_dict['drinks'][drink_id]['strDrink']

def convert_drink(convert_string,length = 1):
    '''
    Calculeert een passende drink ID nummer gebasseerd op zijn (binnen de gebasseerd op de ascii waarde van de letters in een string.
    '''
    output_value = 1
    for i in range(len(convert_string)):
        output_value += ord(convert_string[i])

    drink_id = output_value % length
    return drink_id

def print_options():
    for i in range(1,4):
        print(f'Option:{i} {answer_array[i-1]}')

def ask_answer():
    while True:
        answer = input('Please submit your answer: ')
        if answer == '1' or answer == '2' or answer == '3':
            return answer
        else:
            print('Please input a valid answer.')

def check_answer(answer, right_answer):

    answer = int(answer)
    if answer_array[answer - 1] == right_answer:
        print('Correct!')
    else:
        print('Incorrect!')


