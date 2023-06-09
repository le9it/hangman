import random
WORDLIST = []


def wordslist():

    with open('python/needed/New_words.txt', 'r') as file:   
        for word in file:
            WORDLIST.append(word.strip())
    RANDWORD = random.choice(WORDLIST)
    randList = list(RANDWORD)
    correct_guesses = ['_' for _ in range(len(RANDWORD))]

    return randList, RANDWORD, correct_guesses



def guess():
    guessed_character = input("Enter your first character: ").lower()

    return guessed_character

def livescheck(correct_guesses, RANDWORD, randList): 
    lives = len(RANDWORD)

    if lives == 0:
        print(f"You have lost the game. The word was: {RANDWORD.capitalize()}")

    if correct_guesses == randList:
        print("You won the game!")
    return lives


def compare(randList, correct_guesses, guessed_character, lives):
    
        
    found = False

    if guessed_character.isalpha() and len(guessed_character) == 1:
        for index, char in enumerate(randList):
            if guessed_character == char:
                correct_guesses[index] = guessed_character
                found = True
                    
        if found:
                print(f"The character '{guessed_character}' appears in the word!")
        if not found:
            print("The character doesn't appear in the word.")
            lives -= 1
            print(f"You have {lives} lives left")

    else:
        print("You must enter 1 character only")
    print("".join(correct_guesses).capitalize())
        

def hangman():
    randList, RANDWORD, correct_guesses = wordslist()
    print(f"You have {len(RANDWORD)} lives, good luck :D")
    print("".join(correct_guesses).capitalize())


    lives = livescheck(correct_guesses, RANDWORD, randList)
    while lives > 0 and correct_guesses != randList:
        guessed_character = guess()
        compare(randList, correct_guesses, guessed_character, lives)
        lives = livescheck(correct_guesses, RANDWORD, randList)

if __name__ == '__main__':
    hangman()
