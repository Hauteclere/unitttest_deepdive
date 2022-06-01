import random

def get_input(prompt):
    input_value = input(prompt)
    if input_value == "\quit":
        raise KeyboardInterrupt
    return input_value

def get_a_number(prompt):
    result = None
    while result is None:
        user_input = get_input(prompt)
        try:
            result = int(user_input)
        except ValueError:
            print("That wasn't a number, please try again.")
    return result

def guess_the_number(the_number):
    user_guess = get_a_number("Guess the number I'm thinking of!: ")
    while user_guess != the_number:
        user_guess = get_a_number("That wasn't quite right, try again! Don't forget, you can quit any time by typing '\quit'.: ")
    else:
        print(f"That's correct it was {the_number}!\n\n")

def prompt_play(text_insert):
    choice = get_input(f"""Let's play {text_insert} game! I'll think of a number between 0 and 10, and you have to guess it. You can quit any time by typing '\quit'.
Press Enter to begin: """)

def main_loop():
    text_insert = "a"
    try:
        while True:
            prompt_play(text_insert)
            text_insert="another"
            guess_the_number(random.randint(0, 10))
    except KeyboardInterrupt:
        print("Ok, see you next time!")

