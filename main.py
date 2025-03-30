import data
import json
import streamlit as st

# Filters
filters = {
    'session_name': 'Race'
}

sessionData = data.GetData('sessions')

# Filter out sessions without 'date_start' field
valid_sessions = [session for session in sessionData if 'date_start' in session]

# Apply all active filters from the filters dictionary
filtered_sessions = valid_sessions
for key, value in filters.items():
    if value:  # Only apply if the filter has a value
        filtered_sessions = [session for session in filtered_sessions if session.get(key) == value]

# Sort sessions by date and get the 3 most recent ones
session3 = sorted(filtered_sessions, key=lambda x: x['date_start'], reverse=True)[:3]

# Pretty print the session data
for session in session3:
    print(json.dumps(session, indent=4))
    
st.title("F1 Session Data")
st.write("This is the F1 Session Data app.")
st.line_chart