import psycopg2
import streamlit as st
from driver.preprocessor import preprocess
from sqlalchemy import engine

class call_db:
    def __init__(self, database ,host, dbname, id, pwd, port):
        self.fetch = None
        if database == 'Postgresql':
            self.connection = psycopg2.connection(host=host
                                              , dbname=dbname
                                              , user=id
                                              , password=pwd
                                              , port=port)
            self.cursor = self.connection.cursor()
            st.session_state['database_connection'] = True

    def __call__(self,sql):
        self.cursor.execute(sql)
        self.fetch = self.cursor.fetchall()
        return self.fetch

    def is_connect(self):
        # return st.success("DB connect"),st.rerun()
        return st.success("DB connection")

# class call_db:
#     def __init__(self):
#         engine.Connection()