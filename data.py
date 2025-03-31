from urllib.request import urlopen
import requests
import json

def GetData(DataType):
  # Define the URL based on the DataType
  rawData = urlopen(f'https://api.openf1.org/v1/{DataType}')      
  data = json.loads(rawData.read().decode('utf-8'))
  return data

def GetDriverChampionshipPoints(year):
    url = f"http://api.jolpi.ca/ergast/f1/{year}/driverStandings.json"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        
        try:
            standings = data['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings']
            return standings
        except (KeyError, IndexError) as e:
            print("Error parsing data:", e)
            return None
    else:
        print("Error fetching data:", response.status_code)
        return None

