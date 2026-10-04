import sys

from stats import character_count, chars_dict_to_sorted_list, words_count


def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 {sys.argv[0]} <path_to_book>")
        sys.exit(1)
    
    num_words = words_count(get_book_text(sys.argv[1]))
    char_count = character_count(get_book_text(sys.argv[1]))
    sorted_char_list = chars_dict_to_sorted_list(char_count)
    print_report(sys.argv[1], num_words, sorted_char_list)


def get_book_text(file_path: str) -> str:
    with open(file_path) as file:
        file_contents = file.read()
        return file_contents

def print_report(book_path: str, word_count: int, sorted_list: list[tuple[str, int]]):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...\n----------- Word Count ----------\nFound {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        if item[0].isalpha():
            print(f"{item[0]}: {item[1]}")
        else:
            continue
    print("============= END ===============")

main()
