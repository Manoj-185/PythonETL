import mysql.connector as msql
#from mysql.connector import error
import pandas as pd

#sql = "SELECT * FROM teamer_db.users";

# db = connection.connect(user='root',password='password',host='127.0.0.1',port='3306',database='teamer_db',
# auth_plugin='mysql_native_password')

# creating a connection to mysql database
try:
  connection = msql.connect(user='root',password='password',host='127.0.0.1',port='3306',database='teamer_db',auth_plugin='mysql_native_password')
  if connection.is_connected():
      db_Info = connection.get_server_info()
      print("Connected to MySQL Server version ", db_Info)  # getting the
      #server info
      cursor = connection.cursor()
      # selecting the database diamond
      cursor.execute("select database();")
      record = cursor.fetchone()
      print("You're connected to database: ", record)
      mycursor = connection.cursor()
      # executing the query to fetch all record from diamond record
      #mycursor.execute("SELECT * from teamer_db.users")
      #table_rows = mycursor.fetchall()

      df = pd.read_sql("SELECT * from teamer_db.users", connection)
      df.head()
      df.to_excel("mysql_date.xlsx", index=False)

# except Error as e:
#   print("Error while connecting to MySQL", e)

finally:
  if connection.is_connected():
      cursor.close()
      connection.close()
      print('mysql connection is closed')
