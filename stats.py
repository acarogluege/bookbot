def get_word_count(filepath):
    with open(filepath, 'r') as f:
        text = f.read()   
    stringify_text = text.split()
    total_words = len(stringify_text)
    return total_words

def count_character(filepath, ):
    with open(filepath, 'r') as f:
        text = f.read().lower()
    stringify_text = text.split()
    char_counts = {}
    for word in stringify_text:
        for char in word:
            if char not in char_counts:
                char_counts[char] = 1
            else:
                char_counts[char] += 1
    return char_counts

def chars_dict_to_sorted_list(char_counts):
    chars_list = []
    # Convert each key-value pair to a dictionary
    for char, count in char_counts.items():
        chars_list.append({"char": char, "num": count})
    # Sort the list by the "num" value in descending order
    chars_list.sort(reverse=True, key=lambda x: x["num"])
    return chars_list