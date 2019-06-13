#!python
from icalendar import Calendar
import datetime
import requests
import sys
events=[]
now=(datetime.date.today())
DateDict = {}
try:
	url="https://a.wunderlist.com/api/v1/ical/20433434-bm0levog7ddoqoo22f487svn1d.ics"
except IndexError:
	print("No URL given...")
	sys.exit()
try:
	cal = Calendar.from_ical(requests.get(url).text)
except:
	print("Can't fetch .ics file, sorry...")
for e in cal.walk('vevent'):
    delta=e.get('dtstart').dt-now
    event=[e.get('summary'),(delta.days)]
    events.append(event)
events.sort(key=lambda x:x[1])
for e in events:
	print('['+str(e[1])+']  '+e[0])
