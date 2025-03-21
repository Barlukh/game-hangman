"""
Project Title: Hangman
Filename: main.py

Description:
    A classic game of Hangman. Guess the letters of the hidden word.
    The game is played in the terminal, execute with main.py.
    The only required dependency is the module wonderwords.
"""

__author__ = "Boris Gazur"
__version__ = "1.0.0"
__date__ = "March 20, 2025"

from wonderwords import RandomWord
from string import ascii_lowercase

def main():
    """ Main function. Call to main() at the end of this file executes the program. """
    player_name = intro()
    while True:
        choice = player_input()
        if choice == 0:
            end_game(player_name)
        else:
            new_game(player_name)

def intro():
    """ Print a welcoming text and ask the player for a name. """
    separator()
    print('"Welcome to the Hangman game!"\n')
    player_name = input('Please enter your name: ')
    separator()
    print(f'"Very well, {player_name}, I am thinking of a word,\ntry to guess the letters of the word one by one.')
    print('After each failed attempt, I will draw a piece of a Hangman.\nOnce finished, you lose. If you guess the word, you win."\n')
    return player_name

def separator():
    """ Print a separation line for visual purposes. """
    print('-' * 70)

def player_input():
    """ Print available commands from the help_commands() function and ask the player for an input. """
    while True:
        help_commands()
        try:
            player_command = int(input('Please enter a choice: '))
            if player_command not in (0, 1):
                raise ValueError('Invalid value')
        except ValueError:
            separator()
            print('Wrong choice, only 1 or 0 allowed.\n')
            continue

        if player_command == 0:
            return 0
        elif player_command == 1:
            return 1

def help_commands():
    """ Print available commands for the player to use. """
    print("1 : new game")
    print("0 : exit\n")

def end_game(player_name: str):
    """ Print a goodbye message and exit() the program. """
    separator()
    print(f'"I hope to see you again, {player_name}."')
    separator()
    exit()

def new_game(player_name: str):
    """ Start a new game: generate a word, create masked mirror, loop until win or lose condition is met. """
    separator()
    word = list(generate_word())
    masked_word = list("_" * len(word))
    wrong_answers = 0
    while wrong_answers < 6:
        hangman_drawing(wrong_answers)
        word_drawing(masked_word)
        user_letter = input('\nGuess a letter: ')
        separator()
        if user_letter not in ascii_lowercase or len(user_letter) != 1:
            print(f'"I can\'t accept \'{user_letter}\', it must be a single lowercase letter!"')                           
        elif user_letter in masked_word:
            print('"You have already revealed that letter!"')
        elif user_letter in word:
            for i in range(len(word)):
                if user_letter == word[i]:
                    masked_word[i] = user_letter
            print(f'"Yes! Letter \'{user_letter}\' is a right guess!"')
            if "_" not in masked_word:
                break
        else:
            wrong_answers += 1
            print(f'"What a shame, letter \'{user_letter}\' is a wrong guess!"')
    
    hangman_drawing(wrong_answers)
    word_drawing(masked_word)
    if wrong_answers != 6:
        print(f'\n"You got all the letters, the word was indeed \'{"".join(word)}\'."\n')
    else:
        print(f'\n"Sorry {player_name}, the word was \'{"".join(word)}\'. Do you want to try again?"\n')

def generate_word():
    """ Generate and return a random word (english noun). """
    w_inst = RandomWord()
    game_word = w_inst.word(include_categories=["noun"])
    return game_word

def hangman_drawing(wrong_answers: int):
    """ Print the Hangman figure based on wrong_answers value. """
    base0 = "  +---+"
    base1 = "  |   |"
    base2 = "      |"
    base6 = "========="
    space = ""
    base = [space, base0, base1, base2, base2, base2, base2, base6, space]
    wrong1 = "  O   |"
    wrong2 = "  |   |"
    wrong3 = " /|   |"
    wrong4 = r" /|\  |"
    wrong5 = " /    |"
    wrong6 = r" / \  |"

    if wrong_answers == 0:
        for i in range(9):
            print(base[i])
    elif wrong_answers == 1:
        print(f"{space}\n{base0}\n{base1}\n{wrong1}\n{base2}\n{base2}\n{base2}\n{base6}\n{space}")
    elif wrong_answers == 2:
        print(f"{space}\n{base0}\n{base1}\n{wrong1}\n{wrong2}\n{base2}\n{base2}\n{base6}\n{space}")
    elif wrong_answers == 3:
        print(f"{space}\n{base0}\n{base1}\n{wrong1}\n{wrong3}\n{base2}\n{base2}\n{base6}\n{space}")
    elif wrong_answers == 4:
        print(f"{space}\n{base0}\n{base1}\n{wrong1}\n{wrong4}\n{base2}\n{base2}\n{base6}\n{space}")
    elif wrong_answers == 5:
        print(f"{space}\n{base0}\n{base1}\n{wrong1}\n{wrong4}\n{wrong5}\n{base2}\n{base6}\n{space}")
    elif wrong_answers == 6:
        print(f"{space}\n{base0}\n{base1}\n{wrong1}\n{wrong4}\n{wrong6}\n{base2}\n{base6}\n{space}")

def word_drawing(masked_word):
    """ Print the word in its current revealed form. """
    masked_word = " ".join(masked_word)
    print(masked_word)

if __name__ == '__main__':
    main()