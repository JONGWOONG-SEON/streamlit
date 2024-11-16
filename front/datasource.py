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
                con = database_client(self.database,self.host,self.dbname,self.id,self.pwd,self.port)
                con()
                return self.database,self.host,self.dbname,self.id,self.pwd,self.port

    @staticmethod
    def database_selection_stat(database,host,dbname,id,pwd,port):
        if 'database_connection' in st.session_state:
            schema_data = database_client(database,host,dbname,id,pwd,port)
            schema_data()
            return schema_data.show_schema()

def database_selection_callback(Datasource:datasource()):
    Datasource = Datasource();
    global data
    if 'database_connection' not in st.session_state:
        data = Datasource.database_selection()
    else:
        Data = Datasource.database_selection_stat(data[0],data[1],data[2],data[3],data[4],data[5])
        st.selectbox("Choose schmea", Data)
        # data = Database_Selection
        # data()
        # st.selectbox("choose schema",data.show_schema(),[])
        # print(data)
