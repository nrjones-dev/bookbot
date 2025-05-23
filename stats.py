def count_words(book_text):
    word_count = 0
    for word in book_text.split():
        word_count += 1
    return word_count


def count_symbols(book_text):
    symbols = dict()

    for char in book_text:
        if char.lower() in symbols:
            symbols[char.lower()] += 1
        else:
            symbols[char.lower()] = 1

    return symbols


def sort_on(dict):
    return dict["num"]


def sort_lists(symbol_dict):
    symbol_list = []
    for key, value in symbol_dict.items():
        symbol_list.append({"name": key, "num": value})

    symbol_list.sort(reverse=True, key=sort_on)

    return symbol_list
