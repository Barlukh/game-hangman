""" Main file of the game. Game starts automatically through the start() function. """

from wonderwords import RandomWord
from string import ascii_lowercase

def generate_word():
    """ Generate and return a random word (noun). """
    w_inst = RandomWord()
    game_word = w_inst.word(include_categories=["noun"])
    return game_word

def new_game():
    """ Play a new game. """
    word = list(generate_word())
    masked_word = list("_" * len(word))
    wrong_answers = 0
    while True:
        hangman_drawing(wrong_answers)
        word_drawing(masked_word)
        if wrong_answers < 6:
            user_letter = input("Guess a letter: ")
            if user_letter not in ascii_lowercase or len(user_letter) > 1:
                separator()
                print("")
                print(f'"I can\'t accept \'{user_letter}\', it must be a single lowercase letter!"')                           
            elif user_letter in masked_word:
                separator()
                print("")
                print('"You have already revealed that letter!"')
            elif user_letter in word:
                for i in range(len(word)):
                    if user_letter == word[i]:
                        masked_word[i] = user_letter
                separator()
                print("")
                print(f'"By my beard! Letter \'{user_letter}\' is a right guess!"')
                if "_" not in masked_word:
                    hangman_drawing(wrong_answers)
                    word_drawing(masked_word)
                    print(f'"You got all the letters, the word was indeed \'{"".join(word)}\'."')
                    print("")
                    break
            else:
                wrong_answers += 1
                separator()
                print("")
                print(f'"What a shame, letter \'{user_letter}\' is a wrong guess!"')
        else:
            print(f'"How is it hangin\', outlander? The word was \'{"".join(word)}\'. Do you want to try again, or are you a chicken?"')
            print("")
            break     

def separator():
    """ Print a separation line for visual purposes. """
    print("____________________________________________________________________")

def word_drawing(masked_word):
    """ Print the word and all revealed letters. """
    masked_word = " ".join(masked_word)
    print(masked_word)
    print("")

def hangman_drawing(wrong_answers: int):
    """ Print the the Hangman figure based on wrong_answers parameter. """
    base0 = "  +---+"
    base1 = "  |   |"
    base2 = "      |"
    base3 = "      |"
    base4 = "      |"
    base5 = "      |"
    base6 = "========="
    space = ""
    base = [space, base0, base1, base2, base3, base4, base5, base6, space]
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
        print(f"{space}\n{base0}\n{base1}\n{wrong1}\n{base3}\n{base4}\n{base5}\n{base6}\n{space}")
    elif wrong_answers == 2:
        print(f"{space}\n{base0}\n{base1}\n{wrong1}\n{wrong2}\n{base4}\n{base5}\n{base6}\n{space}")
    elif wrong_answers == 3:
        print(f"{space}\n{base0}\n{base1}\n{wrong1}\n{wrong3}\n{base4}\n{base5}\n{base6}\n{space}")
    elif wrong_answers == 4:
        print(f"{space}\n{base0}\n{base1}\n{wrong1}\n{wrong4}\n{base4}\n{base5}\n{base6}\n{space}")
    elif wrong_answers == 5:
        print(f"{space}\n{base0}\n{base1}\n{wrong1}\n{wrong4}\n{wrong5}\n{base5}\n{base6}\n{space}")
    elif wrong_answers == 6:
        print(f"{space}\n{base0}\n{base1}\n{wrong1}\n{wrong4}\n{wrong6}\n{base5}\n{base6}\n{space}")

def help():
    """ Print available commands for the player to use. """
    print("1 : new game")
    print("0 : exit\n")

def player_input(player_name: str):
    """ Call to print operational commands from the help() function and ask the player for an input. """
    while True:
        help()
        try:
            player_command = int(input("Please enter a choice: "))
        except ValueError:
            separator()
            print("")
            print("Wrong choice, only 1 or 0 allowed.")
            print("")
            continue
        if player_command != 0 and player_command != 1:
            separator()
            print("")
            print("Wrong choice, only 1 or 0 allowed.")
            print("")
        elif player_command == 0:
            separator()
            print("")
            print(f'"May the roads lead you to warm places, {player_name}. Live long and prosper!"')
            print("")
            break
        elif player_command == 1:
            separator()
            print("")
            print('"Keep your feet on the ground and hold on to your chair!"')
            new_game()

def start():
    """ Print a welcoming text and ask the player for a name. """
    print('"Welcome, outlander. Take a seat by the fire and leave your burdens at the door.')
    print('Come, the wind is freezing outside, let\'s cheer up our spirits with a little game.')
    print('Now, what is your name, outlander?"\n')
    player_name = input("Please enter your name: ")
    print("")
    print(f'"Very well, {player_name}, I am thinking of a word, your task is to guess the letters of the word one by one.')
    print('After each failed attempt, I will draw a piece of a \'Hangman\'. Once finished, you lose.')
    print(f'Now, are you up to the challenge, {player_name}?"\n')
    player_input(player_name)

start()