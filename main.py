from stats import get_book_text, num_words, unique_characters, sorted_list

def main():
    file_contents=get_book_text("books/frankenstein.txt")
    words = num_words("books/frankenstein.txt")
    unique_chars = unique_characters("books/frankenstein.txt")
    unique_chars = sorted_list(unique_chars)


    print(f"Found {words} total words")
    for char, count in unique_chars:
        print(f"{char}: {count}")

if __name__ == "__main__":
    main()
