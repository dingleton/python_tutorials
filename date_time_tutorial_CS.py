# -*- coding: utf-8 -*-
"""
Python Date & time tutorial code

Taken/adatpted from youtube vbideo from Corey Schafer

Python 3.6
"""

import datetime
import pytz

#Examples using naieve date
d = datetime.date(2010, 7, 9)  #use regular integers only, not with a leading zero
print ("\nDate = {}".format(d))

#Print todays date, then the separate components e.g. year, day of week etc.
today = datetime.date.today()
print ("\nDate = {}".format(today))
print ("Year of today = {}".format(today.year))
print ("Month of today = {}".format(today.month))
print ("Day of today = {}".format(today.day))
print ("Weekday of today = {}".format(today.weekday())) # mon = 0, Sun = 6
print ("ISOWeekday of today = {}".format(today.isoweekday())) # mon = 1 sun = 7
print ("Timetuple of today = {}".format(today.timetuple()))

#Time delay
tdelta = datetime.timedelta(days=7)
print("\nThis day next week : {}".format(today+ tdelta))

hogmany_2017 = datetime.date(2017, 12, 31)
#datetime.date works on years, months days

datetime_to_end_year = hogmany_2017 - today
print("Datetime to end of year = {}".format(datetime_to_end_year))
print("Days to end of year = {}".format(datetime_to_end_year.days))
print("Seconds to end of year = {}".format(datetime_to_end_year.total_seconds()))

#datetime.time works on hours, minutes, seconds & microseconds
#it does not include : year, month, day

time_1 = datetime.time(9, 30, 12, 678)  #still naieve
print ("\nExample of datetime.time format = {}".format(time_1))
datetime_1 = datetime.datetime(2016, 2, 14, 11, 30, 45, 100000)
print ("datetime example = {}".format(datetime_1))
print ("datetime.date example = {}".format(datetime_1.date()))
print ("datetime.time example = {}".format(datetime_1.time()))

time_delta = datetime.timedelta(hours = 12)
print ("Add delta of 12 hours to datetime gives : {}".format(datetime_1 + time_delta))

dt_today = datetime.datetime.today()    #local time zone assumed
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()
print ("\ntd_today = \t{}\ndt_now = \t{}\ndt_utcnow = \t{}".format(dt_today, dt_now, dt_utcnow))

#Now start to use timezone info i.e. it's non-Naive
datetime_2 = datetime.datetime(2016, 6, 20, 6, 30, tzinfo = pytz.UTC)
dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print ("\ndatetime_2 = \t{} \ndt_now_2 = \t{}".format(datetime_2, dt_utcnow))

dt_usa_mountain = dt_utcnow.astimezone(pytz.timezone('US/Mountain'))
print ("\nTime zone corrected time for US/Mountain = \t{}".format(dt_usa_mountain))

#Print the date in ISO format 
print ("Mountain time in ISO format = \t{}".format(dt_usa_mountain.isoformat()))
print ("Mountain time re-formated = \t{}".format(dt_usa_mountain.strftime('%d, %B, %Y')))

#now convert a string to a time format
dt_str = '21, April, 2017'
dt_from_str = datetime.datetime.strptime(dt_str, '%d, %B, %Y')
print ('Datetime created from a string = {}'.format(dt_from_str))
