#!/usr/bin/python

import sys
import datetime

# This should be run with a Sunday as the start date.

sys.stderr.write('usage: %s <start year> <start month> <start day> <number of weeks> <schedule-MW, MWF, etc.>\n'%sys.argv[0])

try:
    start_date = datetime.date(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
except:
    sys.stderr.write('Bad time string.\n')
    sys.exit(-1)

try:
    weeks = int(sys.argv[4])
except:
    sys.stderr.write('Bad number of weeks.\n')
    sys.exit(-1)
    
try:
    schedule = sys.argv[5]
except:
    sys.stderr.write('Bad weekly schedule.\n')
    sys.exit(-1)
if schedule not in ['MW', 'TH', 'MWF']:
    sys.stderr.write('Bad weekly schedule.\n')
    sys.exit(-1)

print '''---
layout: page
title: Schedule
header: 
group: navigation
---
{% include JB/setup %}

<p>
Here is the tentative schedule for the class.
</p>

'''

print '<table class="table table-bordered table-hover">'
print '  <tr><td>#</td>'
if 'M' in schedule:
    print '''    <td>
      Monday
    </td>'''
if 'T' in schedule:
    print '''    <td>
      Tuesday
    </td>'''
if 'W' in schedule:
    print '''    <td>
      Wednesday
    </td>'''
if 'H' in schedule:
    print '''    <td>
      Thursday
    </td>'''
if 'F' in schedule:
    print '''    <td>
      Friday
    </td>'''
print '  </tr>'

# Loop over all days in the date range
d = start_date
one_day = datetime.timedelta(days=1)
week_count = 1
while d <= start_date + (weeks * one_day * 7) - one_day:
    if d.isoweekday() == 7:
        print '  <tr><td>%d</td>'%week_count
    if d.isoweekday() == 6:
        print '  </tr>'
        week_count += 1

    if (d.isoweekday() == 1 and 'M' in schedule) or \
       (d.isoweekday() == 2 and 'T' in schedule) or \
       (d.isoweekday() == 3 and 'W' in schedule) or \
       (d.isoweekday() == 4 and 'H' in schedule) or \
       (d.isoweekday() == 5 and 'F' in schedule):
        print '''    <td>
      <strong>%s</strong><br />
      Topic
    </td>'''%(d.strftime("%b %d"))
    d += one_day

print '</table>'
