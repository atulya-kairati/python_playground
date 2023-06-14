'''
Loads a text file into a list of lines

Arguments
- file: filename

Return
- List of lines in the file

Exceptions
- IOError

Libs
sys
'''

import sys

dictionary = '/usr/share/dict/words.txt'


def load(file_path) -> list:
    try:
        with open(file_path) as file:
            loaded_txt = file.read().strip().split('\n')
            loaded_txt = [w.lower() for w in loaded_txt]
            return loaded_txt
    except IOError as e:
        print(f'{e}\nError opening {file}. Exitting...', file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    print(len(load(dictionary)))
