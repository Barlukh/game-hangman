![screenshot](screenshot.png)

## Introduction
A simple game of Hangman. The game is only text-based in the command line. It has a simple functionality and is a copy of the classic Hangman game idea.

## Functionality
- The computer picks a random word from the Wonderwords module and presents the player with blank spaces equal to the length of the word.
- The player tries to guess the letters of the word one by one.
- If the player guesses a letter that is not present in the word, the computer draws a piece of the Hangman figure.
- Once fully drawn, the player loses. The code repeats but gives the option to the player to exit after the game.
- The player wins if he correctly guesses all the letters in the word, therefore revealing the whole word.
- The player input is protected to only insert valid parameters. The game also has some role-playing text for flavour.

## Installation
No installation. Run the code in main.py. The game starts automatically through the start() function.
