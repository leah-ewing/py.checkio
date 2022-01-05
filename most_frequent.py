"""
You have a sequence of strings, and you’d like to determine the most frequently occurring string in the sequence. It can be only one.

Input: non empty list of strings.

Output: a string.

>>> most_frequent(['a', 'b', 'c', 'a', 'b', 'a'])
a

>>> most_frequent(['a', 'a', 'bi', 'bi', 'bi'])
bi

"""


def most_frequent(str):
    sorted_list = sorted(str)
    str_set = sorted(set(str))
    frequency = 0
    f_list = []
    i = 0

    
    while i < len(str_set) - 1:
        while len(sorted_list) > 0:
            if str_set[i] == sorted_list[0]:
                sorted_list.pop(0)
                frequency += 1
            else:
                f_list.append(frequency)
                frequency = 0
                i += 1
    f_list.append(frequency)

    max_frequency = max(f_list)

    for f in range(len(f_list)):
        if f_list[f] == max_frequency:
            answer = str_set[f]

    print(answer)
    


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n🥳 ALL TESTS PASSED! YAY!\n')
