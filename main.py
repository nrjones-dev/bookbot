import sys

from stats import count_symbols, count_words, sort_lists


def get_book_text(filepath):
    with open(filepath) as book:
        return book.read()


def main():
    book_file_path = sys.argv[1]
    book_text = get_book_text(book_file_path)

    word_count = count_words(book_text)
    symbol_count = count_symbols(book_text)
    symbol_count_list = sort_lists(symbol_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_file_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in symbol_count_list:
        if item.get("name").isalpha():
            symbol = item.get("name")
            count = item.get("num")
            print(f"{symbol}: {count}")
    print("============= END ===============")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    main()
