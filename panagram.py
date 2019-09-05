import re

# Then, test your understanding with the following problem:
# a pangram is a phrase which contains every letter
# at least once, such as

# “the quick brown fox jumps over the lazy dog”.

# Write a function which determines if a given string is a pangram.



# Potential strategies:
# => array with alphabet, must find match
# => sort string alphabetically, take unique characters + regex
#    must find 26 matches
# =>

all_letters = "the quick brown fox jumps over the lazy dogs"
not_all_letters = "blah"

def is_panagram_1(phrase):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for letter in alphabet:
        if letter not in phrase.lower():
            return False
    return True

# print(is_panagram_1(all_letters))
# print(is_panagram_1(not_all_letters))


def is_panagram_2(phrase):
    phrase = ''.join(set(phrase.lower()))
    matches = re.findall('[a-z]', phrase)

    return len(matches) == 26

# print(is_panagram_2(all_letters))
# print(is_panagram_2(not_all_letters))


def is_panagram_3(phrase):
    matches = re.findall('[a-z]', phrase.lower())
    return len(set(sorted(matches))) == 26

# print(is_panagram_3(all_letters))
# print(is_panagram_3(not_all_letters))
