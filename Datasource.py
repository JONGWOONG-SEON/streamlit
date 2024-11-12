import driver.client as db
from driver.client import database_client
import streamlit as st
import threading
from front.datasource import database_selection


if 'database_connection' not in st.session_state:
    database_selection()
    if 'database_connection' in st.session_state:
        with st.sidebar:
            st.write("DataBase Connection")