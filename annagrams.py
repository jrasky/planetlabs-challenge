#!/usr/bin/env python

WORDS = "/usr/share/dict/words"
PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61,
          67, 71, 73, 79, 83, 89, 97, 101]


def hash_word(word):
    """Takes a word and hashes it such that words with the same number of
    identical letters collide. Returns None if the word contains non-letter
    characters."""

    total = 1

    for char in word:
        value = ord(char.upper()) - 65
        if not 0 <= value <= 25:
            # word contains a non-letter character
            return None
        total *= PRIMES[value]

    return total


def create_table(word_file):
    """Reads the given file object one line at a time, creating the a hash
    table containing annagrams. Reads until the end of the file, returning the
    resulting table."""

    # hash table for the annagrams
    table = {}

    for word in word_file:
        # remove any whitespace on the ends of the word
        word = word.strip()

        # skip this word if it's not long enough
        if len(word) < 4:
            continue

        # has the word
        key = hash_word(word)

        # skip this word if it contains non-letter characters
        if key is None:
            continue

        table[key] = table.get(key, []) + [word]

    # return the resulting table
    return table


def strip_table(table):
    """Remove any annagram lists which contain less elements than the number
    of letters in the word. In-place, modifies table, returns None."""

    # in python, it's a bad idea to iterate over a changing list. For this
    # reason, we create a copy of the list of keys in table and iterate over
    # that, instead of over table itself.
    keys = table.keys()

    for key in keys:
        # all words in the list should have the same length, so we can just
        # assume the first one is the same length as all of them
        # all lists should also have at least one item, since they're only
        # created when a word is encountered
        if len(table[key]) < len(table[key][0]):
            del table[key]


def read_words():
    """Open the words file, and create a hash table from it. Return this
    table."""

    # open the dictionary
    words = open(WORDS)

    # create the table
    table = create_table(words)

    # strip the entries we don't want
    strip_table(table)

    # return the result
    return table


def print_annagrams(table):
    """Given a hash table of annagrams, print them out. Returns None"""

    for words in table.values():
        print ", ".join(words)


def main():
    # create the hash table
    table = read_words()

    # print them out
    print_annagrams(table)


# run main if we're the main module
if __name__ == "__main__":
    main()
