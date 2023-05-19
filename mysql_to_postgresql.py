# Import necessary libraries
import mysql.connector
import psycopg2

# Connect to the MySQL database
mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="password",
    database="teamer_db",
    port='3306',
    auth_plugin='mysql_native_password',
)

# Connect to the PostgreSQL database
pgdb = psycopg2.connect(
    host="127.0.0.1",
    user="pitcherogps_dbuser",
    password="password",
    database="pitcherogps_db"
)

# Create a cursor to perform operations on the MySQL database
mycursor = mydb.cursor()

# Create a cursor to perform operations on the PostgreSQL database
pgcursor = pgdb.cursor()

# Execute a MySQL query to retrieve the data
mycursor.execute("SELECT table_name FROM information_schema.tables")

# Fetch the result of the MySQL query
mysql_data = mycursor.fetchall()
print("You're connected to database: ", mysql_data)
# Loop through the result and insert each row into the PostgreSQL table
# for row in mysql_data:
#     pgcursor.execute("INSERT INTO postgres_table VALUES (%s, %s, %s)", row)

# # Commit the changes to the PostgreSQL database
# pgdb.commit()

# Close the cursors and databases
mycursor.close()
pgcursor.close()
mydb.close()
pgdb.close()
