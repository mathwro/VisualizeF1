import streamlit as st
import data, util
from datetime import datetime
import page_functions.championshipDriver as chd
import page_functions.championshipConstructor as chc



def constructor_championship_page():
    st.title("Constructor Championship")
    # Placeholder for constructor championship data
    st.info("Constructor championship data is not yet implemented.")
    # You can add logic here to fetch and display constructor data.

def main():
    st.sidebar.title("Championships")
    page = st.sidebar.radio("Go to", ["Driver Championship", "Constructor Championship"])

    if page == "Driver Championship":
        chd.driver_championship_page()
    elif page == "Constructor Championship":
        chc.constructor_championship_page()

if __name__ == "__main__":
    main()