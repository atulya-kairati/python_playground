#! /usr/bin/bash

'''
route cipher works by replacing few words with keys and then jumbling them

It jumbles them by arranging the words in a 4x5 matrix and and then reads 
each column either from top or bottom. The value in key file decides that

Ex: if key is -1,-3,2,4 or -1,2-3,4
Then 1st and 3rd column are read from bottom to top and 2nd and 4th from top to bottom  

> Place the text in note.txt. And make sure the no of words <= 20 (mat is 4x5)
> If its less than 20 then remaining sapce will filled with "filler"
'''

import sys

row_nums, col_nums = 5, 4
total_words = row_nums * col_nums

def read_key() -> list:
    with open('key', 'r') as file:
        key_str = file.read().strip()
        key = list(map(lambda n: int(n), key_str.split(',')))
        return key
        # return sorted(key, key=abs)

def load_and_parse_note(file_name) -> list[list[str]]: 
    content = ''
    with open(file_name, 'r') as file:
        content = file.read().strip()

    content = content.split()
    if len(content) > total_words: raise Exception("note.txt should have <= 20 words")
    
    content += ['filler'] * (total_words - len(content))
    
        
    # create word matrix
    words = []
    for i, word in enumerate(content):
        j = i // col_nums

        if len(words) <= j: words.append(list())

        words[j].append(word)

    return words
        
def encrypt(words: list[list]) -> str:
    key = read_key()

    text = ''
    for col, direction in enumerate(key):
        start, end, step = (0, len(words), 1) if (direction > 0) else (len(words) - 1, -1, -1)

        for i in range(start, end, step): 
            text += ' ' + words[i][col]        
        
    return text.strip()

def main():

    if len(sys.argv) < 2: raise Exception('Enter file name')

    file_name = sys.argv[1]

    words = load_and_parse_note(file_name)
    encrypted_text = encrypt(words)
    print(encrypted_text)


if __name__ == '__main__':
    main()

