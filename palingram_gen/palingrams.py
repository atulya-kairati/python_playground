import time
import load_dictionary

def find_palingrams():
    dictionary = '/usr/share/dict/words.txt'
    word_list = load_dictionary.load(dictionary)
    word_set = set(word_list)

    palingrams = []

    for word in word_list:
        for i in range(1, len(word) + 1):
            front = word[:i]
            front_rev = front[::-1]
            back = word[i:]

            # for palingrams like "nurses run", here the core word comes first
            if front_rev in word_set and back == back[::-1]:
                palingrams.append(word + ' ' + front_rev)
            
            # for palingrams like "stir grits", here the core word comes after
            back_rev = back[::-1]
            if back_rev in word_set and front == front[::-1]:
                palingrams.append(back_rev + ' ' + word)

    return palingrams


if __name__ == '__main__' :
    init = time.time()
    pals = find_palingrams()
    pals.sort()
    print(pals)
    print(f'found {len(pals)} palingrams')
    print(f'Took {time.time() - init} seconds')


