import random

word_list = ['python', 'java', 'kotlin', 'javascript']
letter_list = list("qwertyuiopasdfghjklzxcvbnm")

guess_word = random.choice(word_list)
letters = set(guess_word)
list_letters = list(guess_word)
typed_letters = []
guessed_letters = []
errors = 0
win = False
play = True

winner = lambda x: x == len(letters)

print("H A N G M A N\n")

while play:
    game = input('Type "play" to play the game, "exit" to quit:')
    if game == "exit":
        play = False
    elif game == "play":
        while errors < 8 and not win:
            for let in list_letters:
                if let in guessed_letters:
                    print(let, end="")
                else:
                    print("-", end="")
            print("")

            letter = input("Input a letter:")

            if len(letter) != 1:
                print("You should print a single letter")
            else:
                if letter not in letter_list:
                    print("It is not an ASCII lowercase letter")
                else:
                    if letter not in typed_letters:
                        typed_letters.append(letter)
                        if letter in letters:
                            if letter not in guessed_letters:
                                guessed_letters.append(letter)
                        else:
                            print("No such letter in the word")
                            errors += 1
                    else:
                        print("You already typed this letter")
            if errors < 8:
                print("")
            win = winner(len(guessed_letters))

        if win:
            print(guess_word)
            print("You guessed the word! \nYou survived!")
        else:
            print("You are hanged!")
    print("")
