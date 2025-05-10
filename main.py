from stats import get_word_count
from stats import count_character
def main():
    words_found = f'{get_word_count("books/frankenstein.txt")} words found in the document'
    print(words_found)
    character_calculated = f'{count_character("books/frankenstein.txt")}'
    print(character_calculated)
main()



