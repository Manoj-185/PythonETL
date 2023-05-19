from sqlalchemy import create_engine
import pandas as pd
import pymysql
pymysql.install_as_MySQLdb()

# extract data from sql server


def extract():
    try:
        engine = create_engine(
            "mysql+mysqldb://root:password@127.0.0.1/teamer_db", pool_recycle=3600, echo=True)
        # conn = engine.connect()
        # src_cursor = mydb.cursor()
        # execute query
        with engine.connect() as mysql_conn:
            src_tables = pd.read_sql(
                "select table_name from information_schema.tables where TABLE_SCHEMA='teamer_db';", mysql_conn)
            # print(src_tables)
            # src_tables = conn.fetchall()
            for tbl in src_tables['TABLE_NAME']:
                df = pd.read_sql(f'select * FROM `teamer_db`.{tbl}', engine)
                load(df, tbl)
    except Exception as e:
        print("Data extract error: " + str(e))
    finally:
        mysql_conn.close()


def new_func(mysql_conn):
    return mysql_conn

 # load data to postgres


def load(df, tbl):
    try:
        rows_imported = 0
        engine = create_engine(
            "postgresql://pitcherogps_dbuser:password@127.0.0.1:5432/teamer_db")
        # connection = engine.raw_connection()
        print(
            f'importing rows {rows_imported} to {rows_imported + len(df)}... for table {tbl}')
        # save df to postgres
        df.to_sql(f'stg_{tbl}', engine,
                  if_exists='replace', index=False)
        rows_imported += len(df)
        # add elapsed time to final print out
        print("Data imported successful")
    except Exception as e:
        print("Data load error: " + str(e))


try:
    # call extract function
    extract()
except Exception as e:
    print("Error while extracting data: " + str(e))
