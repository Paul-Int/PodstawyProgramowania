def time_string(hours, minutes, time_format):
    if time_format == 24:
        return f'{hours:02}:{minutes:02}'
    else:
        period = 'AM'
        if hours >= 12:
            period = 'PM'
        display_hours = hours % 12
        if display_hours == 0:
            display_hours = 12
        return f'{display_hours}:{minutes:02} {period}'
       
print('24-hour format:', time_string(13, 10, 24))
print('12-hour format:', time_string(13, 10, 12))