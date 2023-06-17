import time
import sys
from collections import Counter
from load_dictionary import load

dictionary = '/usr/share/dict/words.txt'
word_list = load(dictionary)
word_list.extend(['a', 'i'])
init_name = input("Enter a name: ").lower()
word_set = set(word_list)

def find_anagram_words(name, word_set):
    """Find words that can be formed using letters in the name"""
    print('Finding words...')
    name_counter = Counter(name)

    anagram_words = []
    for word in word_set:
        word_counter = Counter(word)
        
        for l in word_counter:
            if word_counter[l] > name_counter[l]:
                break
        else:
            anagram_words.append(word)

    print(*anagram_words, sep='\n')
    print()
    print("Remaining letters = {}".format(name))
    print("Number of remaining letters = {}".format(len(name)))
    print("Number of remaining (real word) anagrams = {}".format(len(anagram_words)))
    return set(anagram_words)
    

def process_choice(name):
    '''Check user choice validity and return user choice and leftover letters'''
    while True:
        choice = input('\nEnter the chosen word or s to start over and q to quit: ').lower() 

        if choice == 's':
            main()
        elif choice == 'q':
            sys.exit()
        else:
            in_name = all(map(lambda x: x in name, choice))
            if choice not in word_set or not in_name:
                print('\nNig nog! Wrong choice. Try again', file=sys.stderr)
                continue
            candidate = choice.lower().strip()

        left_over_list = list(name)
        for letter in candidate:
            left_over_list.remove(letter)

        name = ''.join(left_over_list)
        return choice, name

def main():
    global word_set
    word_set = set(word_list)
    name = ''.join(filter(lambda x: x not in {' ', '-'}, init_name))
    limit = len(name)
    print(limit)
    phrase = ''

    while True:
        temp_phrase = phrase.replace(' ', '')
        if len(temp_phrase) < limit:
            word_set = find_anagram_words(name, word_set)
            
            print(f'Current phrase: {phrase}')

            choice, name = process_choice(name)

            phrase += choice + ' '
            print(f'Current phrase: {phrase}')

        else:
            print(f'\n\nFinished!\nAnagram for {init_name} is "{phrase.strip()}"\n')
            
            try_again = input('Enter n to try again else press enter to exit: ').lower().strip() == 'n'
            if try_again:
                main()
            else:
                print('Bye! ...And fuck you.')
                sys.exit()


if __name__ == '__main__':
   main() 
