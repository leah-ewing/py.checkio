"""

Try to find out how many zeros a given number has at the end.

Input: A positive Int
Output: An Int.


>>> end_zeros(0)
1

>>> end_zeros(1)
0

>>> end_zeros(10)
1

>>> end_zeros(101)
0

"""


def end_zeros(num):
    number = str(num)
    i = -1
    neg_index = -(len(number))
    answer = 0

    if len(number) > 1:
        while i > neg_index:
            if number[i] == '0':
                answer += 1
                i -= 1
            else:
                break
    else:
        if number == '0':
            answer = 1
    
    print(answer)



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n🥳 ALL TESTS PASSED! YAY!\n')