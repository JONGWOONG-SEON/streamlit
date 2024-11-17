# from driver.client import database_client
from sqlalchemy import engine
#     data = database_client(database='Postgresql', host='localhost',dbname='data', port='5432', id='admin', pwd='admin')
#     data()
#     print(data.show_schema())
#
# db = create_engine(f'{engine_name}://{user_id}:{user_pw}@{host}:{ip}/{db}')

if __name__ == '__main__':

    con = engine.create_engine('postgresql://admin:admin@localhist:5432/data')
    con.connect()
