import random
from words import words


def get_random_words():
    # Getting a random word from the word list
    word = random.choice(words)
    return word.upper()


def user_guess(hangman_word):
    #print(hangman_word)
    #print(type(hangman_word))
    tries = 6
    previous_tries = []
    game_over = False
    # setting all values in the list to underscore _
    word_list = ["_" for i in range(len(hangman_word))]
    while not game_over:
        # *word_list opens the list and sets the separators to ' '
        print("Words tried: ", end='')
        print(*previous_tries, sep=',')
        print(display_hangman(tries))
        print(*word_list, sep=' ')
        word_guess = input("\nGuess the word : ")

        if word_guess not in previous_tries:
            previous_tries.append(word_guess)

        for i in range(len(hangman_word)):
            if hangman_word[i] == word_guess.upper():
                # deleting the placeholder value
                del word_list[i]
                # adding the letter to the index location of the letter in the original word
                word_list.insert(i, word_guess.upper())

        if hangman_word.count(word_guess.upper()) > 0:
            display_hangman(tries)
        else:
            tries = tries - 1
            display_hangman(tries)

        # counting the number of underscores in the list
        if word_list.count("_") == 0:
            print(f'Congrats you have guess the word: {hangman_word.capitalize()}')
            game_over = True
        elif tries == 0:
            print(f'You did not guess the word: {hangman_word.capitalize()}')
            print(display_hangman(tries))
            game_over = True


def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
        # head, torso, both arms, and one leg
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
        # head, torso, and both arms
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
        # head, torso, and one arm
        """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
        # head and torso
        """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
        # head
        """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
        # initial empty state
        """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


if __name__ == '__main__':
    hangman_word = get_random_words()
    play_again = 'Y'
    user_guess(hangman_word)
    while play_again.upper() != 'N' or play_again.upper() != 'Y':
        play_again = input("Would you like to play again?, enter Y or N: ").upper()
        if play_again.upper() == 'N':
            break
        elif play_again.upper() == 'Y':
            hangman_word = get_random_words()
            user_guess(hangman_word)

#hint
