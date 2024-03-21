#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics:

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" 
<status code> <file size> (if the format is not this one, the line must be skipped)

After every 10 lines and/or a keyboard interruption (CTRL + C), print these statistics from the beginning:
Total file size: File size: <total size>
where <total size> is the sum of all previous <file size> (see input format above)
Number of lines by status code:
possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
if a status code doesn’t appear or is not an integer, don’t print anything for this status code
format: <status code>: <number>
status codes should be printed in ascending order
"""

import sys

"""Store the status code count in a dic3t"""
status_dict = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
               '404': 0, '405': 0, '500': 0}
total_size = 0
count = 0 # keep count of numbers of line counted

try:
    for line in sys.stdin:
        line_list = line.split(" ")

        if len(line_list) > 4:
            status_code = line_list[-2]
            file_size = int(line_list[-1])
            
            """Check if status_code receive exists and increment the count"""
            if status_code in status_dict.keys():
                status_dict[status_code] += 1

            """Update total size"""
            total_size += file_size
            count += 1

        if count == 10:
            count = 0 # reset count
            print('File size: {}'.format(total_size))

            """Print out the status code counts"""
            for key, value in sorted(status_dict.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))

except Exception as err:
    pass

finally:
    print('File size: {}'.format(total_size))
    for key, value in sorted(status_codes_dict.items()):
        if value != 0:
            print('{}: {}'.format(key, value))
        