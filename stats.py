def words_count(text: str) -> int:
    words = text.split()
    return len(words)

def character_count(text: str) -> dict[str, int]:
    character_count = {}
    characters = list(text)
    lower_case = []
    for char in characters:
        if char.isalpha():
            lower_case.append(char.lower())
        else:
            lower_case.append(char)

    for char in lower_case:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1

    return character_count

# Other implementation was to implement a helper method called counter which accepts a char and gives us a int count back
# Using for loop, we can call helper method on each char and it will return a counter back.

def sort_on(char: tuple[str, int]) -> int:
    return char[1]

def chars_dict_to_sorted_list(char: dict[str, int]) -> list[tuple[str, int]]:
    empty_list = []
    for k, v in char.items():
        empty_list.append((k, v))

    sorted_list = sorted(empty_list, reverse=True, key=sort_on)
    return sorted_list
