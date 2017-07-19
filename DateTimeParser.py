# this function parses dates in almost any string formats given by user
# it takes the "time_sentence" as string from json file (no need to write any CFG for time_sentence
# it returns standard time
# to use this function, you need to install "datefinder" library
# File -> settings -> project interpreter -> add lib

import parsedatetime as pdt
c = pdt.Constants("en")
p = pdt.Calendar(c)
values = (c.uses24,                 # 24hr clock?
          c.usesMeridian,           # AM/PM used?
          c.usePyICU,               # was PyICU found/enabled?
          c.meridian,               # list of the am and pm values
          c.am,                     # list of the lowercase and stripped AM string
          c.pm,                     # list of the lowercase and stripped PM string
          c.dateFormats,            # dict of available date format strings
          c.timeFormats,            # dict of available time format strings
          c.timeSep,                # list of time separator, e.g. the ':' in '12:45'
          c.dateSep,                # list of date separator, e.g. the '/' in '11/23/2006'
          c.Months,                 # list of full month names
          c.shortMonths,            # list of the short month names
          c.Weekdays,               # list of the full week day names
          c.localeID                # the locale identifier
          )


def parse_dateTime(time_sentence):
    result = p.parseDT(time_sentence)
    return result
# test the function
"""
you can Copy/past the following example
please send sms at 9 pm to Hassan body take your medicine say it loudly
At 5 PM
At 5 PM tomorrow
5 hours after now
next Saturday
this saturday
"""
time_sentence1 = "March 24th"
while time_sentence1 != "finish":
    time_sentence1 = input("please,Copy/paste time_sentence \n")
    print("The standard time is :\n")
    print(parse_dateTime(time_sentence1))

