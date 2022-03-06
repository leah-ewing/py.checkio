"""

Joe Palooka has fat fingers, so he always hits the “Caps Lock” key whenever he actually intends to hit the key “a” by itself. 
(When Joe tries to type in some accented version of “a” that needs more keystrokes to conjure the accents, 
he is more careful in the presence of such raffinated characters ([Shift] + [Char]) and will press the keys correctly.) 

Compute and return the result of having Joe type in the given text. 
The “Caps Lock” key affects only the letter keys from “a” to “z” , and has no effect on the other keys or characters. 
“Caps Lock” key is assumed to be initially off.

For Joe's keyboard, Caps Lock is always uppercase a letter. 
That means if Caps Lock is on, and Joe does Shift + b - he gets 'B' (in upper case) printed.


Input: A string. The typed text.
Output: A string. The showed text after being typed.


>>> caps_lock("Why are you asking me that?")
Why RE YOU sking me thT?

>>> caps_lock("Madder than Mad Brian of Madcastle")
MDDER THn MD BRIn of MDCstle

>>> caps_lock("Aloha from Hawaii")
Aloh FROM HwII

>>> caps_lock("thank you")
thNK YOU

"""

def caps_lock(text):

    indexes = []
    lowercase = 'abcdefghijklmnopqrstuvwxyz'

    text_list = []
    for letter in text:
        text_list.append(letter)

    for i in range(len(text_list)):
        if text_list[i] == 'a':
            indexes.append(i)

    for i in range(len(indexes)):
        indexes[i] = indexes[i] - i

    for index in indexes:
        text_list.pop(index)

    index_ranges = []
    if len(indexes) % 2 == 0:
        i = 0
        while i < len(indexes) - 1:
            index_ranges.append([indexes[i], indexes[i + 1]])
            i += 2
    else:
        i = 0
        while i < len(indexes) - 2:
            index_ranges.append([indexes[i], indexes[i + 1]])
            i += 2
        index_ranges.append([indexes[-1]])

    if len(index_ranges[-1]) == 1:

        if len(index_ranges) == 1:
            only_a = index_ranges[0][0]

            if text_list[only_a] == ' ':
                only_a = only_a + 1

            if text_list[only_a] in lowercase:
                for j in range(only_a, len(text_list)):
                    text_list[j] = text_list[j].upper()
            else:
                for j in range(only_a, len(text_list)):
                    text_list[j] = text_list[j].lower()


        else:
            i = 0
            while i < len(index_ranges) - 1:

                first_a = index_ranges[i][0]
                second_a = index_ranges[i][1]

                if text_list[first_a] == ' ':
                    first_a += 1
                    next_letter = first_a + 1

                    if text_list[next_letter] in lowercase:
                        for j in range(first_a, second_a):
                            text_list[j] = text_list[j].upper()

                else:
                    if text_list[first_a] in lowercase:
                        for j in range(first_a, second_a):
                            text_list[j] = text_list[j].upper()
                    else:
                        for j in range(first_a, second_a):
                            text_list[j] = text_list[j].lower()

                last_a = index_ranges[-1][0]

                if text_list[last_a] == ' ':
                    next_letter2 = last_a + 1

                    if text_list[next_letter] in lowercase:
                        for j in range(last_a, len(text_list)):
                            text_list[j] = text_list[j].upper()
                    else:
                        for j in range(last_a, len(text_list)):
                            text_list[j] = text_list[j].lower()
                
                else:
                    if text_list[last_a] in lowercase:
                        for j in range(last_a, len(text_list)):
                            text_list[j] = text_list[j].upper()
                    else:
                        for j in range(last_a, len(text_list)):
                            text_list[j] = text_list[j].lower()

                i += 1

    else:
        i = 0
        while i < len(index_ranges):

            first_a = index_ranges[i][0]
            second_a = index_ranges[i][1]

            if text_list[first_a] == ' ':
                first_a + 1
                next_letter = first_a + 1

                if text_list[next_letter] in lowercase:
                    for j in range(first_a, second_a):
                        text_list[j] = text_list[j].upper()

            else:
                if text_list[first_a] in lowercase:
                    for j in range(first_a, second_a):
                        text_list[j] = text_list[j].upper()
                else:
                    for j in range(first_a, second_a):
                        text_list[j] = text_list[j].lower()
            i += 1

    text_list = "".join(text_list)
    print(text_list)



if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n🥳 ALL TESTS PASSED! YAY!\n")