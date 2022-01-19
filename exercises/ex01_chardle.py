"""<3<3 to the UTAs"""

__author__ = "730409578"

from operator import index
from re import search


word_to_check: str = input("Enter a 5-character word: ")
if len(word_to_check) != 5:
    print("Error: Word must contain five characters")
    exit()

search_letter: str = input("Enter a single character: ")
if len(search_letter) != 1:
    print("Error: Character must be a single character")
    exit()

occurences: int = 0

print("Searching for " + search_letter + " in " + word_to_check)

if word_to_check[0] == search_letter:
    print(search_letter + " found at index 0")
    occurences = occurences + 1
if word_to_check[1] == search_letter:
    print(search_letter + " found at index 1")
    occurences = occurences + 1
if word_to_check[2] == search_letter:
    print(search_letter + " found at index 2")
    occurences = occurences + 1
if word_to_check[3] == search_letter:
    print(search_letter + " found at index 3")
    occurences = occurences + 1
if word_to_check[4] == search_letter:
    print(search_letter + " found at index 4")
    occurences = occurences + 1

if occurences == 0:
    print("No instances of " + search_letter + " found in " + word_to_check)
elif occurences == 1:
    print("1 instance of " + search_letter + " found in " + word_to_check)
else:
    occurences_print = str(occurences)
    print(occurences_print + " instances of " + search_letter + " found in " + word_to_check)