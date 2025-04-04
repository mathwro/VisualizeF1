import data, util
import streamlit as st
from datetime import datetime
import pandas as pd

def constructor_championship_page():
    st.title("Constructor Championship")
    standings = data.GetChampionshipPoints(datetime.now().year, 'constructorStandings')
    if standings:
        df = ConvertToDataFrame_Constructor(standings)
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

def ConvertToDataFrame_Constructor(data):
    constructor_data = []
    for constructor in data:
        constructor_data.append({
            'Position': constructor.get('position', 'N/A'),
            'Constructor': constructor.get('Constructor', {}).get('name', 'Unknown'),
            'Nationality': constructor.get('Constructor', {}).get('nationality', 'Unknown'),
            'Points': constructor.get('points', 0),
            'Wins': constructor.get('wins', 0)
        })
    print(constructor_data)
    return pd.DataFrame(constructor_data)