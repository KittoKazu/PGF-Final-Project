import random
import poke_api
import poke_menu as menu
import poke_pokemon_to_drink
import poke_drink_to_pokemon
from poke_api import POKEAPI_URL

RANDOM_DRINK_URL = 'https://www.thecocktaildb.com/api/json/v1/1/random.php'
answer_array = []
#Array globally predeclared to prevent bugs with local variables.

def run_quiz():
    """
    Displays an intro to the quiz subsystem then
    """
    menu.print_stars()
    print('Welcome to the quiz game subsystem!')
    menu.print_stars()

    answer_array.clear()
    #Reset the answer array to prevent bugs when looping the entire program.
    choice = choose_quiz_type()
    point_to_question(choice)

def choose_quiz_type():
    """
    Asks the user what type of question they'd want.
    """
    print('Please choose the type of quiz \nGuess drink with Pokemon [1]\nGuess Pokemon with drink [2]')
    while True:
        quiz_choice = input('Which type of quiz would you like to choose?: ')
        if quiz_choice in ['1','2']:
            #Instead of using multiple if statements we check if the input is present in a list.
            return quiz_choice
        else:
            menu.print_stars()
            print('Please enter a valid option.')

def point_to_question(choice):
    """
    Points to the right question type
    """
    if choice == '1':
        run_drink_quiz()
    else:
        run_pokemon_quiz()

def run_pokemon_quiz():
    """
    Runs the Pokémon quiz, making sure all required functions are called.
    """
    menu.print_stars()
    print('Welcome to the Pokemon quiz!')
    question_type = ask_question_type()
    question_drink = pick_drink(question_type)
    menu.print_stars()
    print(f'Your drink is: {question_drink}')
    right_answer = poke_drink_to_pokemon.convert_to_pokemon(question_drink)

    answer_array.append(right_answer)
    add_random_pokemon()
    random.shuffle(answer_array)

    print_options()
    answer = ask_answer()
    check_answer(answer, right_answer)
    print(f'The right answer was: {right_answer.capitalize()}')

def run_drink_quiz():
    """
    Runs the drink quiz, making sure all required functions are called.
    """
    menu.print_stars()
    print('Welcome to the drink quiz!')
    question_type = ask_question_type()
    question_pokemon = pick_pokemon(question_type)
    menu.print_stars()
    print(f'Your Pokemon is: {question_pokemon.capitalize()}')
    right_answer = poke_pokemon_to_drink.convert_to_drink(question_pokemon)

    answer_array.append(right_answer)
    add_random_drinks()
    random.shuffle(answer_array)

    print_options()
    answer = ask_answer()
    check_answer(answer, right_answer)
    print(f'The right answer was: {right_answer}')

def ask_question_type():
    """
    Asks the user to input what type of question they'd like
    """
    print('Please choose the type of question you would like to choose. \nRandom Question [1] \nPredetermined question [2]')
    question_type = input('Please enter your desired question type: ')
    while True:
        if question_type in ['1','2']:
            #Instead of using multiple if statements we check if the input is present in a list.
            return question_type
        else:
            menu.print_stars()
            print('Please enter a valid option.')

def pick_pokemon(question_type):
    """
    Checks what type of question was selected, and decides if a random Pokémon must be generated.
    """
    if question_type == '1':
        pokemon_name = get_random_pokemon()
    else:
        pokemon_name = 'charizard'
    return pokemon_name

def pick_drink(question_type):
    """
    Checks what type of question was selected, and decides if a random drink must be generated.
    """
    if question_type == '1':
        drink_name = get_random_drink()
    else:
        drink_name = 'Pina Colada'
    return drink_name

def get_random_pokemon():
    """
    Generates a random ID to find a corresponding Pokémon, returns the name of a random Pokémon.
    """
    random_id = random.randint(1,1025)
    #Generates random ID between 1 and 1025
    response_dict = poke_api.call_api(POKEAPI_URL, random_id)
    #Calls the Poke API with the generated id
    poke_name = response_dict['name']
    return poke_name

def get_random_drink():
    """
    Picks a random drink and returns its name.
    """
    drink_dict = poke_api.call_api(RANDOM_DRINK_URL)
    drink_string = drink_dict['drinks'][0]['strDrink']
    return drink_string

def add_random_drinks():
    """
    Fills array of answers with two extra random drinks.
    """
    for i in range(2):
        drink_string = get_random_drink()
        answer_array.append(drink_string)

def add_random_pokemon():
    """
    Fills array of answers with two extra random Pokémon.
    """
    for i in range(2):
        random_pokemon = get_random_pokemon()
        answer_array.append(random_pokemon)

def print_options():
    """
    Prints out the possible answers to the user, labeled 1 to 3
    """
    for i in range(1,4):
        print(f'Option [{i}]: {answer_array[i-1].capitalize()}')

def ask_answer():
    """
    Takes answer input from user and checks if it is a valid answer.
    """
    while True:
        answer = input('Please submit your answer: ')
        if answer in ['1','2','3']:
            #Instead of using multiple if statements we check if the input is present in a list.
            return answer
        else:
            print('Please input a valid answer.')

def check_answer(answer, right_answer):
    """
    Checks if the answer is correct. And tells the user if they were correct.
    """

    answer = int(answer)
    menu.print_stars()
    if answer_array[answer - 1] == right_answer:
        print('Your answer is Correct!')
    else:
        print('Your answer is Incorrect!')