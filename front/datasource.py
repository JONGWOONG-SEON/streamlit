import streamlit as st
from driver.client import database_client

def database_selection():
    database = st.selectbox("데이터베이스 선택해주세요"
                                 , ("Postgresql", "Vertica")
                                 )
    host = st.text_input("Host")
    port = st.text_input("Port")
    dbname = st.text_input("dbname")
    id = st.text_input("Id")
    pwd = st.text_input("Password")
    if st.button("Submit"):
        if database == '' or host == '' or id == '' or pwd == '':
            return st.text("입력해주세요.")
        else:
            return database_client(database,host,dbname,id,pwd,port)