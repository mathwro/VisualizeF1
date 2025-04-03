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

def colorRow(row):
    # Get the color for the constructor name, defaulting to white if not found
    color = GetTeamColor(row['Constructor'])
    return [f'background-color: {color}'] * len(row)
  
def GetTeamColor(constructor_name):
    team_colors = {
        'Alpine F1 Team': '#0093CC',
        'Aston Martin': '#229971',
        'Ferrari': '#E80020',
        'Haas F1 Team': '#B6BABD',
        'McLaren': '#FF8000',
        'Mercedes': '#27F4D2',
        'RB F1 Team': '#6692FF',
        'Red Bull': '#3671C6',
        'Sauber': '#52E252',
        'Williams': '#64C4FF'
    }
    # return 
    return team_colors.get(constructor_name, '#FFFFFF')  # Default to white if not found