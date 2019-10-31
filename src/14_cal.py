"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime
import argparse

# create initial set-up for argparse

parser = argparse.ArgumentParser(description="calendar tutorial")
parser.add_argument("--m", default=1, type=int,
                    help="This is the 'month' input", nargs="*")
parser.add_argument("--y", default=2019, type=int,
                    help="This is the 'year' input", nargs="*")

# parse command line arguments
args = parser.parse_args()
print("args: ", args)

month = args.m[0]
year = args.y[0]


print("month: ", month)
print("year: ", year)
# print("b: ", b)


def cal(input):
    print(input)


print(calendar.month(year, month))
