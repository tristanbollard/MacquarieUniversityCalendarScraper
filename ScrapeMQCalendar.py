import requests
from bs4 import BeautifulSoup
import re
import json
from ics import Calendar, Event
from dateutil.parser import parse as parse_date
from datetime import datetime, timedelta

url = "https://www.mq.edu.au/study/admissions-and-entry/calendar"

# Send a GET request to the URL
response = requests.get(url)
sydney_tz = 'Australia/Sydney'


# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find the script tag that contains the "important_dates" variable
script = soup.find("script", string=lambda t: "var important_dates" in t)

# Extract the value of the "important_dates" variable
start_index = script.text.find("[")
end_index = script.text.find("]")
important_dates = script.text[start_index:end_index+1]
important_dates = important_dates[:-2]
json_str = '{"important_dates": ' + important_dates + '] }'
print(json_str[50:])


# New JsonFile
with open("important_dates.json", "w") as f:
    f.write(json_str)

print("File saved as important_dates.json")

count = 0
# Open the JSON file
with open('important_dates.json') as f:
    data = json.load(f)
    
# Create a new calendar
cal = Calendar()
for event in data['important_dates']:
    if  event['location'] == 'North Ryde' and event['parent_calendar'] == 'Macquarie University' and (event['study_period'] == 'Session 1' or event['study_period'] == 'Session 2'):
        #print(event['date'] + event['date_name'])
        date_str = event['date']
        if date_str == 'TBC':
            continue  # skip events with "TBC" date value
        date_obj = datetime.strptime(date_str, '%d/%m/%Y')
        #print(date_obj)
        e = Event()
        e.name = event['date_name']
        e.begin = date_obj
        e.make_all_day()
        e.description = "Parent Calendar: " + event['parent_calendar'] + "\nStudy Period: " + event['study_period'] + "\nStudent Event: " + event['students']
        cal.events.add(e)
        count = count + 1
        print(e.begin, " - ", e.end)

# Save the calendar to an ICS file'
print(count)
with open('Session_1and2_MQ.ics', 'w') as f:
    f.write(str(cal))
    
