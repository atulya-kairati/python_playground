import time
from load_dictionary import load

dictionary = '/usr/share/dict/words.txt'
word_list = load(dictionary)


def find_anagrams_of(word):
    word = word.lower()
    
    anagrams = list()
    for w in word_list:
        if sorted(w) == sorted(word) and w != word:
            anagrams.append(w)
    return anagrams


if __name__ == '__main__':
    word = input("Enter a word: ")
    init = time.time()
    print(find_anagrams_of(word))
    print(f'time: {time.time() - init}s')
