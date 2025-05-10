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