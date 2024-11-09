import streamlit as st
import psycopg2


def conn(database, host,port,dbname, id, pwd):
    if database == 'Postgresql':
        conn = psycopg2.connect(host = host, dbname = dbname, user = id, password = pwd, port = port)
        st.session_state.dbcon = True
    cur = conn.cursor()
    print(cur)
    return st.success("DB connect"),st.rerun()


@st.dialog("DataBase")
def insert():
    database = st.selectbox(
        "데이터베이스 선택해주세요"
        ,("Postgresql","Vertica")
    )
    st.write("Host")
    host = st.text_input("Host")
    port = st.text_input("Port")
    dbname = st.text_input("dbname")
    id = st.text_input("Id")
    pwd = st.text_input("Password")
    # print(f"{host},{id},{pwd}")
    if st.button("Submit"):
       st.session_state.insert = {"Database" : database,"Host": host, "id": id, "pwd" : pwd}
       if database == '' or host == ''  or id == '' or  pwd == '':
           return st.text("입력해주세요.")
       else:
           print(id)
           con = conn(database, host,port,dbname, id, pwd)
           return print(con)
       # client_db.conn(self)
       st.rerun()


