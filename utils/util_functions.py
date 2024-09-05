def read_data():
    with open('words.txt', 'r', encoding='utf-8') as f:
        words = []  # List to store words
        for line in f:
            word = line.strip()
            words.append(word)
    return words

def write_data(word):
    with open('words.txt', 'a', encoding='utf-8') as f:
        f.write(word + '\n')
