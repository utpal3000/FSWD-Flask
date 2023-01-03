import sqlite3
import traceback
import sys

try:
    sqliteConnection = sqlite3.connect('SQLite_Python.db')
    cursor = sqliteConnection.cursor()
    print("Successfully Connected to SQLite")


    sqlite_create_table_query = '''CREATE TABLE fixedExRate (id INTEGER PRIMARY KEY,USD INTEGER NOT NULL,EUR INTEGER NOT NULL,LastUpDate datetime);'''

    sqlite_insert_query = """INSERT INTO fixedExRate(id, USD, EUR, LastUpDate)  VALUES  (1, )"""

    # count = cursor.execute(sqlite_insert_query)
    # sqliteConnection.commit()
    # print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)

    cursor.execute(sqlite_create_table_query)
    sqliteConnection.commit()
    print("SQLite table created")
    cursor.close()

except sqlite3.Error as error:
    print("Failed to insert data into sqlite table")
    print("Exception class is: ", error.__class__)
    print("Exception is", error.args)
    print('Printing detailed SQLite exception traceback: ')
    exc_type, exc_value, exc_tb = sys.exc_info()
    print(traceback.format_exception(exc_type, exc_value, exc_tb))
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("The SQLite connection is closed")