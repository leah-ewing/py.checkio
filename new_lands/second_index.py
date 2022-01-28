"""

Given two strings, find an index of the second occurrence of the second string in the first one.

Input: Two strings
Output: Int or None

>>> second_index("sims", "s")
3

>>> second_index("find the river", "e")
12

>>> second_index("hi", " ")
None

"""

def second_index(text, symbol):
    i = 0
    indexes = []

    while i < len(text):
        if text[i] == symbol:
            indexes.append(i)
        i += 1

    if len(indexes) >= 2:
        answer = indexes[1]
    else:
        answer = None
    
    print(answer)



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n🥳 ALL TESTS PASSED! YAY!\n')
