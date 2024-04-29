import nltk
from nltk.corpus import stopwords
from collections import Counter
import string


def read_file(file_path):
    
        with open(file_path, 'r') as file:
            text = file.read()
        return text
    
        

def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    translator = str.maketrans('', '', string.punctuation)
    words = nltk.word_tokenize(text.lower())
    filtered_words = [word.translate(translator) for word in words if word not in stop_words]
    return filtered_words


def count_word_frequencies(words):
    word_counts = Counter(words)
    return word_counts


def display_word_frequencies(word_counts):
    for word, count in word_counts.items():
        print(f"{word}: {count}")


def main():
    file_path = "random_paragraphs.txt"
    text = read_file(file_path)
    if text:
        words = preprocess_text(text)
        word_counts = count_word_frequencies(words)
        display_word_frequencies(word_counts)

if name == "main":
    main()

