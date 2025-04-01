import json
import pandas as pd

def prettyPrintJson(data):
  for session in data:
    print(json.dumps(session, indent=4))
    
def getLastX(data, sortkey='date_start', reverse=False, count=3):
  return sorted(data, key=lambda x: x[sortkey], reverse=reverse)[:count]

def applyFilters(data, filters):
  filtered_sessions = None
  for key, value in filters.items():
    if value:  # Only apply if the filter has a value
        filtered_sessions = [session for session in data if session.get(key) == value]
  return filtered_sessions

def prettyPrintDriverStandings(data):
    for driver in data:
        # Extracting the position, points, and driver name correctly
        position = driver.get('position', 'N/A')
        points = driver.get('points', '0')
        name = f"{driver['Driver'].get('givenName', 'Unknown')} {driver['Driver'].get('familyName', 'Unknown')}"
        print(f"{position}. {name} - {points} points")

def rowTeamColor(row):
  if row['Constructor'] == 'Alpine F1 Team':
    return ['background-color: #0093CC'] * len(row)
  elif row['Constructor'] == 'Aston Martin':
    return ['background-color: #229971'] * len(row)
  elif row['Constructor'] == 'Ferrari':
    return ['background-color: #E80020'] * len(row)
  elif row['Constructor'] == 'Haas F1 Team':
    return ['background-color: #B6BABD'] * len(row)
  elif row['Constructor'] == 'McLaren':
    return ['background-color: #FF8000'] * len(row)
  elif row['Constructor'] == 'Mercedes':
    return ['background-color: #27F4D2'] * len(row)
  elif row['Constructor'] == 'RB F1 Team':
    return ['background-color: #6692FF'] * len(row)
  elif row['Constructor'] == 'Red Bull':
    return ['background-color: #3671C6'] * len(row)
  elif row['Constructor'] == 'Sauber':
    return ['background-color: #52E252'] * len(row)
  elif row['Constructor'] == 'Williams':
    return ['background-color: #64C4FF'] * len(row)
  else:
    return ['background-color: #FFFFFF'] * len(row)