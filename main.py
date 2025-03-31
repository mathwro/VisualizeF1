import data, util
import streamlit as st
from datetime import datetime

def main():
    # Filters
    filters = {
        'session_name': 'Race'
    }

    # Get the session data from the API
    sessionData = data.GetData('sessions')

    # Apply all active filters from the filters dictionary
    filtered_sessions = util.applyFilters(sessionData, filters)
    #util.prettyPrintJson(util.getLastX(filtered_sessions, 'date_start', reverse=True, count=3))

    standings = data.GetDriverChampionshipPoints(datetime.now().year)
    util.prettyPrintDriverStandings(standings)

if __name__ == "__main__":
    main()