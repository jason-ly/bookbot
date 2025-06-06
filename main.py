import sys
from stats import (
   word_count, 
   character_count,
   sorted_dict,
)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) #Exit the program with a non-zero status to inidcate an error.
    book_path = sys.argv[1] #Uses the second argument as the book path.
    text = get_book_text(book_path)
    num_words = word_count(text)
    char_counts = character_count(text)
    sorted_chars = sorted_dict(char_counts)
    print_report(book_path, num_words, sorted_chars)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def print_report(book_path, num_words, sorted_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        if not item["char"].isalpha():
                continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

main()