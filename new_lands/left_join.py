"""

Given a sequence of strings, join these strings into a chunk of text where the initial strings are separated by commas. 
Replace all cases of the words "right" with the word "left", even if it's a part of another word. 
All strings are given in lowercase.

Input: A sequence of strings
Output: The text as a comma-separated string

Precondition: 0 < len(phrases) < 42


>>> left_join(("left", "right", "left", "stop"))
'left,left,left,stop'

>>> left_join(("bright aright", "ok"))
'bleft aleft,ok'

>>> left_join(("brightness wright",))
'bleftness wleft'

>>> left_join(("enough", "jokes"))
'enough,jokes'

"""


def left_join(phrases):
    
    new_phrase = ','.join(phrases)
    new_phrase = new_phrase.replace("right", "left")

    # print(new_phrase)
    return new_phrase
    




# left_join(("left", "right", "left", "stop")) # => "left,left,left,stop"
# left_join(("bright aright", "ok")) # => "bleft aleft,ok"
# left_join(("brightness wright",)) # => "bleftness wleft"
# left_join(("enough", "jokes")) # => "enough,jokes"


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n🥳 ALL TESTS PASSED! YAY!\n')