from stats import word_count

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    # print(text) - previous part
    print(f"{word_count(text)} words found in the document")

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()