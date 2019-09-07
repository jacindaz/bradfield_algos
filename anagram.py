# Our first solution to the anagram problem will check whether each character
# in the first string occurs in the second. As we perform these checks, we’ll
# “check off” characters. If we can check off each character, then the two
# strings must be anagrams.

# We can check off a character by replacing it with the special Python value
# None. Since strings in Python are immutable, we need to convert the
# second string to a list. Each character from the first string will be checked
# against the characters in this list and, if found, checked off by replacement.



def anagram(string1, string2):
    """
    O(n^2), worst case iterates over entire str2
    for each time it iterates over entire str2
    """
    str1_list = list(string1)
    str2_list = list(string2)

    if len(str1_list) == len(str2_list):
        for char1 in str1_list:
            if char1 not in str2_list:
                return False
    else:
        return False

    return True

# print(anagram("earth", "heart")) # True
# print(anagram("earth", "hearta")) # True


def anagram_sort_and_compare(string1, string2):
    str1_list = list(string1).sort()
    str2_list = list(string2).sort()

    if str1_list == str2_list:
        return True
    else:
        return False


# Our final solution uses the fact that any two anagrams have the same number
# of a’s, the same number of b’s, the same number of c’s, and so on. First,
# we generate character counts for each string. If these counts match, the
# two strings are anagrams.

# Since there are 26 possible characters, we can use a list of 26 counters
# for each string. Each time we see a particular character, we’ll increment
# the counter at that character’s position. If the two lists are identical
# at the end, the strings must be anagrams.

def anagram_count_and_compare(string1, string2):
    """Jacinda's solution"""
    str1_counts = {}
    str2_counts = {}

    for char in string1:
        if str1_counts.get(char):
            str1_counts[char] += 1
        else:
            str1_counts[char] = 1

    for char2 in string2:
        if str2_counts.get(char2):
            str2_counts[char2] += 1
        else:
            str2_counts[char2] = 1

    return str1_counts == str2_counts

# print(anagram_count_and_compare("hearta", "haha"))
# print(anagram_count_and_compare("heart", "earth"))


def anagram_count_compare_bradfield_solution(s1, s2):
    c1 = [0] * 26
    c2 = [0] * 26

    for char in s1:
        # ord(char) gives the unicode integer
        pos = ord(char) - ord('a')
        c1[pos] += 1

    for char in s2:
        pos = ord(char) - ord('a')
        c2[pos] += 1

    for a, b in zip(c1, c2):
        if a != b:
            return False
    return True


from collections import Counter
def anagram_counter(string1, string2):
    """
    Counter makes an object of type Counter that is a
    dictionary with each char and a count of each char

    This solution is O(n), it sacrifices using more space
    than time, since it stores string1 and string2
    Counter objects
    """
    return Counter(string1) == Counter(string2)
