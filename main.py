# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022-2024)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from pathlib import Path
import os
import streamlit as st
import streamlit_authenticator as stauth
import yaml
import time


dir_path = Path(__file__).parent
source_path = os.path.join(os.getcwd(),'source')

def get_auth():
    with open('config.yaml') as file:
        config = yaml.load(file, Loader=stauth.SafeLoader)

    st.session_state.authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days']
    )
    return st.session_state.authenticator

def login():
    auth = get_auth()
    st.session_state.authenticator.login(key="login")

    if st.session_state['authentication_status'] == False:
        st.error("Username/password is incorrect")

    if st.session_state['authentication_status'] == None:
        st.warning("Please enter your username and password")

    if st.session_state['authentication_status']:
        time.sleep(0.5)
        run()

def run():
    page = {
        "Default":
        [
            st.Page(dir_path / "Home.py", icon="🏠"),
            st.Page(dir_path / "Logout.py", icon="🤚"),
        ],
        "Sales":[
            st.Page(os.path.join(source_path,"Sales.py"), icon="📈"),
            st.Page(os.path.join(source_path,"Sales_spark.py"), icon=":material/animation:")
        ],
        "Datasource":[
            st.Page(dir_path / "Datasource.py")
        ]

    }
    st.navigation(page).run()


if __name__ == "__main__":
    st.set_page_config(page_title="Dominic_Page",layout = 'wide',initial_sidebar_state='auto',
                       menu_items={
                           # 'Logout': 'http://localhost:8502/Logout'
                       }

    )
    login()