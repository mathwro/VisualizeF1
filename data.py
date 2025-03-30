from urllib.request import urlopen
import json

def GetData(DataType):
  # Define the URL based on the DataType
  rawData = urlopen(f'https://api.openf1.org/v1/{DataType}')      
  data = json.loads(rawData.read().decode('utf-8'))
  return data
