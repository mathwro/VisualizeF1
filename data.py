from urllib.request import urlopen
import requests
import json

def GetChampionshipPoints(year, type):
    url = f"http://api.jolpi.ca/ergast/f1/{year}/{type}.json"
    response = requests.get(url)

    if response.status_code == 200:
        try:
            data = response.json()
            standings = None

            # Safely navigate the JSON structure
            if type == 'driverStandings':
                standings_lists = data.get('MRData', {}).get('StandingsTable', {}).get('StandingsLists', [])
                if standings_lists:
                    standings = standings_lists[0].get('DriverStandings', [])
            elif type == 'constructorStandings':
                standings_lists = data.get('MRData', {}).get('StandingsTable', {}).get('StandingsLists', [])
                if standings_lists:
                    standings = standings_lists[0].get('ConstructorStandings', [])
            else:
                print("Invalid type specified.")

            return standings
        except (KeyError, IndexError, ValueError) as e:
            print("Error parsing data:", e)
            return None
    else:
        print("Error fetching data:", response.status_code)
        return None

