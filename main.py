from stats import get_word_count
from stats import count_character

def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")

    words_found = f'Found {get_word_count("books/frankenstein.txt")} total words'
    print("----------- Word Count ----------")
    print(words_found)


    character_calculated = f'{count_character("books/frankenstein.txt")}'
    print("----------- Character Count -----------")
    print(character_calculated)

main()



