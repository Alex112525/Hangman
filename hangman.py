import random

word_list = ['python', 'java', 'kotlin', 'javascript']

guess_word = random.choice(word_list)
letters = set(guess_word)
list_letters = list(guess_word)
guessed_letters = []
errors = 0

print("H A N G M A N\n")

while errors < 8:
    for let in list_letters:
        if let in guessed_letters:
            print(let, end="")
        else:
            print("-", end="")
    print("")
    letter = input("Input a letter:")

    if letter in letters:
        # if not repeat
        guessed_letters.append(letter)
    else:
        print("No such letter in the word")
    print("")
    errors += 1

print("""Thanks for playing!
We'll see how well you did in the next stage
""")
