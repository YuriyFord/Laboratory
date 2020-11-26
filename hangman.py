# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string
<<<<<<< HEAD
import re
=======
>>>>>>> 6cfbdf27c62e488d61cfe936f719eefaae10c7e5

WORDLIST_FILENAME = r"D:\hangman_untracked_changes\words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    secret_word = secret_word.lower()
    secret_word_set = set(secret_word)
    letters_guessed = ''.join(letters_guessed)
    letters_guessed_set = set(letters_guessed)
    # Intersection of sets must form the letters of seret_word.
    if secret_word_set.intersection(letters_guessed_set) == secret_word_set:
        return True
    else:
        return False



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # Change the type of letters_guessed variable into the string.
    letters_guessed = "".join(letters_guessed)
    # Form a set of characters from the string.
    letters_guessed = set(letters_guessed)
    guessed_word = list()
    # Run through the each character of secret_word and find the equivalent one in letters_guessed list.
    for char in secret_word:
        if char in letters_guessed:
            guessed_word.extend(char)
        else:
            guessed_word.extend("_")
    guessed_word = ' '.join(guessed_word)
    return guessed_word


<<<<<<< HEAD
=======

>>>>>>> 6cfbdf27c62e488d61cfe936f719eefaae10c7e5
def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # Create a string of letters which are in letters_guessed list.
    letters_guessed = ''.join(letters_guessed)
    # Create a set of letters which are not in letters_guessed list.
    not_guessed_letters = set(string.ascii_lowercase) - set(letters_guessed)
    # Turn the type of not_guessed_letters variable into string
    not_letters_guessed = ''.join(not_guessed_letters)
    return not_letters_guessed
    
<<<<<<< HEAD
=======
    
>>>>>>> 6cfbdf27c62e488d61cfe936f719eefaae10c7e5

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive    feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    print('Wellcome to the Hangman!')
    length_word = len(secret_word)
    print(f'I am thinking of a word that is {length_word} letters long.')
    warnings_remaining = 3
    print(f'You have {warnings_remaining} warnings left.')
    guesses_remaining = 6
    letters_guessed = list()

    while guesses_remaining > 0:
        print('----------')
        print(f'You have {guesses_remaining} guesses left.')
        available_letters = get_available_letters(letters_guessed)
        print(f'available_letters: {available_letters}')
        guess = input("Please guess a letter:")
        guess = guess.lower()
        # The input which is acceptable.
        if guess.isalpha() == True and len(guess) == 1:
            if guess in letters_guessed:
                if warnings_remaining > 0:
                    warnings_remaining -= 1
                    print(f"Oops! You've already guessed that letter. You have {warnings_remaining} warnings left:")
                else:
                    guesses_remaining -= 1
                    print(f"Oops! You've already guessed that letter. You have no warnings left so you lose one guess:")
            elif guess in secret_word:
                print(f"Good guess:")
            elif guess not in secret_word:
                print('Oops! That letter is not in my word.')
                if guess in set('aoieu'):
                    guesses_remaining -= 2
                else:
                    guesses_remaining -= 1
            letters_guessed.extend(guess)
            print(f'{get_guessed_word(secret_word, letters_guessed)}')
            # Checking if the secret_word is guessed.
            if is_word_guessed(secret_word, letters_guessed) == True:
                unique_words = set(secret_word)
                unique_words = "".join(unique_words)
                score = (6 - warnings_remaining)*len(unique_words)
<<<<<<< HEAD
                result = f"Congratulations, you won! Your total score for this game is: {score}"
                return print(result)              
        # The input is non-alphabetic.
        else:
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print(f"That is not a valid letter. You have {warnings_remaining} warnings left:")
            else:
                guesses_remaining -= 1
                print(f"That is not a valid letter. You have no warnings left so you lose one guess:")
=======
                result = f"Congratulations, you won! Your total score for this game is: {score}"        
                
        # The input is non-alphabetic.
        else:
            if warnings_remaining > 0:
                print(f"That is not a valid letter. You have {warnings_remaining} warnings left:")
                warnings_remaining -= 1
            else:
                print(f"That is not a valid letter. You have no warnings left so you lose one guess:")
                guesses_remaining -= 1
>>>>>>> 6cfbdf27c62e488d61cfe936f719eefaae10c7e5

    if is_word_guessed(secret_word, letters_guessed) == False:
        result = f'Sorry, you ran out of guesses. The word was {secret_word}'
    return print(result)

<<<<<<< HEAD
=======

>>>>>>> 6cfbdf27c62e488d61cfe936f719eefaae10c7e5
# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
<<<<<<< HEAD
    word_only_letters = re.findall(r'[^_\s]', my_word)
    word_set = set(word_only_letters)
    other_word_set = set()
    word = re.findall(r'\S', my_word)
    empty_set = set()
    i = 0
    if len(word) == len(other_word):
        # Check if letters in both inputs can be the same
        while i < len(word):
            if word[i] not in other_word_set:
                if word[i] == other_word[i]:
                    i += 1
                elif word[i] == '_':
                    other_word_set.update({other_word[i]})
                    i += 1
                else:
                    return False
            else:
                return False
        
        if word_set.intersection(other_word_set) == empty_set:
            return True
        else:
            return False
    else:
        return False
=======
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass
>>>>>>> 6cfbdf27c62e488d61cfe936f719eefaae10c7e5



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
<<<<<<< HEAD
    dictionary = open(r'D:\hangman_untracked_changes\words.txt', 'r') 
    content = dictionary.read()
    all_chars = list()
    for char in content: 
        all_chars.append(char)
    all_chars = "".join(all_chars)
    all_words = all_chars.split(" ")
    matches = list()
    for el in all_words:
        if match_with_gaps(my_word, el) == True:
            matches.append(el)
        else:
            continue
    if len(matches) != 0:
        matches = " ".join(matches)
        return print(matches)
    else:
        return print("No matches found.")
=======
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass

>>>>>>> 6cfbdf27c62e488d61cfe936f719eefaae10c7e5


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
<<<<<<< HEAD
    print('Wellcome to the Hangman!')
    length_word = len(secret_word)
    print(f'I am thinking of a word that is {length_word} letters long.')
    warnings_remaining = 3
    print(f'You have {warnings_remaining} warnings left.')
    guesses_remaining = 6
    letters_guessed = list()

    while guesses_remaining > 0:
        print('----------')
        print(f'You have {guesses_remaining} guesses left.')
        available_letters = get_available_letters(letters_guessed)
        print(f'available_letters: {available_letters}')
        guess = input("Please guess a letter:")
        guess = guess.lower()
        # The input which is acceptable.
        if guess.isalpha() == True and len(guess) == 1:
            if guess in letters_guessed:
                if warnings_remaining > 0:
                    warnings_remaining -= 1
                    print(f"Oops! You've already guessed that letter. You have {warnings_remaining} warnings left:")
                else:
                    guesses_remaining -= 1
                    print(f"Oops! You've already guessed that letter. You have no warnings left so you lose one guess:")
            elif guess in secret_word:
                print(f"Good guess:")
            elif guess not in secret_word:
                print('Oops! That letter is not in my word.')
                if guess in set('aoieu'):
                    guesses_remaining -= 2
                else:
                    guesses_remaining -= 1
            letters_guessed.extend(guess)
            print(f'{get_guessed_word(secret_word, letters_guessed)}')
            # Checking if the secret_word is guessed.
            if is_word_guessed(secret_word, letters_guessed) == True:
                unique_words = set(secret_word)
                unique_words = "".join(unique_words)
                score = (6 - warnings_remaining)*len(unique_words)
                result = f"Congratulations, you won! Your total score for this game is: {score}"        
                return print(result)
        # Hints provided if "*" is called.
        elif guess == "*" and len(guess) == 1:
            print("Possible word matches are:")
            print(show_possible_matches(get_guessed_word(secret_word, letters_guessed)))
        # The input is non-alphabetic.
        else:
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print(f"That is not a valid letter. You have {warnings_remaining} warnings left:")
            else:
                print(f"That is not a valid letter. You have no warnings left so you lose one guess:")
                guesses_remaining -= 1

    if is_word_guessed(secret_word, letters_guessed) == False:
        result = f'Sorry, you ran out of guesses. The word was {secret_word}'
    return print(result)
=======
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass
>>>>>>> 6cfbdf27c62e488d61cfe936f719eefaae10c7e5



# When you've completed your hangman_with_hint function, comment the two similar
<<<<<<< HEAD
# Hints provided if "*" is called.
        
=======
>>>>>>> 6cfbdf27c62e488d61cfe936f719eefaae10c7e5
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
<<<<<<< HEAD
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)
=======
    secret_word = choose_word(wordlist)
    hangman(secret_word)
>>>>>>> 6cfbdf27c62e488d61cfe936f719eefaae10c7e5

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
<<<<<<< HEAD
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
=======
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
>>>>>>> 6cfbdf27c62e488d61cfe936f719eefaae10c7e5
