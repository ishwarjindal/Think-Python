#This script will fetch the current time and then determine number of days elapsed

import time

current_time = time.time()
print('Current Time is ' + str(current_time))

#Constants
seconds_in_minute = 1 * 60
seconds_in_hour = 1 * 60 * seconds_in_minute
seconds_in_day = 1 * 24 * seconds_in_hour

#Days elapsed since 01-Jan-1970 00:00:00
days_elapsed = current_time // seconds_in_day
total_seconds_left = current_time % seconds_in_day

#Hours elapsed since today's 00:00:00
hours_elapsed = total_seconds_left // (60*60)
total_seconds_left = total_seconds_left % (60*60)

#Minutes elapsed since last hour of today
minutes_lapsed = total_seconds_left // (60)

#Seconds elapsedafter last minute of today
total_seconds_left = total_seconds_left % 60

print(str(int(days_elapsed)) + ' days ' + str(int(hours_elapsed)) + ' hour ' + str(int(minutes_lapsed)) + ' minute ' + str(int(total_seconds_left)) + ' seconds elapsed since 01-Jan-1970 00:00:00')

