
"""

Convert the input date and time from computer format into a more readable format.
- Example: 21.05.2018 16:30 => 21 May 2018 year, 16 hours 30 minutes


>>> date_time('01.01.2000 00:00')
'1 January 2000 year 0 hours 0 minutes'

>>> date_time('19.09.2999 01:59')
'19 September 2999 year 1 hour 59 minutes'

>>> date_time('21.10.1999 18:01')
'21 October 1999 year 18 hours 1 minute'

"""

def date_time(time):
    
    time = time.split('.')
    day = int(time.pop(0))
    month = int(time.pop(0))
    
    time = time[0].split(' ')
    year = int(time.pop(0))
    
    time = time[0].split(':')
    hour = int(time[0])
    minute = int(time[1])

    
    if month == 1:
        month = 'January'
    elif month == 2:
        month = 'February'
    elif month == 3:
        month = 'March'
    elif month == 4:
        monthn = 'April'
    elif month == 5:
        month = 'May'
    elif month == 6:
        month = 'June'
    elif month == 7:
        month = 'July'
    elif month == 8:
        month = 'August'
    elif month == 9:
        month = 'September'
    elif month == 10:
        month = 'October'
    elif month == 11:
        month = 'November'
    elif month == 12:
        month = 'December'
        
    if minute == 1:
        minute_written = 'minute'
    else:
        minute_written = 'minutes'
    
    if hour == 1:
        hour_written = 'hour'
    else:
        hour_written = 'hours'

    date_string = f"{day} {month} {year} year {hour} {hour_written} {minute} {minute_written}"
    return date_string
    
    

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n🥳 ALL TESTS PASSED! YAY!\n')