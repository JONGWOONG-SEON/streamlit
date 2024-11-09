import streamlit as st

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

import streamlit as st
import driver.client as db
import streamlit_authenticator as stauth


st.write("# 만나서 반갑습니다. 👋")
dbtest = st.button("DBTEST", on_click=db.insert)

st.markdown(
    """
    안녕하세요. 검증용 BI 웹서비스입니다.
    문의사항이 있으시면 dominic.seon@cheilpengtai.com 으로 연락바랍니다.
    
"""
)
st.page_link("http://www.google.com", label="Google", icon="🌎")
st.page_link("http://www.naver.com", label="Naver")