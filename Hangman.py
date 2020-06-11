import random
print('H A N G M A N')
print()

def game_start():
    user_input = ''
    while user_input != 'exit':
        user_input = input('Type "play" to play the game, "exit" to quit: ')
        if user_input == "play":
            game()


def game():
    tries = 8
    print('\nH A N G M A N')
    word_list = ['python', 'java', 'kotlin', 'javascript']
    tried_letters = ''
    picked_word = random.choice(word_list)
    hidden_word = len(picked_word) * '-'
    while tries > 0:
        print()
        print(hidden_word)
        letter_input = str(input("Input a letter: "))
        if letter_input in picked_word and letter_input not in tried_letters:
            for x in range(len(picked_word)):
                if picked_word[x] == letter_input:
                    hidden_word = list(hidden_word)
                    hidden_word[x] = letter_input
                    hidden_word = ''.join(hidden_word)
                    tried_letters += letter_input
            continue
        else:
            if len(letter_input) > 1:  # double symbol
                print("You should input a single letter")
            elif (letter_input in hidden_word or letter_input in tried_letters) and letter_input != '-':  # same letter
                print('You already typed this letter')
                continue
            elif (letter_input.isalpha() and letter_input.isupper()) or letter_input.isupper() or not letter_input.isalpha():  # ascii
                print('It is not an ASCII lowercase letter')
                continue
            elif letter_input not in picked_word:  # not in the final word
                print("No such letter in the word")
                tried_letters += letter_input
                tries -= 1
        if '-' not in hidden_word:
            print('You guessed the word! ' + hidden_word)
            print("You survived!")
            break
    else:
        print("You are hanged!\n")


game_start()