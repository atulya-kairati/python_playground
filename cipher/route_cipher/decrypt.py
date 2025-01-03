#! /usr/bin/bash

import sys

row_nums, col_nums = 5, 4

def read_key() -> list:
    with open('key', 'r') as file:
        key_str = file.read().strip()
        key = list(map(lambda n: int(n), key_str.split(',')))
        return key
        # return sorted(key, key=abs)

def load_and_parse(file_name) -> list[str]: 
    content = ''
    with open(file_name, 'r') as file:
        content = file.read().strip()

    content = content.split()

    return content
        
def decrypt(words: list[str]) -> str:
    key = read_key()

    words = list(reversed(words))
 
    word_mat = [list() for _ in range(row_nums)]
    for i in range(col_nums):
        direction = key[i]
        start, end, step = (0, row_nums, 1) if (direction > 0) else (row_nums - 1, -1, -1)

        for j in range(start, end, step):
            word_mat[j].append(words.pop())

    return ' '.join([' '.join(l) for l in word_mat])

    
def main():

    if len(sys.argv) < 2: raise Exception('Enter file name')

    file_name = sys.argv[1]

    words = load_and_parse(file_name)
    decrypted_text = decrypt(words)
    print(decrypted_text)



if __name__ == '__main__':
    main()

