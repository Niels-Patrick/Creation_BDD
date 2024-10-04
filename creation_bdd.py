import sqlite3

# Connecting to the database (creating it if not exist)
con = sqlite3.connect("brief_cbdd.db")
# Creating the cursor
cur = con.cursor()

try:
# Opening and reading the SQL file
    with open("Brief_CBDD.sql", "r") as sql_file:
        content = sql_file.read()

    # Spliting the SQL queries
    content_list = content.split(";", 1)
    # Executing the content of the SQL file, creating the database's tables
    for query in content_list:
        cur.execute(query)
except:
    con.rollback()
finally:
    # Closing the connection
    con.close()
