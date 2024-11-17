import streamlit as st
from driver.client import database_client

class datasource:
    def __init__(self):
        self.database = None
        self.host = None
        self.port = None
        self.dbname = None
        self.id = None
        self.pwd = None

    def database_selection(self):
        if 'database_connection' not in st.session_state:
            self.database = st.selectbox("데이터베이스 선택해주세요"
                                   , ("Postgresql", "Vertica"))
            self.host = st.text_input("Host")
            self.port = st.text_input("Port")
            self.dbname = st.text_input("dbname")
            self.id = st.text_input("Id")
            self.pwd = st.text_input("Password")
            if st.button("Submit"):
                if self.database == '' or self.host == '' or self.id == '' or self.pwd == '':
                    return st.text("입력해주세요.")
                else:
                    global schema_data
                    con = database_client(self.database,self.host,self.dbname,self.id,self.pwd,self.port)
                    con()
                    schema_data = con.show_schema()

    @staticmethod
    def database_selection_stat(database,host,dbname,id,pwd,port):
        if 'database_connection' in st.session_state:
            schema_data = database_client(database,host,dbname,id,pwd,port)
            schema_data()
            return schema_data.show_schema()

def database_selection_callback(Datasource:datasource()):
    Datasource = Datasource()
    if 'database_connection' not in st.session_state:
        Datasource.database_selection()
    else:
        st.selectbox("Choose schema", schema_data, key="database_connection")

"""
# 전역변수로 키 값을 넘겨주는 형식

import streamlit as st
from driver.client import database_client

class datasource:
    def __init__(self):
        self.database = None
        self.host = None
        self.port = None
        self.dbname = None
        self.id = None
        self.pwd = None

    def database_selection(self):
        if 'database_connection' not in st.session_state:
            self.database = st.selectbox("데이터베이스 선택해주세요"
                                   , ("Postgresql", "Vertica"))
            self.host = st.text_input("Host")
            self.port = st.text_input("Port")
            self.dbname = st.text_input("dbname")
            self.id = st.text_input("Id")
            self.pwd = st.text_input("Password")
            if st.button("Submit"):
                if self.database == '' or self.host == '' or self.id == '' or self.pwd == '':
                    return st.text("입력해주세요.")
                else:
                    global info
                    info = {'database': self.database
                            ,'host': self.host
                            ,'dbname': self.dbname
                            ,'id': self.id
                            ,'pwd': self.pwd
                            ,'port': self.port}
                    return info

    @staticmethod
    def database_selection_stat(database,host,dbname,id,pwd,port):
        if 'database_connection' in st.session_state:
            schema_data = database_client(database,host,dbname,id,pwd,port)
            schema_data()
            return schema_data.show_schema()

def database_selection_callback(Datasource:datasource()):
    Datasource = Datasource()
    if 'database_connection' not in st.session_state:
        Datasource.database_selection()
    else:
        Data = Datasource.database_selection_stat(info['database'],info['host'],info['dbname'],info['id'],info['pwd'],info['port'])
        with st.session_state['database_connection']:
            st.selectbox("Choose schema", Data, key='database_connection')


        # data = Database_Selection
        # data()
        # st.selectbox("choose schema",data.show_schema(),[])
        # print(data)
"""