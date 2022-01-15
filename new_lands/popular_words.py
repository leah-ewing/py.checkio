"""

Determine the popularity of certain words in the text.

You are given 2 arguments: the text and the array of words the popularity of which you need to determine.

- The words should be sought in all registers. This means that if you need to find a word "one" then words like "one", "One", "oNe", "ONE" etc. will do.
- The search words are always indicated in the lowercase.
- If the word wasn't found even once, it has to be returned in the dictionary with 0 (zero) value.

Input: The text and the search words array
Output: The dictionary where the search words are the keys and values are the number of times when those words are occurring in a given text.

>>> popular_words('When I was One I had just begun When I was Two I was nearly new', ['i', 'was', 'three', 'near'])
{'i': 4, 'was': 3, 'three': 0, 'near': 0}


"""

def popular_words(text, words):

    i = 0
    popular = {}

    text = text.lower().split(' ')

    while i < len(words):
        word_count = 0

        for word in text:
            if word == words[i]:
                word_count += 1

        popular[words[i]] = word_count 

        i += 1

    print(popular)





if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n🥳 ALL TESTS PASSED! YAY!\n')