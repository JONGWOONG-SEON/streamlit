import streamlit as st
import psycopg2
from driver.connector import call_db
from driver.preprocessor import preprocess
import threading

class database_client(call_db):
    def __init__(self,database,host,dbname,id,pwd,port):
        self.session = None
        self.data = None
        self.call_db = call_db(database,host,dbname,id,pwd,port)
        self.call_db.is_connect()

    def __call__(self, *args, **kwargs):
        sql = """select schemaname, tablename from pg_tables;"""
        self.data = self.call_db.cursor(sql)

    def show_schema(self):
        pre = preprocess(self.data)
        data = pre.return_dict()
        schema = data.keys()
        schema = list(schema)
        return schema


    # @st.dialog("Database")
    # def __call__(self):
    #     self.database = st.selectbox("데이터베이스 선택해주세요"
    #     ,("Postgresql","Vertica")
    #     )
    #     self.host = st.text_input("Host")
    #     self.port = st.text_input("Port")
    #     self.dbname = st.text_input("dbname")
    #     self.id = st.text_input("Id")
    #     self.pwd = st.text_input("Password")
    #     if st.button("Submit"):
    #         if self.database == '' or self.host == '' or self.id == '' or self.pwd == '':
    #             return st.text("입력해주세요.")
    #         else:
    #             cursor = call_db(self.database, self.host, self.dbname, self.id, self.pwd, self.port)
    #             # sql = """select schemaname, tablename from pg_tables where schemaname = 'public';"""
    #             sql = """select schemaname, tablename from pg_tables;"""
    #             data = cursor(sql)
    #             cursor.is_connect()
    #             self.schema_data = cursor.show_schema(data)




# @st.dialog("DataBase")
# def connection_button():
#     database = st.selectbox(
#         "데이터베이스 선택해주세요"
#         ,("Postgresql","Vertica")
#     )
#     st.write("Host")
#     host = st.text_input("Host")
#     port = st.text_input("Port")
#     dbname = st.text_input("dbname")
#     id = st.text_input("Id")
#     pwd = st.text_input("Password")
#
#     if st.button("Submit"):
#        st.session_state.insert = {"Database" : database,"Host": host, "id": id, "pwd" : pwd}
#        if database == '' or host == '' or id == '' or pwd == '':
#            return st.text("입력해주세요.")
#        else:
#            cursor = call_db(database, host, dbname, id, pwd, port)
#            sql = """select schemaname, tablename from pg_tables;"""
#            data = cursor(sql)
#            cursor.is_connect()
#            return cursor.show_schema(data)

# @st.dialog("Choose Table")
# def select_schema():
#     st.selectbox('Schema', data['0'], [])