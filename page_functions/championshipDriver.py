import data, util
import streamlit as st
import pandas as pd
from datetime import datetime

def driver_championship_page():
    st.title("Driver Championship")
    standings = data.GetChampionshipPoints(datetime.now().year, 'driverStandings')
    if standings:
        df = ConvertToDataFrame_Driver(standings)
        # Set the index before styling
        df = df.set_index('Position')
        # Apply team colors but also set text to black and bold
        styled_df = df.style.apply(util.colorRow, axis=1).set_properties(**{
            'color': 'black',
            'font-weight': 'bold'
        })
        st.table(styled_df)
    else:
        st.error("Failed to fetch driver championship data.")
        
def ConvertToDataFrame_Driver(data):
    driver_data = []
    for driver in data:
        driver_data.append({
            'Position': driver.get('positionText', '-'),
            'Driver': f"{driver.get('Driver', {}).get('givenName', '')} {driver.get('Driver', {}).get('familyName', '')}",
            'Points': driver.get('points', '0'),
            'Wins': driver.get('wins', '0'),
            'Nationality': driver.get('Driver', {}).get('nationality', ''),
            'Constructor': driver.get('Constructors', [{}])[0].get('name', '') if driver.get('Constructors') else ''
        })
    # Create the DataFrame
    df = pd.DataFrame(driver_data)
    
    return df