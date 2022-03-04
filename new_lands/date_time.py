
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
    month = time.pop(0)
    
    time = time[0].split(' ')
    year = time.pop(0)
    
    time = time[0].split(':')
    hour = int(time[0])
    minute = int(time[1])

    
    if month == '01':
        month_written = 'January'
        month = month[1:]
    elif month == '02':
        month_written = 'February'
        month = month[1:]
    elif month == '03':
        month_written = 'March'
        month = month[1:]
    elif month == '04':
        month_written = 'April'
        month = month[1:]
    elif month == '05':
        month_written = 'May'
        month = month[1:]
    elif month == '06':
        month_written = 'June'
        month = month[1:]
    elif month == '07':
        month_written = 'July'
        month = month[1:]
    elif month == '08':
        month_written = 'August'
        month = month[1:]
    elif month == '09':
        month_written = 'September'
        month = month[1:]
    elif month == '10':
        month_written = 'October'
    elif month == '11':
        month_written = 'November'
    elif month == '12':
        month_written = 'December'
        
    if minute == 1:
        minute_written = 'minute'
    else:
        minute_written = 'minutes'
    
    if hour == 1:
        hour_written = 'hour'
    else:
        hour_written = 'hours'

    date_string = f"{day} {month_written} {year} year {hour} {hour_written} {minute} {minute_written}"
    return date_string
    
    

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n🥳 ALL TESTS PASSED! YAY!\n')