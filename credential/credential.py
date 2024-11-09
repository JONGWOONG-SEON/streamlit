import yaml
import streamlit_authenticator as stauth
import streamlit as st


class custom_session:
    with open('credential/config.yaml') as file:

        config = yaml.load(file, Loader=stauth.SafeLoader)
        authenticator = stauth.Authenticate(
            config['credentials'],
            config['cookie']['name'],
            config['cookie']['key'],
            config['cookie']['expiry_days']
        )
    def __init__(self):

    def is_check(self):
        if 'authenticated' not in st.session_state:
            return self.authenticator.login()
        if st.session_state['authentication_status'] == None:
            return self.authenticator.login()
        elif st.session_state['authentication_status'] == None:
            return self.authenticator.login()

    def is_print(self):
        st.write(self.authenticator)
