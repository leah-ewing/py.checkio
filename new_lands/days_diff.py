"""

Given two dates as an array with three numbers - a year, month and day. (19 April 1982 == (1982, 4, 19)) 
Find the difference in days between the given dates. (Between today and tomorrow == 1 day)
The difference will always be either a positive number or zero, so don't forget about the absolute value.

Input: Two dates as tuples of integers.
Output: An integer.

Precondition: Dates between 1 January 1 and 31 December 9999. Dates are correct.


>>> days_diff((1982, 4, 19), (1982, 4, 22))
3

>>> days_diff((2014, 1, 1), (2014, 8, 27))
238

>>> days_diff((2014, 8, 27), (2014, 1, 1))
238

days_diff([1,1,1],[9999,12,31])
3652058

"""


def days_diff(a, b):

    from datetime import datetime

    date1 = []
    date2 = []

    for date in a:
        date1.append(str(date))
    for date in b:
        date2.append(str(date))

    if len(date1[0]) < 4 or len(date2[0]) < 4:
        if len(date1[0]) < 4:
            if len(date1[0]) == 3:
                date1[0] = '0' + date1[0]
            elif len(date1[0]) == 2:
                date1[0] = '00' + date1[0]
            elif len(date1[0]) == 1:
                date1[0] = '000' + date1[0]
        if len(date2[0]) < 4:
            if len(date2[0]) == 3:
                date2[0] = '0' + date2[0]
            elif len(date2[0]) == 2:
                date2[0] = '00' + date2[0]
            elif len(date2[0]) == 1:
                date2[0] = '000' + date2[0]
    
    date1 = "-".join(date1)
    date2 = "-".join(date2)

    date1 = datetime.strptime(date1, '%Y-%m-%d')
    date2 = datetime.strptime(date2, '%Y-%m-%d')

    difference = str(date2 - date1)

    if difference[0] == '-':
        difference = difference[1:]

    difference = difference.split(' ')
    answer = int(difference[0])

    print(answer)



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n🥳 ALL TESTS PASSED! YAY!\n')