import driver.client as db
from driver.client import database_client
import streamlit as st

data = database_client()
if 'database_connection' in st.session_state:
    st.selectbox('choose schema', data.show_schema())
    with st.sidebar:
        st.write("db connection")