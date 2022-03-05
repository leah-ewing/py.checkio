"""

A median is a numerical value separating the upper half of a sorted array of numbers from the lower half. 
In a list where there are an odd number of entities, the median is the number found in the middle of the array. 
If the array contains an even number of entities, then there is no single middle value, 
instead the median becomes the average of the two numbers found in the middle.
 
Given a non-empty array of natural numbers, find the median.

Input: An array as a list of integers.
Output: The median as a float or an integer.

>>> median([1, 2, 3, 4, 5])
3

>>> median([3, 1, 2, 5, 3])
3

>>> median([1, 300, 2, 200, 1])
2

>>> median([3, 6, 20, 99, 10, 15])
12.5

"""

def median(data):
    data = sorted(data)
    
    if len(data) % 2 == 0:
        index1 = int(len(data)/2)
        index2 = int(index1 - 1)
        median_num = (data[index1] + data[index2]) / 2
    else:
        median_num = data[int(len(data)/2)]
    print(median_num)


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n🥳 ALL TESTS PASSED! YAY!\n")