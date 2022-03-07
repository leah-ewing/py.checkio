"""

Given a text and a list of words, check if the words in a list appear in the same order as in the given text.
- A word from the list is not in the text - your function should return False;
- Any word can appear more than once in a text - use only the first one;
- If two words in the given list are the same - your function should return False;
- The condition is case sensitive, which means 'hi' and 'Hi' are two different words;
- The text includes only English letters and spaces.

Input: Two arguments. The first one is a given text, the second is a list of words.
Output: A bool.

>>> words_order('hi world im here', ['world', 'here'])
True

>>> words_order('hi world im here', ['here', 'world'])
False

>>> words_order('hi world im here', ['world'])
True

>>> words_order('hi world im here', ['world', 'here', 'hi'])
False

>>> words_order('hi world im here', ['world', 'im', 'here'])
True

>>> words_order('hi world im here', ['world', 'hi', 'here'])
False

>>> words_order('hi world im here', ['world', 'world'])
False

>>> words_order('hi world im here', ['country', 'world'])
False

>>> words_order('hi world im here', ['wo', 'rld'])
False

>>> words_order('', ['world', 'here'])
False

"""


def words_order(text, words):

    text = text.split(' ')
    indexes = []


    for word in words:
        if word in text:
            indexes.append(text.index(word))
        else:
            print(False)
            break

    if len(indexes) > 0:
        if sorted(indexes) == indexes and len(set(indexes)) == len(indexes):
            print(True)
        else:
            print(False)



if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n🥳 ALL TESTS PASSED! YAY!\n")


