"""

Find the nearest value to the given one.

You are given a list of values as set form and a value for which you need to find the nearest one.

- If 2 numbers are at the same distance, you need to choose the smallest one;
- The set of numbers is always non-empty, i.e. the size is >= 1;
- The given value can be in this set, which means that it's the answer;
- The set can contain both positive and negative numbers, but they are always integers;
- The set isn't sorted and consists of unique numbers.

Input: Two arguments. A list of values in the set form. The sought value is an int.
Output: Int.

>>> nearest_value({4, 7, 10, 11, 12, 17}, 9)
10

>>> nearest_value({4, 7, 10, 11, 12, 17}, 8)
7

>>> nearest_value({4, 8, 10, 11, 12, 17}, 9)
8

>>> nearest_value({4, 9, 10, 11, 12, 17}, 9)
9

>>> nearest_value({4, 7, 10, 11, 12, 17}, 0)
4

>>> nearest_value({4, 7, 10, 11, 12, 17}, 100)
17

>>> nearest_value({5, 10, 8, 12, 89, 100}, 7)
8

>>> nearest_value({5}, 5)
5

>>> nearest_value({5}, 7)
5

"""

def nearest_value(values, one):
    number_plus = one + 1
    number_minus = one - 1

    if one in values:
        answer = one
    elif one > max(values):
        answer = max(values)
    elif one < min(values):
        answer = min(values)
    else:
        while number_plus < max(values) + 1: 
            if number_plus in values and number_minus not in values:
                answer = number_plus
                break
            if number_minus in values and number_plus not in values:
                answer = number_minus
                break
            if number_minus in values and number_plus in values:
                answer = number_minus
                break
            else:
                number_plus += 1
                number_minus -= 1

    print(answer)





if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n🥳 ALL TESTS PASSED! YAY!\n')

