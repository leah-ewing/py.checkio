"""

Convert the time from the 24-hour format into 12-hour format by following the next rules: 
- the output format should be 'hh:mm a.m.' (for hours before noon) or 'hh:mm p.m.' (for hours after noon) 
- if hours is less than 10 - don't write a '0' before it. For example: '9:05 a.m.' 

Input: Time in a 24-hour format (as a string).
Output: Time in a 12-hour format (as a string).


>>> time_converter('12:30')
12:30 p.m.

>>> time_converter('09:00')
9:00 a.m.

>>> time_converter('23:15')
11:15 p.m.

>>> time_converter('00:00')
12:00 a.m.


"""

def time_converter(time):

    time = time.split(":")
    hour = int(time[0])
    minute = time[1]

    if hour >= 12:
        am_pm = 'p.m.'
        if hour != 12:
            hour = hour - 12
    
    else:
        am_pm = 'a.m.'
        if hour == 0:
            hour = 12

    time = (f"{hour}:{minute} {am_pm}")
    print(time)



if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n🥳 ALL TESTS PASSED! YAY!\n")