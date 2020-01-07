# This program takes a user input message, and returns a censored message, if any of those words belong to a user-input file of censored words
from cs50 import get_string
import sys
import string


def main():
    # Ensures correct amount of user command line arguments
    if len(sys.argv) != 2:
        print("Usage: python bleep.py dictionary")
        sys.exit(1)

    # Ensures correct type of user command line arguments
    try:
        infile = open(sys.argv[1], 'r')
    except FileNotFoundError:
        print("Usage: python bleep.py dictionary")
        sys.exit(1)

    # Converts dictionary file to a temporary list
    wordset = set(line.strip() for line in infile)

    # Takes user input and converts it into a temporary list
    print("What message would you like to censor?")
    message = get_string("")
    message = message.split(' ')

    # Iterates through user input, printing words or censored equivalents after cross checking with the dictionary buffer list
    for word in message:
        if word.lower() in wordset:
            print(('*' * len(word)) + ' ', end='')
        else:
            print(word + ' ', end='')

    print('')


if __name__ == "__main__":
    main()
