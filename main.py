from urllib.request import urlopen
import json
#import streamlit as st

#drivers = urlopen('https://api.openf1.org/v1/drivers')
#driverdata = json.loads(driverdata.read().decode('utf-8'))

sessions = urlopen('https://api.openf1.org/v1/sessions')
sessiondata = json.loads(sessions.read().decode('utf-8'))
# Filter out sessions without 'date_start' field
valid_sessions = [session for session in sessiondata if 'date_start' in session]

# Sort sessions by date and get the 3 most recent ones
session3 = sorted(valid_sessions, key=lambda x: x['date_start'], reverse=True)[:3]

# Pretty print the session data
for session in session3:
    print(json.dumps(session, indent=4))

# Get a list of all active drivers full names
#driverlist = [driver['full_name'] for driver in data]

print(session3)
#print(drivers)