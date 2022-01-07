"""

Given an array of integers. Find the sum of the integers with even indexes (0th, 2nd, 4th...). 
Then multiply this summed number and the final element of the array together. 

For an empty array, the result will always be 0 (zero).

Input: A list of integers
Output: The number as an integer

Precondition: 0 ≤ len(array) ≤ 20 
all(isinstance(x, int) for x in array) 
all(-100 < x < 100 for x in array) 

>>> checkio([0, 1, 2, 3, 4, 5])
30

>>> checkio([1, 3, 5])
30

>>> checkio([6])
36

>>> checkio([])
0

"""

def checkio(array):
    even_indexes = []
    
    if len(array) == 0:
        answer = 0
    else:
        for i in range(len(array)):
            if i % 2 == 0:
                even_indexes.append(array[i])

        answer = sum(even_indexes) * array[-1]
    
    print(answer)



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n🥳 ALL TESTS PASSED! YAY!\n')