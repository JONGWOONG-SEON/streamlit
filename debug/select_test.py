import psycopg2
from collections import defaultdict

def main():
    __connection = psycopg2.connect(host='localhost'
                                         , dbname='data'
                                         , user='admin'
                                         , password='admin'
                                         , port='5432')
    __cursor = __connection.cursor()
    sql = """select schemaname, tablename from pg_tables;"""
    __cursor.execute(sql)
    data = __cursor.fetchall()

    data_dict = {}
    for key, value in data:
        if key in data_dict:
            data_dict[key].append(value)
        else:
            data_dict[key] = [value]

    data_dict = list(data_dict.keys())
    print(f"data_dict{data_dict}")

if __name__ == '__main__':
    main()