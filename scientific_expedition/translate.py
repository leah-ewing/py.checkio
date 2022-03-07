"""

Stephan has a friend who happens to be a little mechbird. 
Recently, he was trying to teach it how to speak basic language. 
Today the bird spoke its first word: "hieeelalaooo". 
This sounds a lot like "hello", but with too many vowels. 
Stephan asked Nikola for help and he helped to examine how the bird changes words. 
With the information they discovered, we should help them to make a translation module.

The bird converts words by two rules: 
- After each consonant letter the bird appends a random vowel letter (l ⇒ la or le);
- After each vowel letter the bird appends two of the same letter (a ⇒ aaa);
(Vowels letters == "aeiouy")

You are given an ornithological phrase as several words which are separated by white-spaces (each pair of words by one whitespace). 
The bird does not know how to punctuate its phrases and only speaks words as letters. 
All words are given in lowercase. You should translate this phrase from the bird language to something more understandable.

Input: A bird phrase as a string.
Output: The translation as a string.


>>> translate('hieeelalaooo')
hello

>>> translate('hoooowe yyyooouuu duoooiiine')
how you doin

>>> translate('aaa bo cy da eee fe')
a b c d e f

>>> translate('sooooso aaaaaaaaa')
sos aaa

>>> translate("zy")
z

>>> translate("aaa")
a


"""


def translate(text):

    vowels = 'aeiouy'
    new_list = []

    letter_list = []
    for letter in text:
        letter_list.append(letter)
    text = letter_list

    if len(text) > 2:
        i = 0
        while i < len(text) - 2:
            if text[i] not in vowels:
                new_list.append(text[i])
                i += 1
            else:
                if text[i] == text[i + 1] and text[i] == text[i + 2]:
                    new_list.append(text[i])
                    i += 3

                else:
                    i += 1

        if text[-1] != new_list[-1] or text[-2] != new_list[-1]:
            new_list.append(text[-2])

    else:
        new_list.append(text[0])

    new_list = "".join(new_list)
    print(new_list)




if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n🥳 ALL TESTS PASSED! YAY!\n")