"""while loop practice"""

__author__: str = "730643371"


def num_instances(phrase: str, search_char: str) -> int:
    count: int = 0
    if len(search_char) == 1:
        length_phrase: int = 0
        while length_phrase < len(phrase):  # needed to be < not <=
            if phrase[length_phrase] == search_char:
                count = count + 1
            length_phrase = length_phrase + 1
        print(count)
    else:
        print(search_char + " is not one letter")
    return count
