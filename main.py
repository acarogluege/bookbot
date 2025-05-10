from stats import get_word_count, count_character, chars_dict_to_sorted_list
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]

    print("============ BOOKBOT ============")
    print("Analyzing book found at " + file_path)
    
    # Word count section
    print("----------- Word Count ----------")
    word_count = get_word_count(filepath=file_path)
    print(f"Found {word_count} total words")
    
    # Character count section
    print("--------- Character Count -------")
    char_counts = count_character(filepath=file_path)
    sorted_chars = chars_dict_to_sorted_list(char_counts)
    
    # Print each character and its count
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["num"]
        if char.isalpha():  # Only print alphabetic characters
            print(f"{char}: {count}")
    
    print("============= END ===============")

main()