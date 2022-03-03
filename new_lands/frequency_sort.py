"""

Sort the given iterable so that its elements end up in the decreasing frequency order, that is, the number of times they appear in elements. 
If two elements have the same frequency, they should end up in the same order as the first appearance in the iterable.

Input: Iterable
Output: Iterable


>>> frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])
[4, 4, 4, 4, 6, 6, 2, 2]

>>> frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])
['bob', 'bob', 'bob', 'carl', 'alex']

>>> frequency_sort([])
[]

>>> frequency_sort([1])
[1]

"""


def frequency_sort(items):
    items_list = sorted(items)
    word_counts = []
    word_list = []

    if sorted(items) == sorted(list(set(items))):
        print(items)
        
    else:
        i = 0
        while len(items_list) > 1:
            word_counts.append(1)
            if items_list[0] == items_list[1]:
                word_counts[i] += 1
            else:
                i += 1
                word_list.append(items_list[0])

            items_list.pop(0)

        word_list.append(items_list[0])
        word_counts = word_counts[0:len(word_list)]
        words_and_counts = []

        i = 0
        while i < len(word_list):
            words_and_counts.append([word_list[i], [word_counts[i]]])
            i += 1
        
        word_counts = sorted(word_counts)
        sorted_words_and_counts = []

        i = 0
        while i < len(word_counts):
            for item in words_and_counts:
                if item[1][0] == word_counts[i] and item not in sorted_words_and_counts:
                    sorted_words_and_counts.insert(0, item)
            i += 1

        new_list = []

        i = 0
        while i < len(sorted_words_and_counts):
            for item in items:
                if item == sorted_words_and_counts[i][0]:
                    new_list.append(item)
            i += 1

        print(new_list)



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n🥳 ALL TESTS PASSED! YAY!\n')