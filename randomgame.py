from random import randint
import sys

def init_random_game():

    try:
        first = int(sys.argv[1])
        last = int(sys.argv[2])
        num_gen = randint(first, last)
        if first < 0 or last < 0 or first >= last:
            raise ValueError()
    except ValueError:
        print('\nYou cannot do that\n')
    else:
        while True:
                try:
                    number = int(input(f'\nGuess a number between {first} and {last}:    '))
                except ValueError:
                    print("\nPlease input actual numbers\n")
                    continue
                else:
                    if num_gen == number:
                        print('\nCORRECT!!! ~ Well done!\n')
                        break
                    else:
                        print('\nWrong ~ Guess again...\n')

init_random_game()