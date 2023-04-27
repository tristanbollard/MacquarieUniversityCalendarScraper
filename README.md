
# MacquarieUniversityCalendarScraper
This python script will scrape the Public Macquarie University Calendar on their website by using python. The [Macquarie University Public Calendar](https://www.mq.edu.au/study/admissions-and-entry/calendar) is used to see events that may come up such as "Results Publication Date" or "Last Date of Enrollment" for University Students. This script can also be used to get staff, finance, teaching, research and coursework for any of the campuses.This script has been confirmed to be working with Python 3.11.3 the prerequisites required for this script are:
 - Requests
 - BeautifulSoup
 - RE
 - JSON
 - ICS
 - dateutil.parser
 - datetime

Features that would be beneficial for this script:

 - [ ] A customizable filter for any group rather than MQ Uni Students.

Things to note:

 - This program spits out two files. One is a .json with **all the events** from the  website. The other which is an .ics file is the filtered output that can be injected into calendar applications.
