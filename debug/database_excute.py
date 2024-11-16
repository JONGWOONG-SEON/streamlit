from driver.client import database_client



if __name__ == '__main__':
    data = database_client(database='Postgresql', host='localhost',dbname='data', port='5432', id='admin', pwd='admin')
    data()
    print(data.show_schema())
