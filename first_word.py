"""

You are given a string and you have to find its first word.
- The input string consists of only English letters and spaces.
- There aren't any spaces at the beginning and the end of the string.

Input: A string.

Output: A string.

How it is used: The first word is a command in a command line.

Precondition: The text can contain a-z, A-Z and spaces.

>>> first_word("Hello World")
Hello

>>> first_word("a word")
a

>>> first_word("hi")
hi

"""


def first_word(text):

    text_list = text.split(" ")
    answer = text_list[0]
    
    print(answer)




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n🥳 ALL TESTS PASSED! YAY!\n')