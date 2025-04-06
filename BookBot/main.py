import sys

from stats import count_words, count_characters, sort_dictionary
from sys import argv

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]

    text = get_book_text(path)
    words = count_words(text)
    chars = count_characters(text)
    sorted_chars = sort_dictionary(chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
       key = item["key"]
       if key.isalpha():
           print(f"{key}: {item["num"]}")

    print("============= END ===============")

main()
