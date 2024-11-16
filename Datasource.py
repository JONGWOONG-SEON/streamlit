import driver.client as db
from driver.client import database_client
import streamlit as st
import threading
from front.datasource import database_selection_callback, datasource
col = st.columns(3)

with col[0]:
    st.write("")
with col[1]:
    database_selection_callback(datasource)
with col[2]:
    st.write("")