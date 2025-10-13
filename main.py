from stats import get_book_text, num_words, unique_characters

def main():
    file_contents=get_book_text("books/frankenstein.txt")
    words = num_words("books/frankenstein.txt")
    unique_chars = unique_characters("books/frankenstein.txt")

    print(f"Found {words} total words")
    print(unique_chars)

if __name__ == "__main__":
    main()
