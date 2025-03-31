import json

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

