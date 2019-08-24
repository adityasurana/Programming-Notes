print("welcome to hangman game")
word = "EVAPORATE"
guess_word = '_' * len(word)
word = list(word)
guess_word = list(guess_word)
wrong_guess = []
letter = input("your guess:")
while True:
    if letter.upper() in word:
        index = word.index(letter.upper())
        guess_word[index] = letter.upper()
        word[index] = '_'

    elif letter.upper() in wrong_guess:
        print("already in wrong guess")
        letter = input("your guess:")

    else:

        print('  '.join(guess_word))
        if letter is not '':
            wrong_guess.append(letter.upper())
        letter = input("your guess:")

    if '_' not in guess_word:
        print("you won")
        break
    

   
