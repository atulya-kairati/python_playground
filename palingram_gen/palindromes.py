'''
Finds all palindromes in a file
'''
from load_dictionary import load

dictionary = '/usr/share/dict/words.txt'

words = load(dictionary)
palindromes = [w for w in words if w == w[::-1]]

print(f'found {len(palindromes)} palindromes')
print(*palindromes, sep='\n')
