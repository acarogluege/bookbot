def get_word_count(filepath):
    with open(filepath, 'r') as f:
        text = f.read()   
    stringify_text = text.split()
    total_words = len(stringify_text)
    return total_words


    