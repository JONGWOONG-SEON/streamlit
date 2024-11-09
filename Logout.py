from streamlit_extras.switch_page_button import switch_page
import streamlit as st
import streamlit_authenticator as stauth
# from credential.credential import custom_session
from main import get_auth
from multiprocessing import Process
import requests
import webbrowser

st.session_state.authenticator.logout('test', 'unrendered')
webbrowser.open('http://localhost:8501', new= 0,autoraise=False)