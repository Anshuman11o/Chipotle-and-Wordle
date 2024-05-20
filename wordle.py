# Author   : Anshuman Agarwal
# Email    : anagarwal@umass.edu
# Spire ID : 34157323

def get_guess():
    word_input = input("What word is this?: ")[:5]
    word = word_input.upper()
    return word
    
#print(get_guess())

def print_word(word):
    new_word = ""
    for i in word:
        new_word += i + ' '
    print(new_word.rstrip())

#print_word('TACOS')

def exact_match_compare(solution, guess):
    final_answer = ""
    x = 0
    for i in guess:
        if (i == solution[x]):
            final_answer+= '🟢'
        else:
            final_answer+= '🔴'
        x += 1
    return final_answer
#print(exact_match_compare('COULD', 'HORSE'))

def one_turn(solution):
    word = get_guess()
    print_word(word)
    print(exact_match_compare(solution, word))
    check = exact_match_compare(solution, word)
    if (check == '🟢🟢🟢🟢🟢'):
        print('Congratulations')
        exit()
#one_turn('COULD')

import random
def make_solution():
    random_words = ["WHICH", "THEIR", "THERE", "WOULD", "OTHER", "THESE", "ABOUT", "FIRST", "COULD", "AFTER"]
    word = random.choice(random_words)
    return word

#print(make_solution())


