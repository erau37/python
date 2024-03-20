import re


def get_words_count(words_str):
    word_frequency = {}
    for word in words_str:
        word = word.lower()
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1
    return word_frequency


def main():
    with open('english_words.txt', 'r') as file:
        words_count = {}
        for line in file:
            words_str = re.sub(r'[^\w\s]', '', line).split()
            print(words_str)
            current_word_count = get_words_count(words_str)
            for word, count in current_word_count.items():
                if word in words_count:
                    words_count[word] += count
                else:
                    words_count[word] = count
    print(f"There are results: {words_count}")


main()
